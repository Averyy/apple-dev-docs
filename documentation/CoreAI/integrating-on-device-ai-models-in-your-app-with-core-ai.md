# Integrating on-device AI models in your app with Core AI

**Framework**: Core AI

Power your app’s intelligent features with an on-device AI model.

#### Overview

Core AI allows you to deploy AI models within your app. Inference happens on device, so data stays private, AI features can be readily available and work offline, and there is no per-inference cost to you or the people using your app.

You start with an `.aimodel` file, either converted from a model using the [`Core AI PyTorch Extensions Python package`](https://developer.apple.comhttps://apple.github.io/coreai-torch) or already prepared in the correct format. The model it represents should contain one or more inference functions needed to power your app’s intelligent features.

#### Add the Model File to Your Project

To use a Core AI model, your app needs access to the `.aimodel` file at runtime. You can bundle the file directly in your Xcode project or Swift package, or your app can download it over the network. The following steps show how to bundle and configure the model in Xcode.

Start by adding the model file to an Xcode target:

1. Drag the `.aimodel` file from the Finder into the Project Navigator in Xcode, or choose File > Add Files to add it.
2. When the sheet appears, select the targets to include the model under Add to targets, then review the remaining options.

1. Click Finish.

> **Note**: After adding the file, you should also see the model in the Compile Sources build phase for that target.

#### Add the Metal Toolchain to Xcode

Core AI model integration in Xcode requires the Metal Toolchain, which isn’t installed by default. There are two options for adding the Metal Toolchain:

1. In Xcode, choose Xcode > Settings > Components > Other Components, then click Get to download and install the Metal Toolchain.

1. In Xcode, select any `.aimodel` file in your project and click the Get button in the Metal toolchain download bar that appears.

> ❗ **Important**: If the Metal toolchain isn’t included, builds that include `.aimodel` files fail with a missing Metal compiler error.

#### Inspect the Model in Xcode

Before writing the code to use the model in your app, you can view its details in the Xcode model viewer by selecting the `.aimodel` file in the Project Navigator.

The model viewer has several tabs for exploring different aspects of your model. The General tab shows the model’s size, in number of parameters and storage size on disk, along with metadata such as description, author, license, and creator-defined key-value pairs. You can edit metadata fields inline; Xcode saves your changes automatically.

![A screenshot of the General tab of the Xcode model viewer, showing the model’s parameter count, storage size on disk, and metadata fields including description, author, license, and creator-defined key-value pairs.](https://docs-assets.developer.apple.com/published/1390b481a9ff634e4264297510fd3703/model-viewer-metadata%402x.png)

The General tab also shows the model’s numeric precision, split into compute and storage categories:

- Compute types are the representations used during inference.
- Storage types are the representations used for the model’s weights on disk.
- The operation distribution shows a breakdown of operations in the model’s graph, sorted by count.

#### Review Inference Functions

The Functions tab shows the exact function signature of each function in the model, including the names, types, and optional descriptions for each input and output.

![A screenshot of the Functions tab of the Xcode model viewer, listing the model’s inference functions with their input and output tensor names, type signatures, and descriptions.](https://docs-assets.developer.apple.com/published/70737fb5dde5db5db7d6d82b478b97e4/model-viewer-functions%402x.png)

Most models have a single function. The named inputs and outputs describe what data your code provides and what it returns. A question mark in an `NDArray` dimension means the dimension is dynamic and is supplied or determined at runtime.

#### Load the Model

Load the model in your app by creating an [`AIModel`](aimodel.md) from the `.aimodel` file.

```swift
import CoreAI

// Specialize the model for this device and load it.
let model = try await AIModel(contentsOf: urlOfModel)

// Load a function from the model.
guard let function = try model.loadFunction(named: "main") else {
    // Handle case where expected function is not found.
}
```

Core AI specializes the model for the current device, considering all available compute units and selecting the combination that delivers the best performance. [`init(contentsOf:options:)`](aimodel/init(contentsof:options:).md) is asynchronous because specialization needs to complete before a valid `AIModel` is returned. Depending on the model size, specialization can take a significant amount of time.

Call [`loadFunction(named:)`](aimodel/loadfunction(named:).md) to get an [`InferenceFunction`](inferencefunction.md) for running the model with your inputs and receiving its outputs. Loading a function prepares the resources needed to run that function and can also be expensive. The method throws on a load failure, and returns `nil` when no function with that name exists. For more information, see [`Managing model specialization and caching`](managing-model-specialization-and-caching.md).

Most models have a single function. If the model contains multiple functions, check [`functionNames`](aimodel/functionnames.md) to see all available names. If your app processes multiple inputs simultaneously, you can safely call the same inference function from different tasks.

#### Inspect Function Inputs and Outputs

Depending on your model deployment strategy, you may need to inspect the model’s inference function at runtime. Each inference function has an [`InferenceFunctionDescriptor`](inferencefunctiondescriptor.md) that describes the names, types, and shapes of its inputs and outputs. You can use this descriptor to verify that a function accepts the inputs your app provides, or to dynamically adapt your app’s behavior as the model’s inputs and outputs change between deployments, without needing to change your code.

For example, you can check that the function’s input matches the shape and type your app expects:

```swift
let function: InferenceFunction = ...

let functionDescriptor = function.descriptor
guard let valueDescriptor = functionDescriptor.inputDescriptor(of: "input"),
      case .ndArray(let arrayDescriptor) = valueDescriptor else {
        // Handle input not found, or an unexpected type.
}

guard arrayDescriptor.shape == [3, 4] else {
    // Handle an unexpected shape.
}

guard arrayDescriptor.scalarType == .float32 else {
    // Handle an unexpected scalar type.
}
```

The [`inputDescriptor(of:)`](inferencefunctiondescriptor/inputdescriptor(of:).md) method returns an [`InferenceValue.Descriptor`](inferencevalue/descriptor.md) for a named input. The descriptor tells you whether the input expects an [`NDArray`](ndarray.md) or an image, along with its shape and type.

#### Run Inference

The [`NDArray`](ndarray.md) type represents the input and output tensors from the converted model function at runtime. Values marked as images at conversion time use [`CVMutablePixelBuffer`](https://developer.apple.com/documentation/CoreVideo/CVMutablePixelBuffer). Pass your data using the same input names defined at model conversion time.

For [`NDArray`](ndarray.md) values, write input data with [`NDArray.MutableView`](ndarray/mutableview.md) and read results with [`NDArray.View`](ndarray/view.md). Swift enforces this at compile time. A mutable view allows writes, and a view allows only reads, so you always know how your data is accessed.

Start by creating an `NDArray` that matches the shape and type the model expects:

```swift
// Create an `NDArray` that matches the expected type and shape.
var input = NDArray(shape: [3, 4], scalarType: .float32)
```

Because an [`NDArray`](ndarray.md) is an *n*-dimensional array, the shape should match what the model expects. In this example, `[3, 4]` matches the input shape defined at the `.aimodel` creation. The [`NDArray.ScalarType`](ndarray/scalartype-swift.enum.md) defines what kind of number each element holds, such as [`NDArray.ScalarType.float32`](ndarray/scalartype-swift.enum/float32.md) for 32-bit floating-point values.

An `NDArray` is read-only by default. To write data into it, call [`mutableView(as:)`](ndarray/mutableview(as:).md) which gives you direct write access to the underlying memory:

```swift
// Access a mutable view to write data into the array.
var mutableView = input.mutableView(as: Float.self)
guard let elements = mutableView.contiguousElements else {
    // Handle non-contiguous memory layout.
}

// Your function that writes input data into the mutable span.
writeInputData(into: elements)
```

When the input data is ready, pass the [`NDArray`](ndarray.md) to the inference function to run the model:

```swift
// Run the function with the `NDArray` input.
var outputs = try await function.run(inputs: ["input": input])
```

After the model runs, call [`remove(_:)`](inferencefunction/outputs/remove(_:).md) with the output name to extract each result. The result is an [`InferenceValue`](inferencevalue.md) which holds either an `NDArray` or an image. To check which type your output uses, look at the function signature in the model viewer’s Functions tab, or inspect the [`InferenceFunctionDescriptor`](inferencefunctiondescriptor.md) at runtime. Access the output with `.ndArray` or `.pixelBuffer` based on the type.

To read data from an output `NDArray`, access an [`NDArray.View`](ndarray/view.md):

```swift
// Extract the returned output.
guard let predictionValue = outputs.remove("prediction") else {
    // Handle output not found.
}

guard let prediction = predictionValue.ndArray else {
    // Handle output of unexpected type of value.
}

// Read the output data through a view.
// Your function that processes the output.
processOutput(prediction.view())
```

## See Also

- [struct AIModel](aimodel.md)
  A specialized model for running inference on a device.
- [struct AIModelAsset](aimodelasset.md)
  An unspecialized source model asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/integrating-on-device-ai-models-in-your-app-with-core-ai)*