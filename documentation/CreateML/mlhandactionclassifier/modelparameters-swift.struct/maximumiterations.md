# maximumIterations

**Framework**: Create ML  
**Kind**: property

The largest number of training iterations you allow the training session to use.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var maximumIterations: Int
```

## See Also

- [var batchSize: Int](mlhandactionclassifier/modelparameters-swift.struct/batchsize.md)
  The number of videos the model training session uses for each training iteration.
- [var targetFrameRate: Double](mlhandactionclassifier/modelparameters-swift.struct/targetframerate.md)
  The number of video frames per second the hand action classifier model expects as its input at runtime.
- [var predictionWindowSize: Int](mlhandactionclassifier/modelparameters-swift.struct/predictionwindowsize.md)
  The number of video frames the model training session uses to train a hand action classifier.
- [var algorithm: MLHandActionClassifier.ModelParameters.ModelAlgorithmType](mlhandactionclassifier/modelparameters-swift.struct/algorithm.md)
  The algorithm the training session uses to create the hand action classifier.
- [var augmentationOptions: MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/modelparameters-swift.struct/augmentationoptions.md)
  The variations the training session uses to add more variety to its training dataset.
- [var validation: MLHandActionClassifier.ModelParameters.ValidationData](mlhandactionclassifier/modelparameters-swift.struct/validation.md)
  A dataset the hand action classifier task uses to evaluate the model that’s distinct from the training dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/modelparameters-swift.struct/maximumiterations)*