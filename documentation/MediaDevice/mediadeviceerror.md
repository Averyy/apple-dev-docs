# MediaDeviceError

**Framework**: Media Device  
**Kind**: struct

An error returned by MediaDeviceExtension operations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct MediaDeviceError
```

## Topics

### Initializers
- [init(MediaDeviceError.Code)](mediadeviceerror/init(_:).md)
  Creates an error with the specified error code.
### Instance Properties
- [let code: MediaDeviceError.Code](mediadeviceerror/code-swift.property.md)
  The error code for this error.
- [var errorDescription: String?](mediadeviceerror/errordescription.md)
  A localized description of the error.
- [var failureReason: String?](mediadeviceerror/failurereason.md)
  A localized explanation of the reason for the error.
- [var helpAnchor: String?](mediadeviceerror/helpanchor.md)
  A localized help anchor for the error.
- [var recoverySuggestion: String?](mediadeviceerror/recoverysuggestion.md)
  A localized suggestion for how to recover from the error.
### Enumerations
- [MediaDeviceError.Code](mediadeviceerror/code-swift.enum.md)
  Error codes for media device operations.

## Relationships

### Conforms To
- [Error](../swift/error.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class MediaOutputSession](mediaoutputsession.md)
  Represents a media output session for playing content on a remote device.
- [class MediaDeviceRoutingManager](mediadeviceroutingmanager.md)
  An object used by a [`MediaDeviceExtension`](mediadeviceextension.md) to report device discovery, state changes, and playback events back to the system.
- [protocol RealtimeSampleHandling](realtimesamplehandling.md)
  A protocol that extends a media device extension to support realtime sample delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceerror)*