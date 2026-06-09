# AccessoryTransportSession.Error

**Framework**: Accessory Transport Extension  
**Kind**: enum

Errors that can occur with an accessory transport session.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
enum Error
```

## Topics

### Identifying session errors
- [AccessoryTransportSession.Error.invalidated](accessorytransportsession/error/invalidated.md)
  An error that indicates the session is invalidated.
- [AccessoryTransportSession.Error.unsupported](accessorytransportsession/error/unsupported.md)
  An error that indicates the framework doesn’t support an client-provided value or operation.
- [AccessoryTransportSession.Error.unknown](accessorytransportsession/error/unknown.md)
  An error that indicates a failure with an unknown cause.
### Describing an error
- [var description: String](accessorytransportsession/error/description.md)
  A string that describes the transport-session error.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/error)*