# speechStartTimestamp

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

The start timestamp of speech in the audio.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var speechStartTimestamp: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval speechStartTimestamp;
```

## See Also

### Getting audio timing information
- [var averagePauseDuration: TimeInterval](./averagepauseduration.md)
  The average pause duration between words, measured in seconds.
- [var speakingRate: Double](./speakingrate.md)
  The number of words spoken per minute.
- [var speechDuration: TimeInterval](./speechduration.md)
  The duration in seconds of speech in the audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitionmetadata/speechstarttimestamp)*