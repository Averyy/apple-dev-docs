# soundClassification

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The highest-ranking classifications in the time range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var soundClassification: SNClassificationResult? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) SNClassificationResult * soundClassification;
```

## See Also

### Getting speech metrics and analytics
- [var audioLevel: SRAudioLevel?](./audiolevel.md)
  The audio level of the speech.
- [class SRAudioLevel](../sraudiolevel.md)
  An object that represents the audio level for a range of speech.
- [var speechRecognition: SFSpeechRecognitionResult?](./speechrecognition.md)
  The partial or final results of the speech recognition request.
- [var speechExpression: SRSpeechExpression?](./speechexpression.md)
  The metrics and voice analytics for the range of speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srspeechmetrics/soundclassification)*