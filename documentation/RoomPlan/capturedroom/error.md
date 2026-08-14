# CapturedRoom.Error

**Framework**: RoomPlan  
**Kind**: enum

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

The captured room ([`CapturedRoom`](capturedroom.md)) function [`export(to:metadataURL:modelProvider:exportOptions:)`](capturedroom/export(to:metadataurl:modelprovider:exportoptions:).md) can throw an error of this type.

## Topics

### Interpreting the error
- [CapturedRoom.Error.deviceNotSupported](capturedroom/error/devicenotsupported.md)
  An error that indicates that the framework doesn’t support the user’s device.
- [CapturedRoom.Error.urlInvalidFileExtension](capturedroom/error/urlinvalidfileextension.md)
  An error that indicates that the URL contains an unsupported file extension.
- [CapturedRoom.Error.urlInvalidFilePath](capturedroom/error/urlinvalidfilepath.md)
  An error that indicates that the URL references an invalid file path.
- [CapturedRoom.Error.urlInvalidScheme](capturedroom/error/urlinvalidscheme.md)
  An error that indicates that the URL prefix represents an unsupported scheme.
- [CapturedRoom.Error.urlMissingFileExtension](capturedroom/error/urlmissingfileextension.md)
  An error that indicates that the URL lacks a necessary file extension.
### Inspecting error information
- [var errorDescription: String?](capturedroom/error/errordescription.md)
  A human-readable explanation of the error.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/error)*