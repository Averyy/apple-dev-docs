# AccessorySecuritySession.Error

**Framework**: Accessory Transport Extension  
**Kind**: enum

An error that occurs during accessory security-session operations.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
enum Error
```

#### Overview

The framework throws errors of this type when security-session operations fail. Use the error cases to determine the specific cause and handle it appropriately in your accessory transport-security extension.

## Topics

### Interpreting the error cause
- [AccessorySecuritySession.Error.invalidated](accessorysecuritysession/error/invalidated.md)
  Session was invalidated.
- [AccessorySecuritySession.Error.unknown](accessorysecuritysession/error/unknown.md)
  Underlying failure with an unknown cause.
- [AccessorySecuritySession.Error.unsupported](accessorysecuritysession/error/unsupported.md)
  Unsupported value, operation, etc.
### Accessing error details
- [var description: String](accessorysecuritysession/error/description.md)
  A string that describes the error.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AccessorySecuritySession.EventHandler](accessorysecuritysession/eventhandler.md)
  A protocol that defines methods for handling security session events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/error)*