# stop(atTime:)

**Framework**: Core Haptics  
**Kind**: method  
**Required**: Yes

Stops playing the pattern at the specified time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func stop(atTime time: TimeInterval) throws
```

#### Discussion

If `time` is `0` or any value less than the haptic engine’s [`currentTime`](chhapticengine/currenttime.md), the pattern stops playing immediately.

## Parameters

- `time`: The time at which to stop playing the pattern.

## See Also

- [func start(atTime: TimeInterval) throws](chhapticpatternplayer/start(attime:).md)
  Starts playing the pattern at the specified time.
- [func cancel() throws](chhapticpatternplayer/cancel.md)
  Stops the pattern player immediately and returns the specified error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpatternplayer/stop(attime:))*