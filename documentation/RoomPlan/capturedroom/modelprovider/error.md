# CapturedRoom.ModelProvider.Error

**Framework**: RoomPlan  
**Kind**: enum

Errors that can occur when managing 3D model association with categories and attributes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum Error
```

#### Overview

The `modelFileURL` functions can throw an error of this type, such as `CapturedRoom/ModelProvider/modelFileURL(for:)-42iz3`.

## Topics

### Interpreting the error
- [CapturedRoom.ModelProvider.Error.attributeCombinationNotSupported](capturedroom/modelprovider/error/attributecombinationnotsupported.md)
  An error that indicates the framework doesn’t support the attributes set in a model-URL query.
- [CapturedRoom.ModelProvider.Error.nonExistingFile(url:)](capturedroom/modelprovider/error/nonexistingfile(url:).md)
  An error that indicates a model-URL query failed to return a result.
### Inspecting error information
- [var errorDescription: String?](capturedroom/modelprovider/error/errordescription.md)
  A human-readable explanation for the particular model-provider error.
### Default Implementations
- [Error Implementations](capturedroom/modelprovider/error/error-implementations.md)
- [LocalizedError Implementations](capturedroom/modelprovider/error/localizederror-implementations.md)

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/modelprovider/error)*