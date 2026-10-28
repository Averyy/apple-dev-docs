# restoreTrainingSession(sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

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
static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLinearRegressor>
```

## Return Value

A `MLTrainingSession` that can be used to resume training.

## Parameters

- `sessionParameters`: Training session parameters. The method requires the a valid [`sessionDirectory`](../mltrainingsessionparameters/sessiondirectory.md) parameter.

## See Also

### Creating a linear regressor asynchronously
- [static train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](./train%28trainingdata,targetcolumn,featurecolumns,parameters,sessionparameters%29.md)
  Trains a linear regressor.
- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](./maketrainingsession%28trainingdata,targetcolumn,featurecolumns,parameters,sessionparameters%29.md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLLinearRegressor>) throws -> MLJob<MLLinearRegressor>](./resume%28_%29.md)
  Resumes a training session from the last checkpoint if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllinearregressor/restoretrainingsession(sessionparameters:))*