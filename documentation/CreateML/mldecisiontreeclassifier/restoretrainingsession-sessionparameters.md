# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Restores an existing training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeClassifier>
```

#### Return Value

A `MLTrainingSession` that can be used to resume training.

## Parameters

- `sessionParameters`: Training session parameters. The   parameter is required.

## See Also

- [init(trainingData:targetColumn:featureColumns:parameters:)](mldecisiontreeclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:).md)
  Creates a decision tree classifier.
- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mldecisiontreeclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLDecisionTreeClassifier>) throws -> MLJob<MLDecisionTreeClassifier>](mldecisiontreeclassifier/resume(_:).md)
  Resumes a training session from the last checkpoint if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeclassifier/restoretrainingsession(sessionparameters:))*