# resume(_:)

**Framework**: Create ML  
**Kind**: method

Resumes a training session from the last checkpoint if available.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func resume(_ session: MLTrainingSession<MLDecisionTreeRegressor>) throws -> MLJob<MLDecisionTreeRegressor>
```

#### Return Value

A `MLJob` that can be used to observe training progress.

#### Discussion

If there are no resumable checkpoints training starts over from the beginning.

## Parameters

- `session`: Loaded or new training session.

## See Also

- [static train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mldecisiontreeregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Trains a decision tree regressor.
- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mldecisiontreeregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Creates or restores a training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeRegressor>](mldecisiontreeregressor/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeregressor/resume(_:))*