# init(validation:batchSize:maximumIterations:predictionWindowSize:augmentationOptions:algorithm:targetFrameRate:)

**Framework**: Create ML  
**Kind**: init

Creates a new set of training parameters for an action classifier with the validation dataset.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(validation: MLActionClassifier.ModelParameters.ValidationData = .split(strategy: .automatic), batchSize: Int = MLActionClassifier.__Defaults.batchSize, maximumIterations: Int = MLActionClassifier.__Defaults.maximumIterations, predictionWindowSize: Int = MLActionClassifier.__Defaults.predictionWindowSize, augmentationOptions: MLActionClassifier.VideoAugmentationOptions = [.horizontalFlip], algorithm: MLActionClassifier.ModelParameters.ModelAlgorithmType = .stgcn, targetFrameRate: Double = MLActionClassifier.__Defaults.targetFrameRate)
```

#### Discussion

- validation: A validation dataset represented by an [`MLActionClassifier.ModelParameters.ValidationData`](mlactionclassifier/modelparameters-swift.struct/validationdata.md) instance.
- batchSize: The number of videos the training session uses for each of its training iterations.
- maximumIterations: The largest number of training iterations the training session can use.
- predictionWindowSize: The number of frames the training session uses to train an action classifier. For example, set to 60 to capture actions that take 2 seconds from videos that have a frame rate of 30 frames per second.
- augmentationOptions: The variations the training session uses to generate more variety in the training dataset.
- algorithm: The algorithm the training session uses to train the action classifier.
- targetFrameRate: The number of frames the training session uses per second of video to train an action classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/modelparameters-swift.struct/init(validation:batchsize:maximumiterations:predictionwindowsize:augmentationoptions:algorithm:targetframerate:))*