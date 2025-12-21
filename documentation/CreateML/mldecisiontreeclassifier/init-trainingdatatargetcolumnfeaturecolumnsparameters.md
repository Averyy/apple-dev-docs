# init(trainingData:targetColumn:featureColumns:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates a decision tree classifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil, parameters: MLDecisionTreeClassifier.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

## Parameters

- `trainingData`: The training data
- `targetColumn`: Name of the column containing the class labels
- `featureColumns`: Names of the columns containing feature values. If   all columns, other than the target   column, will be used as feature values.
- `parameters`: Model training parameters

## See Also

- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mldecisiontreeclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLDecisionTreeClassifier>) throws -> MLJob<MLDecisionTreeClassifier>](mldecisiontreeclassifier/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeClassifier>](mldecisiontreeclassifier/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:))*