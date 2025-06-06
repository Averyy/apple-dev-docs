# modelParameters

**Framework**: Create ML  
**Kind**: property

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

#### Discussion

The property reflects the model parameters you provide to one of these methods that train a hand action classifier:

#### Doccomapplecreatemldocumentationcreatemlmlhandactionclassifiertraintrainingdataparameterssessionparameters

[`makeTrainingSession(trainingData:parameters:sessionParameters:)`](mlhandactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:).md)

- [`init(trainingData:parameters:)`](mlhandactionclassifier/init(trainingdata:parameters:).md)

## See Also

- [var model: MLModel](mlhandactionclassifier/model.md)
  The underlying Core ML model of the hand action classifier stored in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/modelparameters-swift.property)*