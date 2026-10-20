# SCStreamError

**Framework**: ScreenCaptureKit  
**Kind**: struct  
**Role**: Structure

An instance representing a ScreenCaptureKit framework error.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct SCStreamError
```

#### Overview

> ❗ **Important**:  When a user cancels a stream, the system calls an observer’s [`stream(_:didStopWithError:)`](./scstreamdelegate/stream%28_,didstopwitherror%29.md) method with [`SCStreamError.Code.userStopped`](./scstreamerror/code/userstopped.md). Rather than treating this event as an error, handle it as an intentional user request.

## Topics

### Error inspection
- [Error Constants](./error-constants.md)
  Error code constants for framework operations.
- [SCStreamError.Code](./scstreamerror/code.md)
  Codes for user cancellation events and errors that can occur in ScreenCaptureKit.
- [static var errorDomain: String](./scstreamerror/errordomain.md)
### Type Properties
- [static var insufficientStorage: SCStreamError.Code](./scstreamerror/insufficientstorage.md)
- [static var missingBackgroundMode: SCStreamError.Code](./scstreamerror/missingbackgroundmode.md)
- [static var notSupported: SCStreamError.Code](./scstreamerror/notsupported.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/customnserror.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Stream errors (Swift)
- [let SCStreamErrorDomain: String](./scstreamerrordomain.md)
  A string representation of the error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamerror)*