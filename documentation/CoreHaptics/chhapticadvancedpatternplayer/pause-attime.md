# pause(atTime:)

**Framework**: Core Haptics  
**Kind**: method  
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

## Parameters

- `time`: The time in the haptic pattern at which to pause playback.

## See Also

- [func resume(atTime: TimeInterval) throws](chhapticadvancedpatternplayer/resume(attime:).md)
  Resumes playing a paused haptic.
- [func seek(toOffset: TimeInterval) throws](chhapticadvancedpatternplayer/seek(tooffset:).md)
  Jumps to the specified offset time in playing the haptic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticadvancedpatternplayer/pause(attime:))*