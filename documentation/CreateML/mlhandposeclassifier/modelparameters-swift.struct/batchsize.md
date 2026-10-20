# batchSize

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

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

### Accessing hand pose training parameters
- [var maximumIterations: Int](./maximumiterations.md)
  The largest number of training iterations you allow the training session to use.
- [var algorithm: MLHandPoseClassifier.ModelParameters.ModelAlgorithmType](./algorithm.md)
  The algorithm the training session uses to create the hand pose classifier.
- [var augmentationOptions: MLHandPoseClassifier.ImageAugmentationOptions](./augmentationoptions.md)
  The variations the training session uses to add more variety to its training dataset.
- [var validation: MLHandPoseClassifier.ModelParameters.ValidationData](./validation.md)
  A dataset the hand pose classifier task uses to evaluate the model that’s distinct from the training dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct/batchsize)*