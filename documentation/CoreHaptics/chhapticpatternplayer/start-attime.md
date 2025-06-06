# start(atTime:)

**Framework**: Core Haptics  
**Kind**: method  
**Required**: Yes

Starts playing the pattern at the specified time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func start(atTime time: TimeInterval) throws
```

## Mentions

- [Playing a single-tap haptic pattern](playing-a-single-tap-haptic-pattern.md)

#### Discussion

If `time` is `0` or any value less than the haptic engine’s [`currentTime`](chhapticengine/currenttime.md), the pattern starts playing immediately. If you call this method on a player that’s already playing, it restarts itself at the beginning of the pattern.

## Parameters

- `time`: The time from which to start playing the pattern.

## See Also

- [func stop(atTime: TimeInterval) throws](chhapticpatternplayer/stop(attime:).md)
  Stops playing the pattern at the specified time.
- [func cancel() throws](chhapticpatternplayer/cancel.md)
  Stops the pattern player immediately and returns the specified error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpatternplayer/start(attime:))*