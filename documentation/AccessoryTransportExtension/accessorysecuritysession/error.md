# AccessorySecuritySession.Error

**Framework**: Accessory Transport Extension  
**Kind**: enum  
**Role**: Enumeration

An error that occurs during accessory security-session operations.

**Availability**:
- iOS 26.5+

## Declaration

```swift
enum Error
```

#### Overview

The framework throws errors of this type when security-session operations fail. Use the error cases to determine the specific cause and handle it appropriately in your accessory transport-security extension.

## Topics

### Interpreting the error cause
- [AccessorySecuritySession.Error.invalidated](./error/invalidated.md)
  Session was invalidated.
- [AccessorySecuritySession.Error.unknown](./error/unknown.md)
  Underlying failure with an unknown cause.
- [AccessorySecuritySession.Error.unsupported](./error/unsupported.md)
  Unsupported value, operation, etc.
### Accessing error details
- [var description: String](./error/description.md)
  A string that describes the error.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling session events
- [AccessorySecuritySession.EventHandler](./eventhandler.md)
  A protocol that defines methods for handling security session events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/error)*