# CapturedRoom.Error

**Framework**: RoomPlan  
**Kind**: enum  
**Role**: Enumeration

Errors that can occur during a captured room export.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum Error
```

#### Overview

The captured room ([`CapturedRoom`](../capturedroom.md)) function [`export(to:metadataURL:modelProvider:exportOptions:)`](./export%28to,metadataurl,modelprovider,exportoptions%29.md) can throw an error of this type.

## Topics

### Interpreting the error
- [CapturedRoom.Error.deviceNotSupported](./error/devicenotsupported.md)
  An error that indicates that the framework doesn’t support the user’s device.
- [CapturedRoom.Error.urlInvalidFileExtension](./error/urlinvalidfileextension.md)
  An error that indicates that the URL contains an unsupported file extension.
- [CapturedRoom.Error.urlInvalidFilePath](./error/urlinvalidfilepath.md)
  An error that indicates that the URL references an invalid file path.
- [CapturedRoom.Error.urlInvalidScheme](./error/urlinvalidscheme.md)
  An error that indicates that the URL prefix represents an unsupported scheme.
- [CapturedRoom.Error.urlMissingFileExtension](./error/urlmissingfileextension.md)
  An error that indicates that the URL lacks a necessary file extension.
### Inspecting error information
- [var errorDescription: String?](./error/errordescription.md)
  A human-readable explanation of the error.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/error)*