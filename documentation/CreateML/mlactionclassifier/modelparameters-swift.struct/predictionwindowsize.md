# predictionWindowSize

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The number of frames the training session uses to train an action classifier.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var predictionWindowSize: Int
```

## See Also

### Accessing the training parameters
- [var maximumIterations: Int](./maximumiterations.md)
  The largest number of training iterations the training session can use.
- [var batchSize: Int](./batchsize.md)
  The number of videos the training session uses for each of its training iterations.
- [var targetFrameRate: Double](./targetframerate.md)
  The number of frames the training session uses per second of video to train an action classifier.
- [var algorithm: MLActionClassifier.ModelParameters.ModelAlgorithmType](./algorithm.md)
  The algorithm the training session uses to train the action classifier.
- [var augmentationOptions: MLActionClassifier.VideoAugmentationOptions](./augmentationoptions.md)
  The variations the training session uses to generate more variety in the training dataset.
- [var validation: MLActionClassifier.ModelParameters.ValidationData](./validation.md)
  The action classifier’s validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/modelparameters-swift.struct/predictionwindowsize)*