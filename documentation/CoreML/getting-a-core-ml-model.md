# Getting a Core ML Model

**Framework**: Core ML

Obtain a Core ML model to use in your app.

#### Overview

Core ML supports a variety of machine learning models, including neural networks, tree ensembles, support vector machines, and generalized linear models. Core ML requires the Core ML model format (models with a `.mlmodel` file extension).

Using [`Create ML`](https://developer.apple.com/documentation/CreateML) and your own data, you can train custom models to perform tasks like recognizing images, extracting meaning from text, or finding relationships between numerical values. Models trained using Create ML are in the Core ML model format and are ready to use in your app.

Apple also provides several popular, open source [`models`](https://developer.apple.comhttps://developer.apple.com/machine-learning/models/) that are already in the Core ML model format. You can download these models and start using them in your app.

Additionally, various research groups and universities publish their models and training data, which may not be in the Core ML model format. Use [`Core ML Tools`](https://developer.apple.comhttps://coremltools.readme.io/) to convert these models to use in your app.

## See Also

- [Updating a Model File to a Model Package](updating-a-model-file-to-a-model-package.md)
  Convert a Core ML model file into a model package in Xcode.
- [Integrating a Core ML Model into Your App](integrating-a-core-ml-model-into-your-app.md)
  Add a simple model to an app, pass input data to the model, and process the model’s predictions.
- [class MLModel](mlmodel.md)
  An encapsulation of all the details of your machine learning model.
- [Model Customization](model-customization.md)
  Expand and modify your model with new layers.
- [Model Personalization](model-personalization.md)
  Update your model to adapt to new data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/getting-a-core-ml-model)*