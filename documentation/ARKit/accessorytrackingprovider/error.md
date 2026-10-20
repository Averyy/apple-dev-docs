# AccessoryTrackingProvider.Error

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

An accessory tracking error.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct Error
```

## Topics

### Instance Properties
- [var code: AccessoryTrackingProvider.Error.Code](./error/code-swift.property.md)
  The error code.
- [var description: String](./error/description.md)
  A textual representation of this error.
- [var errorDescription: String?](./error/errordescription.md)
  A localized message describing what error occurred.
- [var failureReason: String?](./error/failurereason.md)
  A localized message describing the reason for the failure.
- [var recoverySuggestion: String?](./error/recoverysuggestion.md)
  A localized message describing how one might recover from the failure.
- [let source: Accessory.Source?](./error/source.md)
  Source for an accessory if creating it failed.
### Enumerations
- [AccessoryTrackingProvider.Error.Code](./error/code-swift.enum.md)
  Enumeration of all error codes.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Error](../../Swift/error.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessorytrackingprovider/error)*