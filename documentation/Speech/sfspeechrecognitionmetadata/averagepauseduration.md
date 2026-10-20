# averagePauseDuration

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

The average pause duration between words, measured in seconds.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var averagePauseDuration: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval averagePauseDuration;
```

## See Also

### Getting audio timing information
- [var speakingRate: Double](./speakingrate.md)
  The number of words spoken per minute.
- [var speechDuration: TimeInterval](./speechduration.md)
  The duration in seconds of speech in the audio.
- [var speechStartTimestamp: TimeInterval](./speechstarttimestamp.md)
  The start timestamp of speech in the audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitionmetadata/averagepauseduration)*