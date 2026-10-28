# init(trainingData:parameters:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a text classifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(trainingData: MLTextClassifier.DataSource, parameters: MLTextClassifier.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

**Other overloads**:

```swift
init(trainingData: [String : [String]], parameters: MLTextClassifier.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

## Parameters

- `trainingData`: A data source specifying the training data.
- `parameters`: Model training parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/init(trainingdata:parameters:)-8n8vs)*