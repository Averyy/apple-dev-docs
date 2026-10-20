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

## See Also

### Creating and training a text classifier
- [init(trainingData:textColumn:labelColumn:parameters:)](./init%28trainingdata,textcolumn,labelcolumn,parameters%29.md)
  Creates a text classifier.
- [MLTextClassifier.DataSource](./datasource.md)
  A data source for a text classifier.
- [MLTextClassifier.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.
- [let modelParameters: MLTextClassifier.ModelParameters](./modelparameters-swift.property.md)
  The configuration parameters that the text classifier used for training during initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/init(trainingdata:parameters:))*