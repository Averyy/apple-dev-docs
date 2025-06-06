# overlapFactor

**Framework**: Create ML  
**Kind**: property

The proportion of overlap that the training session uses to analyze two consecutive windows in the audio data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var overlapFactor: Double
```

#### Discussion

The overlap factor — which must be in the range `[0.0, 1.0)` — affects how much audio data the training session analyzes in each file. Sessions with smaller overlap factors read fewer audio data samples and finish in less time but may compromise the model’s prediction accuracy. Sessions with larger overlap factors read more audio samples for each file, which increases the session’s training data and processing time. The additional training data can improve a sound classifier’s accuracy; however, it may only be a modest improvement that isn’t worth the extra processing time.

The training session uses the expression `(featureExtractionTimeWindowSize * (1.0 - overlapFactor))` to determine the how much to  (advance) in time between samples.

| Window size | Overlap factor | Step time |
| --- | --- | --- |
| `1.0` | `0.0` | `1.0` |
| `2.0` | `0.0` | `2.0` |
| `5.0` | `0.0` | `5.0` |
| `1.0` | `0.5` | `0.5` |
| `2.0` | `0.5` | `1.0` |
| `5.0` | `0.5` | `2.5` |
| `1.0` | `0.75` | `0.25` |
| `2.0` | `0.75` | `0.5` |
| `5.0` | `0.75` | `1.25` |

For example, a session that’s analyzing a 5-second audio file with a window size of `1.0` and an overlap factor of `0.0` samples the audio five times. The time offsets for those samples are: `0.0`, `1.0`, `2.0`, `3.0`, and `4.0`.

Another session with a window size of `1.0` and an overlap factor of `0.5` samples the same audio file 10 times at half-second intervals. Unlike the first session, this session samples each portion of audio data twice, except for the first and final half-second.

A third session with a window size of `1.0` and an overlap factor of `0.75` samples the same 5-second audio file 20 times at quarter-second intervals. This third session samples most of the audio portions four times; the session samples the intervals near the ends one, two, or three times.

## See Also

- [var validation: MLSoundClassifier.ModelParameters.ValidationData](mlsoundclassifier/modelparameters-swift.struct/validation.md)
  The sound classifier’s validation dataset.
- [var maxIterations: Int](mlsoundclassifier/modelparameters-swift.struct/maxiterations.md)
  The largest number of iterations the training session can use.
- [var algorithm: MLSoundClassifier.ModelParameters.ModelAlgorithmType](mlsoundclassifier/modelparameters-swift.struct/algorithm.md)
  The algorithm the training session uses to train the sound classifier.
- [var featureExtractionTimeWindowSize: TimeInterval](mlsoundclassifier/modelparameters-swift.struct/featureextractiontimewindowsize.md)
  A time duration, in seconds, the training session uses for each audio sample it reads from an audio file in a dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/overlapfactor)*