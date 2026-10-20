# resume(atTime:)

**Framework**: Core Haptics  
**Kind**: method  
**Required**: Yes

Resumes playing a paused haptic.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func resume(atTime time: TimeInterval) throws
```

## Parameters

- `time`: The time in the haptic pattern at which to resume playback.

## See Also

- [func pause(atTime: TimeInterval) throws](chhapticadvancedpatternplayer/pause(attime:).md)
  Pauses the haptic player during playback.
- [func seek(toOffset: TimeInterval) throws](chhapticadvancedpatternplayer/seek(tooffset:).md)
  Jumps to the specified offset time in playing the haptic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticadvancedpatternplayer/resume(attime:))*