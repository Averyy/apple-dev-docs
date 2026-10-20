# pause(atTime:)

**Framework**: Core Haptics  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Pauses the haptic player during playback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func pause(atTime time: TimeInterval) throws
```

```objc
- (BOOL) pauseAtTime:(NSTimeInterval) time error:(NSError **) outError;
```

## Parameters

- `time`: The time in the haptic pattern at which to pause playback.

## See Also

### Controlling Playback
- [func resume(atTime: TimeInterval) throws](./resume%28attime%29.md)
  Resumes playing a paused haptic.
- [func seek(toOffset: TimeInterval) throws](./seek%28tooffset%29.md)
  Jumps to the specified offset time in playing the haptic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticadvancedpatternplayer/pause(attime:))*