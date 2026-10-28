# stop(atTime:)

**Framework**: Core Haptics  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (BOOL) stopAtTime:(NSTimeInterval) time error:(NSError **) outError;
```

## Discussion

If `time` is `0` or any value less than the haptic engine’s [`currentTime`](../chhapticengine/currenttime.md), the pattern stops playing immediately.

## Parameters

- `time`: The time at which to stop playing the pattern.

## See Also

### Starting and Stopping Playback
- [func start(atTime: TimeInterval) throws](./start%28attime%29.md)
  Starts playing the pattern at the specified time.
- [func cancel() throws](./cancel%28%29.md)
  Stops the pattern player immediately and returns the specified error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpatternplayer/stop(attime:))*