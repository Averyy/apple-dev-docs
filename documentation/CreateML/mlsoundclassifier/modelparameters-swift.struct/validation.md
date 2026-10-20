# validation

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The sound classifier’s validation dataset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var validation: MLSoundClassifier.ModelParameters.ValidationData
```

## See Also

### Accessing the training parameters
- [var maxIterations: Int](./maxiterations.md)
  The largest number of iterations the training session can use.
- [var overlapFactor: Double](./overlapfactor.md)
  The proportion of overlap that the training session uses to analyze two consecutive windows in the audio data.
- [var algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType](./algorithm.md)
  The algorithm the training session uses to train the sound classifier.
- [var featureExtractionTimeWindowSize: TimeInterval](./featureextractiontimewindowsize.md)
  A time duration, in seconds, the training session uses for each audio sample it reads from an audio file in a dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validation)*