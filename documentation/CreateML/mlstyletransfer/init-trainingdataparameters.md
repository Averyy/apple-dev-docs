# init(trainingData:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates a style transfer model with a training dataset represented by a data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(trainingData: MLStyleTransfer.DataSource, parameters: MLStyleTransfer.ModelParameters = .init()) throws
```

## Parameters

- `trainingData`: A style image and a content image, represented by a data source.
- `parameters`: An   instance you use to configure the model for the training   session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/init(trainingdata:parameters:))*