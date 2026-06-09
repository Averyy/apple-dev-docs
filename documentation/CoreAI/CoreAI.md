# Core AI

**Framework**: Core AI  
**Kind**: module

Run AI models in your app on Apple silicon.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

#### Overview

Core AI helps you build, run, and deploy AI models in your app. Designed with Apple silicon in mind, Core AI allows your app to use the latest model architectures and inference techniques across the CPU, GPU, and Neural Engine. The Swift API makes common tasks simple, while giving you more control over model specialization, caching, and inference performance when needed.

![An illustration showing AI models connecting to Apple devices.](https://docs-assets.developer.apple.com/published/3436c2b440f83e13deb0e14474c5e08e/core-ai-framework-hero%402x.png)

Alongside the framework, Core AI includes additional tools for model preparation, integration, and debugging. Prepare your models for Apple silicon with [`Core AI Optimization`](https://developer.apple.comhttps://apple.github.io/coreai-optimization), then convert them into the `.aimodel` format with [`Core AI PyTorch Extensions`](https://developer.apple.comhttps://apple.github.io/coreai-torch). The [`Core AI Debugger`](https://developer.apple.comhttps://developer.apple.com/core-ai-debugger/) app supports visualization and numeric debugging, letting you inspect model structure and trace tensor values directly back to your Python source code.

Core AI also integrates with Xcode and the developer toolchain. The Core AI debug gauge and Core AI instrument help you monitor and profile inference performance in your app. You can also compile models ahead of time with the `coreai-build` command-line tool.

If your app uses model types other than neural networks, such as decision trees or tabular feature engineering, see [`Core ML`](https://developer.apple.com/documentation/CoreML).

## Topics

### Essentials
- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)
  Power your app’s intelligent features with an on-device AI model.
- [struct AIModel](aimodel.md)
  A specialized model for running inference on a device.
- [struct AIModelAsset](aimodelasset.md)
  An unspecialized source model asset.
### Inference
- [struct InferenceFunction](inferencefunction.md)
  A function that performs inference on input values and produces output values.
- [struct InferenceFunctionDescriptor](inferencefunctiondescriptor.md)
  A description of an inference function’s signature.
- [struct InferenceValue](inferencevalue.md)
  A value that an inference function accepts as input or produces as output.
- [struct ImageDescriptor](imagedescriptor.md)
  A description of an image’s dimensions and pixel format.
- [class ComputeStream](computestream.md)
  A stream of work to be run asynchronously.
### Multidimensional arrays
- [struct NDArray](ndarray.md)
  A multidimensional array of scalar values used for model inference.
- [struct NDArrayDescriptor](ndarraydescriptor.md)
  A description of an array’s shape, scalar type, and memory layout expectations.
### Configuration
- [Managing model specialization and caching](managing-model-specialization-and-caching.md)
  Configure model specialization, manage cached assets, and reduce your app’s storage footprint.
- [Compiling Core AI models ahead of time](compiling-core-ai-models-ahead-of-time.md)
  Reduce on-device specialization time by compiling Core AI models at build time.
- [class AIModelCache](aimodelcache.md)
  A cache that stores the specialized model artifacts for inference.
- [enum ComputeUnitKind](computeunitkind.md)
  A type of hardware compute unit available for model inference.
- [struct SpecializationOptions](specializationoptions.md)
### Debugging and performance
- [Inspecting, debugging, and profiling Core AI models](inspecting-debugging-and-profiling-core-ai-models.md)
  Investigate model behavior, monitor activity, and profile performance using the Core AI tools across Xcode and the Core AI Debugger app.
### Errors
- [struct AssetError](asseterror.md)
  An error that occurs during model asset operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreAI)*