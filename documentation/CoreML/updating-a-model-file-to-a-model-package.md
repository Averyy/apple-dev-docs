# Updating a Model File to a Model Package

**Framework**: Core ML

Convert a Core ML model file into a model package in Xcode.

#### Overview

A Core ML model package is a file-system structure that can store a model in separate files, similar to an app bundle. Model packages offer more flexibility and extensibility than Core ML model files, including editable metadata and separation of a model’s architecture from its weights and biases. Update your model file to a model package by converting the model in Xcode.

Open or select a Core ML model in Xcode and update it to an ML package by either clicking the Edit button or the Update to Model Package button in the Utilities tab.

![Screenshot of a model window in Xcode highlighting the Edit button in the window’s upper-right corner, and the Model Update section in the window’s Utility tab that includes an “Update to Model Package” button.](https://docs-assets.developer.apple.com/published/cef4d987e8b802b35bac75a347543bd5/media-3846185%402x.png)

Xcode presents a confirmation dialog before it converts the model to the ML package format. By default, Xcode moves the original model file to the Trash. You can keep your original model file by deselecting the checkbox in the Xcode dialog. Click Update and Edit when you’re ready to convert the model to a package.

Once Xcode finishes converting the model, it opens the model’s General tab, where you can edit any of the metadata text fields, including Description, Author, and License.

![Screenshot of a model window highlighting the metadata, which shows the user currently editing the License text field.](https://docs-assets.developer.apple.com/published/550d8743bf5e04f9f7ed75d63aae605d/media-3846183%402x.png)

You can also add a new metadata field in an ML package by entering a new property name and value in the Additional Metadata section.

## See Also

- [Getting a Core ML Model](getting-a-core-ml-model.md)
  Obtain a Core ML model to use in your app.
- [Integrating a Core ML Model into Your App](integrating-a-core-ml-model-into-your-app.md)
  Add a simple model to an app, pass input data to the model, and process the model’s predictions.
- [class MLModel](mlmodel.md)
  An encapsulation of all the details of your machine learning model.
- [Model Customization](model-customization.md)
  Expand and modify your model with new layers.
- [Model Personalization](model-personalization.md)
  Update your model to adapt to new data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/updating-a-model-file-to-a-model-package)*