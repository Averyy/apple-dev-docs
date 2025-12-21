# Downloading and Compiling a Model on the User’s Device

**Framework**: Core ML

Install Core ML models on the user’s device dynamically at runtime.

#### Overview

Download and compile models within your app as an alternative to bundling with the app. Scenarios where this is a practical approach include:

- Reducing the app’s download size of your app on the App Store
- Determining the right models for the user after installation based on their location, specific interests, and A/B testing
- Providing model updates over the network

##### Download and Compile the Model in the Background

Download the model definition file (ending in `.mlmodel`) onto the user’s device by using [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession), [`CloudKit`](https://developer.apple.com/documentation/CloudKit), or another networking toolkit. Then compile the model definition by calling [`compileModel(at:)`](mlmodel/compilemodel(at:)-6442s.md).

```swift
let compiledModelURL = try MLModel.compileModel(at: modelDescriptionURL)
```

This creates a new, compiled model file with the same name as the model description but ending in `.mlmodelc`. Create a new [`MLModel`](mlmodel.md) instance by passing the compiled model [`URL`](https://developer.apple.com/documentation/Foundation/URL) to its initializer.

```swift
let model = try MLModel(contentsOf: compiledModelURL)
```

Model instances you create from model files you’ve downloaded have the same capabilities as those you create from model files that you bundle with your app.

##### Save Reusable Models to a Permanent Location

[`MLModel`](mlmodel.md) saves models it compiles to a temporary location. If your app can reuse the model later, reduce your resource consumption by saving the compiled model to a permanent location.

Build the [`URL`](https://developer.apple.com/documentation/Foundation/URL) to a permanent location that your app can access in the future, such as Application Support.

```swift
let fileManager = FileManager.default
let appSupportURL = fileManager.urls(for: .applicationSupportDirectory,
                                     in: .userDomainMask).first!
```

Create the [`URL`](https://developer.apple.com/documentation/Foundation/URL) for the permanent compiled model file.

```swift
let compiledModelName = compiledModelURL.lastPathComponentlet
permanentURL = appSupportURL.appendingPathComponent(compiledModelName)
```

Move or copy the file to its permanent location.

```swift
// Copy the file to the permanent location, replacing it if necessary.
_ = try fileManager.replaceItemAt(permanentURL,
                                  withItemAt: compiledModelURL)

```

> ❗ **Important**:  You should consider the user’s iCloud Backup size when saving large, compiled Core ML models. You can store models in the app’s container using /tmp and /Library/Caches directories, which contain purgeable data that isn’t backed up. When the models aren’t purgeable, you can exclude them from backup by setting the [`isExcludedFromBackup`](https://developer.apple.com/documentation/Foundation/URLResourceValues/isExcludedFromBackup) resource value to `true`. To learn more about excluding files from iCloud Backup, see [`Optimizing Your App’s Data for iCloud Backup`](https://developer.apple.com/documentation/Foundation/optimizing-your-app-s-data-for-icloud-backup).

## See Also

- [Model Integration Samples](model-integration-samples.md)
  Integrate tabular, image, and text classifcation models into your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/downloading-and-compiling-a-model-on-the-user-s-device)*