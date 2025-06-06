# Creating and Integrating a Model with Custom Layers

**Framework**: Coreml

Add models with custom neural-network layers to your app.

#### Overview

New network layers and architectures solve problems that might be difficult or impractical with code. You can support each new layer type before Core ML directly supports it by implementing a . A custom layer is a class that adopts [`MLCustomLayer`](mlcustomlayer.md) and implements the methods to run a neural network layer in code.

> **Note**:  Core ML supports models with custom layers beginning with these software releases: iOS 11.2, macOS 10.13.2, tvOS 11.2 and watchOS 4.2.

##### Add a Model You Acquire or Create

If you have a Core ML model with custom layers, add the model to your Xcode project.

Otherwise, convert a third-party model and designate the new layers as custom with the [`Core ML Tools`](https://developer.apple.comhttps://coremltools.readme.io). Follow the steps on the [`Custom Operators`](https://developer.apple.comhttps://coremltools.readme.io/docs/custom-operators) page to define the new layers as custom. Give each custom layer a unique name by assigning a unique string to the operator’s class name binding.

```python
bindings = {
    'class_name'  : 'AAPLCustomAdd',
    'description' : "Custom implementation of addition."
    ...
}
```

Save the Core ML model you converted and add it to your Xcode project.

##### Integrate or Create a Class for Each Custom Layer

If the author of the model you plan to add to your Xcode project implemented the custom layers in source-code files, add the source files into your Xcode project.

Otherwise, implement each custom layer by creating a Swift or Objective-C class for each layer. Inspect the names of the model’s custom layers by opening the model in Xcode:

![Screenshot of a model view in Xcode that shows three custom layers in the Dependencies section: AAPLCustomAdd, AAPLCustomInnerProduct, and AAPLCustomConvolution.](https://docs-assets.developer.apple.com/published/07fa13d1f488c3a10fd68a42d3148e2b/media-3744502%402x.png)

Create a class for each custom layer that the model has in its list of dependencies and name each class to match the custom layer it implements.

> ❗ **Important**:  Swift classes must subclass [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class) and use the `@objc` attribute so that Core ML can access your custom layer’s implementation.

Adopt the [`MLCustomLayer`](mlcustomlayer.md) protocol by implementing the following:

Core ML invokes the appropriate [`MLCustomLayer`](mlcustomlayer.md) methods for each custom layer at runtime when your app calls the [`prediction(from:)`](mlmodel/prediction(from:)-9y2aa.md) method.

> ⚠️ **Warning**:  Don’t change the values that Core ML provides to these methods — such as weights, inputs, or outputs — because it may cause your app to behave in unexpected ways, and possibly crash.

##### Test the Custom Layers

If applicable, test the custom layers by using the model to make predictions with input values from one or more test cases. Confirm the model layers function correctly by comparing the model’s prediction values to the output values for each test case.

## See Also

- [protocol MLCustomLayer](mlcustomlayer.md)
  An interface that defines the behavior of a custom layer in your neural network model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreML/creating-and-integrating-a-model-with-custom-layers)*