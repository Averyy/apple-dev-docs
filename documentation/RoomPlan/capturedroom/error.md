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
### Comparing errors
- [static func == (CapturedRoom.Error, CapturedRoom.Error) -> Bool](capturedroom/error/==(_:_:).md)
  Determines whether two captured room errors are equal.
- [static func != (Self, Self) -> Bool](capturedroom/error/!=(_:_:).md)
  Determines whether two captured room errors aren’t equal.
- [func hash(into: inout Hasher)](capturedroom/error/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](capturedroom/error/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](capturedroom/error/equatable-implementations.md)
- [Error Implementations](capturedroom/error/error-implementations.md)
- [LocalizedError Implementations](capturedroom/error/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/error)*