# init(validation:batchSize:maximumIterations:augmentationOptions:algorithm:)

**Framework**: Create ML  
**Kind**: init

Creates a set of training session parameters for a hand pose classifier task.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
init(validation: MLHandPoseClassifier.ModelParameters.ValidationData = .split(strategy: .automatic), batchSize: Int = MLHandPoseClassifier.__Defaults.batchSize, maximumIterations: Int = MLHandPoseClassifier.__Defaults.maximumIterations, augmentationOptions: MLHandPoseClassifier.ImageAugmentationOptions = [], algorithm: MLHandPoseClassifier.ModelParameters.ModelAlgorithmType = .gcn)
```

#### Discussion

- validation: An [`MLHandPoseClassifier.ModelParameters.ValidationData`](mlhandposeclassifier/modelparameters-swift.struct/validationdata.md) instance.
- batchSize: The number of images the training session uses for each of its training iterations.
- maximumIterations: The largest number of training iterations the training session can use.
- augmentationOptions: The variations the training session uses to add more variety to its training dataset.
- algorithm: The algorithm the training session uses to train the hand pose classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct/init(validation:batchsize:maximumiterations:augmentationoptions:algorithm:))*