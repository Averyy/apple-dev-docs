# CapturedRoom.ModelProvider.Error

**Framework**: RoomPlan  
**Kind**: enum  
**Role**: Enumeration

Errors that can occur when managing 3D model association with categories and attributes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum Error
```

## Overview

The `modelFileURL` functions can throw an error of this type, such as `CapturedRoom/ModelProvider/modelFileURL(for:)-42iz3`.

## Topics

### Interpreting the error
- [CapturedRoom.ModelProvider.Error.attributeCombinationNotSupported](./error/attributecombinationnotsupported.md)
  An error that indicates the framework doesn’t support the attributes set in a model-URL query.
- [CapturedRoom.ModelProvider.Error.nonExistingFile(url:)](./error/nonexistingfile%28url%29.md)
  An error that indicates a model-URL query failed to return a result.
### Inspecting error information
- [var errorDescription: String?](./error/errordescription.md)
  A human-readable explanation for the particular model-provider error.

## Relationships

### Conforms To
- [Error](../../../Swift/error.md)
- [LocalizedError](../../../Foundation/localizederror.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/modelprovider/error)*