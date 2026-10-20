# speakingRate

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

The number of words spoken per minute.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var speakingRate: Double { get }
```

```objc
@property (nonatomic, readonly) double speakingRate;
```

## See Also

### Getting audio timing information
- [var averagePauseDuration: TimeInterval](./averagepauseduration.md)
  The average pause duration between words, measured in seconds.
- [var speechDuration: TimeInterval](./speechduration.md)
  The duration in seconds of speech in the audio.
- [var speechStartTimestamp: TimeInterval](./speechstarttimestamp.md)
  The start timestamp of speech in the audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitionmetadata/speakingrate)*