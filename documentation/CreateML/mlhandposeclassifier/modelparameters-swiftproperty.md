# modelParameters

**Framework**: Create ML  
**Kind**: property

The hand pose model’s configuration parameters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
let modelParameters: MLHandPoseClassifier.ModelParameters
```

#### Discussion

The property reflects the model parameters you provide to one of these methods that train a hand pose classifier:

#### Doccomapplecreatemldocumentationcreatemlmlhandposeclassifiertraintrainingdataparameterssessionparameters

[`makeTrainingSession(trainingData:parameters:sessionParameters:)`](mlhandposeclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)

- [`init(trainingData:parameters:)`](mlhandposeclassifier/init(trainingdata:parameters:).md)

## See Also

- [var model: MLModel](mlhandposeclassifier/model.md)
  The underlying Core ML model of the hand pose classifier stored in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.property)*