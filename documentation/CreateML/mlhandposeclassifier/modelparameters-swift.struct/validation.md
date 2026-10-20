# validation

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

A dataset the hand pose classifier task uses to evaluate the model that’s distinct from the training dataset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var validation: MLHandPoseClassifier.ModelParameters.ValidationData
```

#### Discussion

The task produces [`validationMetrics`](../validationmetrics.md) by evaluating the model with the [`validation`](./validation.md) dataset.

## See Also

### Accessing hand pose training parameters
- [var maximumIterations: Int](./maximumiterations.md)
  The largest number of training iterations you allow the training session to use.
- [var batchSize: Int](./batchsize.md)
  The number of images the model training session uses for each training iteration.
- [var algorithm: MLHandPoseClassifier.ModelParameters.ModelAlgorithmType](./algorithm.md)
  The algorithm the training session uses to create the hand pose classifier.
- [var augmentationOptions: MLHandPoseClassifier.ImageAugmentationOptions](./augmentationoptions.md)
  The variations the training session uses to add more variety to its training dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct/validation)*