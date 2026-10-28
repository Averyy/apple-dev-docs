# resume(_:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

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
static func resume(_ session: MLTrainingSession<MLRandomForestRegressor>) throws -> MLJob<MLRandomForestRegressor>
```

## Return Value

A `MLJob` that can be used to observe training progress.

## Discussion

If there are no resumable checkpoints training starts over from the beginning.

## Parameters

- `session`: Loaded or new training session.

## See Also

### Training a random forest regressor
- [static train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](./train%28trainingdata,targetcolumn,featurecolumns,parameters,sessionparameters%29.md)
  Trains a random forest regressor.
- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](./maketrainingsession%28trainingdata,targetcolumn,featurecolumns,parameters,sessionparameters%29.md)
  Creates or restores a training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestRegressor>](./restoretrainingsession%28sessionparameters%29.md)
  Restores an existing training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestregressor/resume(_:))*