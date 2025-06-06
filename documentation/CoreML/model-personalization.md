# Model Personalization

**Framework**: Core ML

Update your model to adapt to new data.

#### Overview

On-device model updates provide your app the flexibility to personalize a user’s experience. For example, ordering a mocha at your favorite coffee shop every day increases a model’s ability to recommend that drink on subsequent visits. With the Core ML framework, you can adapt to incoming data with an updatable model at runtime on the user’s device.

## Topics

### On-Device Model Updates
- [class MLTask](mltask.md)
  An abstract base class for machine learning tasks.
- [Personalizing a Model with On-Device Updates](personalizing-a-model-with-on-device-updates.md)
  Modify an updatable Core ML model by running an update task with labeled data.
- [class MLUpdateTask](mlupdatetask.md)
  A task that updates a model with additional training data.

## See Also

- [Getting a Core ML Model](getting-a-core-ml-model.md)
  Obtain a Core ML model to use in your app.
- [Updating a Model File to a Model Package](updating-a-model-file-to-a-model-package.md)
  Convert a Core ML model file into a model package in Xcode.
- [Integrating a Core ML Model into Your App](integrating-a-core-ml-model-into-your-app.md)
  Add a simple model to an app, pass input data to the model, and process the model’s predictions.
- [class MLModel](mlmodel.md)
  An encapsulation of all the details of your machine learning model.
- [Model Customization](model-customization.md)
  Expand and modify your model with new layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/model-personalization)*