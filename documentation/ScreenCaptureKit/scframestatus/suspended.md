# SCFrameStatus.suspended

**Framework**: ScreenCaptureKit  
**Kind**: case  
**Role**: Case

A status that indicates the system didn’t generate a new frame because you suspended updates.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case suspended
```

```c
SCFrameStatusSuspended
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
- [SCFrameStatus.stopped](./stopped.md)
  A status that indicates the frame is in a stopped state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scframestatus/suspended)*