# seek(toOffset:)

**Framework**: Core Haptics  
**Kind**: method  
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

## Parameters

- `offsetTime`: The time in the haptic pattern at which to seek playback.

## See Also

- [func pause(atTime: TimeInterval) throws](chhapticadvancedpatternplayer/pause(attime:).md)
  Pauses the haptic player during playback.
- [func resume(atTime: TimeInterval) throws](chhapticadvancedpatternplayer/resume(attime:).md)
  Resumes playing a paused haptic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticadvancedpatternplayer/seek(tooffset:))*