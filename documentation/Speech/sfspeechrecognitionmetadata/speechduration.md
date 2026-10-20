# speechDuration

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

The duration in seconds of speech in the audio.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var speechDuration: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval speechDuration;
```

## See Also

### Getting audio timing information
- [var averagePauseDuration: TimeInterval](./averagepauseduration.md)
  The average pause duration between words, measured in seconds.
- [var speakingRate: Double](./speakingrate.md)
  The number of words spoken per minute.
- [var speechStartTimestamp: TimeInterval](./speechstarttimestamp.md)
  The start timestamp of speech in the audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitionmetadata/speechduration)*