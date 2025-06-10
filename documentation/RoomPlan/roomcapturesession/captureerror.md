# RoomCaptureSession.CaptureError

**Framework**: RoomPlan  
**Kind**: enum

Errors that can occur during a room-capture session.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
enum CaptureError
```

#### Overview

The `error` argument of a room-capture session delgate’s  [`captureSession(_:didEndWith:error:)`](roomcapturesessiondelegate/capturesession(_:didendwith:error:).md) function is of this type.

## Topics

### Identifying the error cause
- [RoomCaptureSession.CaptureError.deviceNotSupported](roomcapturesession/captureerror/devicenotsupported.md)
  An error that indicates that the framework doesn’t support the user’s device.
- [RoomCaptureSession.CaptureError.deviceTooHot](roomcapturesession/captureerror/devicetoohot.md)
  An error that indicates when the device thermal metrics surpass the framework’s limitations.
- [RoomCaptureSession.CaptureError.exceedSceneSizeLimit](roomcapturesession/captureerror/exceedscenesizelimit.md)
  An error that indicates when the scene size grows past the framework’s limitations.
- [RoomCaptureSession.CaptureError.invalidARConfiguration](roomcapturesession/captureerror/invalidarconfiguration.md)
  An error that indicates when the ARKit session runs an unsupported configuration.
- [RoomCaptureSession.CaptureError.worldTrackingFailure](roomcapturesession/captureerror/worldtrackingfailure.md)
  An error that indicates an issue with the underlying ARKit session.
- [RoomCaptureSession.CaptureError.internalError](roomcapturesession/captureerror/internalerror.md)
  An error that indicates when the framework encounters an unexpected error case.
### Inspecting error information
- [var errorDescription: String?](roomcapturesession/captureerror/errordescription.md)
  A human-readable explanation for the error.
- [var failureReason: String?](roomcapturesession/captureerror/failurereason.md)
  A localized message describing the reason for the failure.
- [var helpAnchor: String?](roomcapturesession/captureerror/helpanchor.md)
  A localized message providing “help” text if the user requests help.
- [var localizedDescription: String](roomcapturesession/captureerror/localizeddescription.md)
  Retrieve the localized description for this error.
- [var recoverySuggestion: String?](roomcapturesession/captureerror/recoverysuggestion.md)
  A localized message describing how one might recover from the failure.
### Comparing errors
- [static func == (RoomCaptureSession.CaptureError, RoomCaptureSession.CaptureError) -> Bool](roomcapturesession/captureerror/==(_:_:).md)
  Determines whether two errors are equal.
- [static func != (Self, Self) -> Bool](roomcapturesession/captureerror/!=(_:_:).md)
  Determines whether two errors aren’t equal.
- [var hashValue: Int](roomcapturesession/captureerror/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](roomcapturesession/captureerror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](roomcapturesession/captureerror/equatable-implementations.md)
- [Error Implementations](roomcapturesession/captureerror/error-implementations.md)
- [LocalizedError Implementations](roomcapturesession/captureerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var delegate: (any RoomCaptureSessionDelegate)?](roomcapturesession/delegate.md)
  An object that observes important events in the room-scanning process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/captureerror)*