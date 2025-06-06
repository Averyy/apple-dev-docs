# SCStreamError

**Framework**: ScreenCaptureKit  
**Kind**: struct

An instance representing a ScreenCaptureKit framework error.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
struct SCStreamError
```

#### Overview

> ❗ **Important**:  When a user cancels a stream, the system calls an observer’s [`stream(_:didStopWithError:)`](scstreamdelegate/stream(_:didstopwitherror:).md) method with [`SCStreamError.Code.userStopped`](scstreamerror/code/userstopped.md). Rather than treating this event as an error, handle it as an intentional user request.

 When a user cancels a stream, the system calls an observer’s [`stream(_:didStopWithError:)`](scstreamdelegate/stream(_:didstopwitherror:).md) method with [`SCStreamError.Code.userStopped`](scstreamerror/code/userstopped.md). Rather than treating this event as an error, handle it as an intentional user request.

## Topics

### Error inspection
- [Error Constants](error-constants.md)
  Error code constants for framework operations.
- [SCStreamError.Code](scstreamerror/code.md)
  Codes for user cancellation events and errors that can occur in ScreenCaptureKit.
- [static var errorDomain: String](scstreamerror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let SCStreamErrorDomain: String](scstreamerrordomain.md)
  A string representation of the error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamerror)*