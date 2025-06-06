# SCFrameStatus

**Framework**: ScreenCaptureKit  
**Kind**: enum

Status values for a frame from a stream.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
enum SCFrameStatus
```

#### Overview

You create a frame status by initializing it with the value you retrieve for the [`status`](scstreamframeinfo/status.md) from the sample buffer’s attachments dictionary.

```swift
if let statusRawValue = attachments[SCStreamFrameInfo.status] as? Int {
    // Create status value.
    let status = SCFrameStatus(rawValue: statusRawValue)
    ...
}
```

## Topics

### Status values
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
- [SCFrameStatus.stopped](scframestatus/stopped.md)
  A status that indicates the frame is in a stopped state.
### Initializers
- [init?(rawValue: Int)](scframestatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol SCStreamOutput](scstreamoutput.md)
  A delegate protocol your app implements to receive capture stream output events.
- [enum SCStreamOutputType](scstreamoutputtype.md)
  Constants that represent output types for a stream frame.
- [struct SCStreamFrameInfo](scstreamframeinfo.md)
  An instance that defines metadata keys for a stream frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scframestatus)*