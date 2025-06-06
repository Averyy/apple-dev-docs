# batchSize

**Framework**: Create ML  
**Kind**: property

The number of images the model training session uses for each training iteration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var batchSize: Int
```

## See Also

- [var maximumIterations: Int](mlhandposeclassifier/modelparameters-swift.struct/maximumiterations.md)
  The largest number of training iterations you allow the training session to use.
- [var algorithm: MLHandPoseClassifier.ModelParameters.ModelAlgorithmType](mlhandposeclassifier/modelparameters-swift.struct/algorithm.md)
  The algorithm the training session uses to create the hand pose classifier.
- [var augmentationOptions: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/modelparameters-swift.struct/augmentationoptions.md)
  The variations the training session uses to add more variety to its training dataset.
- [var validation: MLHandPoseClassifier.ModelParameters.ValidationData](mlhandposeclassifier/modelparameters-swift.struct/validation.md)
  A dataset the hand pose classifier task uses to evaluate the model that’s distinct from the training dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct/batchsize)*