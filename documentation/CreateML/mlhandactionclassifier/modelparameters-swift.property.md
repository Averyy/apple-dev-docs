# modelParameters

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The hand action model’s configuration parameters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
let modelParameters: MLHandActionClassifier.ModelParameters
```

## Discussion

The property reflects the model parameters you provide to one of these methods that train a hand action classifier:

## ``doc://com.apple.createml/documentation/CreateML/MLHandActionClassifier/train(trainingData:parameters:sessionParameters:)``

[`makeTrainingSession(trainingData:parameters:sessionParameters:)`](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md)

- [`init(trainingData:parameters:)`](./init%28trainingdata,parameters%29.md)

## See Also

### Inspecting a hand action classifier model
- [var model: MLModel](./model.md)
  The underlying Core ML model of the hand action classifier stored in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/modelparameters-swift.property)*