# AccessoryTrackingProvider.Error

**Framework**: ARKit  
**Kind**: struct

An accessory tracking error.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Error
```

## Topics

### Instance Properties
- [var code: AccessoryTrackingProvider.Error.Code](accessorytrackingprovider/error/code-swift.property.md)
  The error code.
- [var description: String](accessorytrackingprovider/error/description.md)
  A textual representation of this error.
- [var errorDescription: String?](accessorytrackingprovider/error/errordescription.md)
  A localized message describing what error occurred.
- [var failureReason: String?](accessorytrackingprovider/error/failurereason.md)
  A localized message describing the reason for the failure.
- [var recoverySuggestion: String?](accessorytrackingprovider/error/recoverysuggestion.md)
  A localized message describing how one might recover from the failure.
- [let source: Accessory.Source?](accessorytrackingprovider/error/source.md)
  Source for an accessory if creating it failed.
### Enumerations
- [AccessoryTrackingProvider.Error.Code](accessorytrackingprovider/error/code-swift.enum.md)
  Enumeration of all error codes.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessorytrackingprovider/error)*