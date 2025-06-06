# Model Customization

**Framework**: Core ML

Expand and modify your model with new layers.

#### Overview

Customize your Core ML model to make it work better for your specific app. For instance, create one or more custom layers to improve accuracy by increasing the model’s capacity to capture information. You can also reduce the model’s size to optimize the contents of your app bundle.

## Topics

### Model File Size
- [Reducing the Size of Your Core ML App](reducing-the-size-of-your-core-ml-app.md)
  Reduce the storage used by the Core ML model inside your app bundle.
### Custom Model Layers
- [Creating and Integrating a Model with Custom Layers](creating-and-integrating-a-model-with-custom-layers.md)
  Add models with custom neural-network layers to your app.
- [protocol MLCustomLayer](mlcustomlayer.md)
  An interface that defines the behavior of a custom layer in your neural network model.
### Custom Models
- [protocol MLCustomModel](mlcustommodel.md)
  An interface that defines the behavior of a custom model.

## See Also

- [Getting a Core ML Model](getting-a-core-ml-model.md)
  Obtain a Core ML model to use in your app.
- [Updating a Model File to a Model Package](updating-a-model-file-to-a-model-package.md)
  Convert a Core ML model file into a model package in Xcode.
- [Integrating a Core ML Model into Your App](integrating-a-core-ml-model-into-your-app.md)
  Add a simple model to an app, pass input data to the model, and process the model’s predictions.
- [class MLModel](mlmodel.md)
  An encapsulation of all the details of your machine learning model.
- [Model Personalization](model-personalization.md)
  Update your model to adapt to new data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/model-customization)*