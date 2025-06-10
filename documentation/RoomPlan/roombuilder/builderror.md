# RoomBuilder.BuildError

**Framework**: RoomPlan  
**Kind**: enum

Errors that can occur during captured room-data processing.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
enum BuildError
```

#### Overview

The room builder ([`RoomBuilder`](roombuilder.md)) function [`capturedRoom(from:)`](roombuilder/capturedroom(from:).md) can throw an error of this type.

## Topics

### Interpreting the error cause
- [RoomBuilder.BuildError.insufficientInput](roombuilder/builderror/insufficientinput.md)
  An error that indicates the framework expects more captured room data.
- [RoomBuilder.BuildError.invalidInput](roombuilder/builderror/invalidinput.md)
  An error that indicates the framework encounters invalid captured room data.
- [RoomBuilder.BuildError.exceedSceneSizeLimit](roombuilder/builderror/exceedscenesizelimit.md)
  An error that indicates when the scene size grows past the framework’s limitations.
- [RoomBuilder.BuildError.internalError](roombuilder/builderror/internalerror.md)
  An error that indicates when the framework encounters an unexpected error case.
- [RoomBuilder.BuildError.deviceNotSupported](roombuilder/builderror/devicenotsupported.md)
  An error that indicates that the framework doesn’t support the user’s device.
### Inspecting error information
- [var errorDescription: String?](roombuilder/builderror/errordescription.md)
  A human-readable explanation of the error.
- [var recoverySuggestion: String?](roombuilder/builderror/recoverysuggestion.md)
  A localized message describing how one might recover from the failure.
- [var localizedDescription: String](roombuilder/builderror/localizeddescription.md)
  Retrieve the localized description for this error.
- [var helpAnchor: String?](roombuilder/builderror/helpanchor.md)
  A localized message providing “help” text if the user requests help.
- [var failureReason: String?](roombuilder/builderror/failurereason.md)
  A localized message describing the reason for the failure.
### Comparing build errors
- [static func == (RoomBuilder.BuildError, RoomBuilder.BuildError) -> Bool](roombuilder/builderror/==(_:_:).md)
  Determines whether two errors are equal.
- [static func != (Self, Self) -> Bool](roombuilder/builderror/!=(_:_:).md)
  Determines whether two errors aren’t equal.
- [func hash(into: inout Hasher)](roombuilder/builderror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](roombuilder/builderror/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](roombuilder/builderror/equatable-implementations.md)
- [Error Implementations](roombuilder/builderror/error-implementations.md)
- [LocalizedError Implementations](roombuilder/builderror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roombuilder/builderror)*