# init(trainingData:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates a hand pose classifier by starting a synchronous training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
init(trainingData: MLHandPoseClassifier.DataSource, parameters: MLHandPoseClassifier.ModelParameters = ModelParameters()) throws
```

## Parameters

- `trainingData`: An [`MLHandPoseClassifier.DataSource`](mlhandposeclassifier/datasource.md) instance.
- `parameters`: An [`MLHandPoseClassifier.ModelParameters`](mlhandposeclassifier/modelparameters-swift.struct.md) instance you use to configure the model for the training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/init(trainingdata:parameters:))*