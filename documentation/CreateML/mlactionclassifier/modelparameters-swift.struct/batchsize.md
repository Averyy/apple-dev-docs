# batchSize

**Framework**: Create ML  
**Kind**: property

The number of videos the training session uses for each of its training iterations.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var batchSize: Int
```

## See Also

- [var maximumIterations: Int](mlactionclassifier/modelparameters-swift.struct/maximumiterations.md)
  The largest number of training iterations the training session can use.
- [var targetFrameRate: Double](mlactionclassifier/modelparameters-swift.struct/targetframerate.md)
  The number of frames the training session uses per second of video to train an action classifier.
- [var predictionWindowSize: Int](mlactionclassifier/modelparameters-swift.struct/predictionwindowsize.md)
  The number of frames the training session uses to train an action classifier.
- [var algorithm: MLActionClassifier.ModelParameters.ModelAlgorithmType](mlactionclassifier/modelparameters-swift.struct/algorithm.md)
  The algorithm the training session uses to train the action classifier.
- [var augmentationOptions: MLActionClassifier.VideoAugmentationOptions](mlactionclassifier/modelparameters-swift.struct/augmentationoptions.md)
  The variations the training session uses to generate more variety in the training dataset.
- [var validation: MLActionClassifier.ModelParameters.ValidationData](mlactionclassifier/modelparameters-swift.struct/validation.md)
  The action classifier’s validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/modelparameters-swift.struct/batchsize)*