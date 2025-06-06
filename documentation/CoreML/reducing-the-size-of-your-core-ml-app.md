# Reducing the Size of Your Core ML App

**Framework**: Core ML

Reduce the storage used by the Core ML model inside your app bundle.

#### Overview

Bundling your machine learning model in your app is the easiest way to get started with Core ML. As models get more advanced, they can become large and take up significant storage space. For a neural-network based model, consider reducing its footprint by using a lower precision representation for its weight parameters. If your model isn’t a neural network that can use lower precision or you need to further reduce your app’s size, add functionality to download and compile your models on the user’s device instead of bundling the models with your app.

##### Convert to a Lower Precision Model

The [`Core ML Tools`](https://developer.apple.comhttps://coremltools.readme.io/) provide utilities to convert a neural network model’s floating point weights from full-precision into half-precision values — reducing the number of bits used in the representation from 32 down to 16 — or lower precisions of 1 to 8 bits. For more information about using these utilities, see the [`Core ML Tools Neural Network Quantization documentation`](https://developer.apple.comhttps://coremltools.readme.io/docs/quantization).

##### Download and Compile a Model

Another option to reduce the size of your app is to have the app download the model onto the user’s device and compile it in the background. For example, if users use only a subset of the models your app supports, you don’t need to bundle all the possible models with your app. Instead, the models can be downloaded later based on user behavior. See [`Downloading and Compiling a Model on the User’s Device`](downloading-and-compiling-a-model-on-the-user-s-device.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/reducing-the-size-of-your-core-ml-app)*