# algorithm

**Framework**: Create ML  
**Kind**: property

The algorithm the training session uses to train the sound classifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType { get set }
```

## See Also

- [var validation: MLSoundClassifier.ModelParameters.ValidationData](mlsoundclassifier/modelparameters-swift.struct/validation.md)
  The sound classifier’s validation dataset.
- [var maxIterations: Int](mlsoundclassifier/modelparameters-swift.struct/maxiterations.md)
  The largest number of iterations the training session can use.
- [var overlapFactor: Double](mlsoundclassifier/modelparameters-swift.struct/overlapfactor.md)
  The proportion of overlap that the training session uses to analyze two consecutive windows in the audio data.
- [var featureExtractionTimeWindowSize: TimeInterval](mlsoundclassifier/modelparameters-swift.struct/featureextractiontimewindowsize.md)
  A time duration, in seconds, the training session uses for each audio sample it reads from an audio file in a dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/algorithm)*