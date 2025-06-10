# currentTime

**Framework**: Core Haptics  
**Kind**: property

The absolute time, in seconds, to use for scheduling haptic and audio events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var currentTime: TimeInterval { get }
```

#### Discussion

This time applies to all haptic and audio events sent to and managed by the Core Haptics engine. Use the current time as a way to determine or track the start times of haptic and audio events, created as [`CHHapticEvent`](chhapticevent.md) objects. It corresponds to the [`relativeTime`](chhapticevent/relativetime.md) and [`duration`](chhapticevent/duration.md) properties of haptic events.

> **Note**:  The Core Haptics engine time doesn’t correlate to time used in media playback classes from other frameworks, such as [`AVAudioPlayer`](https://developer.apple.com/documentation/AVFAudio/AVAudioPlayer).

## See Also

- [var CHHapticTimeImmediate: TimeInterval](chhaptictimeimmediate.md)
  A time constant used to schedule a command immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/currenttime)*