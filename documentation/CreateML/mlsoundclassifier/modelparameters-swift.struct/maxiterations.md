# maxIterations

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The largest number of iterations the training session can use.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var maxIterations: Int
```

## See Also

### Accessing the training parameters
- [var validation: MLSoundClassifier.ModelParameters.ValidationData](./validation.md)
  The sound classifier’s validation dataset.
- [var overlapFactor: Double](./overlapfactor.md)
  The proportion of overlap that the training session uses to analyze two consecutive windows in the audio data.
- [var algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType](./algorithm.md)
  The algorithm the training session uses to train the sound classifier.
- [var featureExtractionTimeWindowSize: TimeInterval](./featureextractiontimewindowsize.md)
  A time duration, in seconds, the training session uses for each audio sample it reads from an audio file in a dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/maxiterations)*