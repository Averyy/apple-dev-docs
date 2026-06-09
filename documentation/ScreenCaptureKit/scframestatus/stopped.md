# SCFrameStatus.stopped

**Framework**: ScreenCaptureKit  
**Kind**: case

A status that indicates the frame is in a stopped state.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case stopped
```

## See Also

- [SCFrameStatus.complete](scframestatus/complete.md)
  A status that indicates the system successfully generated a new frame.
- [SCFrameStatus.idle](scframestatus/idle.md)
  A status that indicates the system didn’t generate a new frame because the display didn’t change.
- [SCFrameStatus.blank](scframestatus/blank.md)
  A status that indicates the system didn’t generate a new frame because the display is blank.
- [SCFrameStatus.started](scframestatus/started.md)
  A status that indicates the frame is the first one sent after the stream starts.
- [SCFrameStatus.suspended](scframestatus/suspended.md)
  A status that indicates the system didn’t generate a new frame because you suspended updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scframestatus/stopped)*