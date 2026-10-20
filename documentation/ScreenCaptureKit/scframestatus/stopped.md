# SCFrameStatus.stopped

**Framework**: ScreenCaptureKit  
**Kind**: case  
**Role**: Case

A status that indicates the frame is in a stopped state.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case stopped
```

```c
SCFrameStatusStopped
```

## See Also

### Status values
- [SCFrameStatus.complete](./complete.md)
  A status that indicates the system successfully generated a new frame.
- [SCFrameStatus.idle](./idle.md)
  A status that indicates the system didn’t generate a new frame because the display didn’t change.
- [SCFrameStatus.blank](./blank.md)
  A status that indicates the system didn’t generate a new frame because the display is blank.
- [SCFrameStatus.started](./started.md)
  A status that indicates the frame is the first one sent after the stream starts.
- [SCFrameStatus.suspended](./suspended.md)
  A status that indicates the system didn’t generate a new frame because you suspended updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scframestatus/stopped)*