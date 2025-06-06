# Generating a Model Encryption Key

**Framework**: Core ML

Create a model encryption key to encrypt a compiled model or model archive.

#### Overview

Use a model’s encryption key to encrypt a model archive for deployment or to encrypt a model compiled and bundled into your app.

> ❗ **Important**:  You must have signed in with your Apple ID in the Apple ID pane in System Preferences to generate a model encryption key in Xcode.

 You must have signed in with your Apple ID in the Apple ID pane in System Preferences to generate a model encryption key in Xcode.

##### Create the Model Encryption Key

Open a model in Xcode, click the Utilities tab, and click Create Encryption Key.

![Screenshot of a Model window in Xcode highlighting the Utilities tab halfway down the window, and the “Create Encryption Key” button below it on the left.](https://docs-assets.developer.apple.com/published/4247a10c563525aa726aeb05a38d9d4e/media-3691089%402x.png)

Select the development team that your app’s target uses from the menu, and click Continue.

![Screenshot of an Xcode dialog, “Generate Encryption Key” prompting the user with text that reads, “Choose the development team you would like to associate with this encryption key. This team should match the team your app is signed with.”](https://docs-assets.developer.apple.com/published/10927eb9d7d2adafc9674d0c9e86a7bd/media-3694274%402x.png)

Xcode’s confirmation dialog provides an arrow button that takes you to the encryption key in Finder.

![Screenshot of an Xcode confirmation dialog, “Model Key Generated”, highlighting a circular button with an inscribed right arrow to the right of the text, “Classifier dot ML model key saved to disk.” The dialog has two additional informational tips: The first reads, “Encrypt this model for a specific target by navigating to Build Phases (right arrow), Compile Sources and adding “dash-dash path to dot ML model key” to the model’s Compiler Flags.” The second reads, “Optionally, to encrypt a model for Cloud Kit deployment, you can use this dot ML model key when you generate a Model Archive.”](https://docs-assets.developer.apple.com/published/94a0ae878525634e39afcc5608592fa7/media-3691090%402x.png)

##### Locate the Model Encryption Key

Use the first button in the confirmation dialog to show the model encryption key in Finder, or navigate to the model’s enclosing folder.

![Screenshot of a Finder window showing one selected file, Classifier dot ML-model-key, which is next to its related file, Classifier dot ML-model.](https://docs-assets.developer.apple.com/published/cf3cf689c60ce65332ae1a538c223514/media-3690965%402x.png)

Xcode saves the model encryption key file in the same folder as the original model file, and uses its base name with the `.mlmodelkey` extension. For example, the encryption key for a model named `Classifier.mlmodel` has the name `Classifier.mlmodelkey` in the same directory.

Use this model encryption file to:

- Encrypt a model archive as you generate it using Xcode (see `Generating a Model Archive`).
- Encrypt a model that Xcode includes in your app’s bundle as it compiles the model (see [`Encrypting a Model in Your App`](encrypting-a-model-in-your-app.md)).

## See Also

- [Encrypting a Model in Your App](encrypting-a-model-in-your-app.md)
  Encrypt your app’s built-in model at compile time by adding a compiler flag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/generating-a-model-encryption-key)*