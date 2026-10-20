# seek(toOffset:)

**Framework**: Core Haptics  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Jumps to the specified offset time in playing the haptic.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func seek(toOffset offsetTime: TimeInterval) throws
```

```objc
- (BOOL) seekToOffset:(NSTimeInterval) offsetTime error:(NSError **) outError;
```

## Parameters

- `offsetTime`: The time in the haptic pattern at which to seek playback.

## See Also

### Controlling Playback
- [func pause(atTime: TimeInterval) throws](./pause%28attime%29.md)
  Pauses the haptic player during playback.
- [func resume(atTime: TimeInterval) throws](./resume%28attime%29.md)
  Resumes playing a paused haptic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticadvancedpatternplayer/seek(tooffset:))*