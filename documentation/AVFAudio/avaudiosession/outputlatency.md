# outputLatency

**Framework**: AVFAudio  
**Kind**: property

The latency for audio output, in seconds.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var outputLatency: TimeInterval { get }
```

#### Discussion

Using an AirPlay-enabled device for your audio content can result in a 2-second delay. Check for this delay in game content.

## See Also

- [var inputLatency: TimeInterval](avaudiosession/inputlatency.md)
  The latency for audio input, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/outputlatency)*