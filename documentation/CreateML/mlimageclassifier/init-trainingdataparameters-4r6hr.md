# init(trainingData:parameters:)

**Framework**: Createml  
**Kind**: init

Creates an image classifier with a training dataset represented by a data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(trainingData: MLImageClassifier.DataSource, parameters: MLImageClassifier.ModelParameters = ModelParameters(
            validation: .split(strategy: .automatic),
            augmentation: [],
            algorithm: .transferLearning(
                featureExtractor: .scenePrint(revision: 1),
                classifier: .logisticRegressor
            )
        )) throws
```

## Mentions

- [Creating an Image Classifier Model](creating-an-image-classifier-model.md)

#### Discussion

When you create an [`MLImageClassifier`](mlimageclassifier.md) instance, initialize it with an [`MLImageClassifier.ModelParameters`](mlimageclassifier/modelparameters-swift.struct.md) structure. This allows you to configure the image classifier training process. For example, you can explicitly define the validation dataset instead of allowing the model to choose a random selection of your training data. Alternatively, as shown in the following example, set `validationData` to `nil` to allow the classifier to choose the validation data for you from among your training data. This lets you set other parameters—like maximum iterations and augmentation options—to values other than the default.

```swift
let parameters = MLImageClassifier.ModelParameters(
    featureExtractor: .scenePrint(revision: 1),
    validationData: nil,
    maxIterations: 20,
    augmentationOptions: [.crop]
)
```

Use the parameter structure and your training data to build a classifier. The following example uses training data from labeled directories within a directory called `Training`, which resides in the `Downloads` directory:

```swift
if let downloads = FileManager.default.urls(for: .downloadsDirectory, in: .userDomainMask).first {
    let trainingURL = downloads.appendingPathComponent("Training")
    let classifier = try MLImageClassifier(
        trainingData: .labeledDirectories(at: trainingURL),
        parameters: parameters
    )
}
```

Training begins immediately.

> **Note**: If you represent your training data with a dictionary of strings and corresponding URL arrays, use [`init(trainingData:parameters:)`](mlimageclassifier/init(trainingdata:parameters:)-7j4w6.md) instead.

## Parameters

- `trainingData`: A set of labeled images the task uses to train the image classifier model, contained in a   data source.
- `parameters`: An   instance you use to configure the model   for the training session.

## See Also

- [init(trainingData: [String : [URL]], parameters: MLImageClassifier.ModelParameters) throws](mlimageclassifier/init(trainingdata:parameters:)-7j4w6.md)
  Creates an image classifier with a training dataset represented by a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/init(trainingdata:parameters:)-4r6hr)*