# AccessoryTransportSession.Error

**Framework**: AccessoryTransportExtension  
**Kind**: enum

A type that defines errors encountered when using an accessory transport session.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
enum Error
```

## Topics

### Handling session errors
- [AccessoryTransportSession.Error.invalidated](accessorytransportsession/error/invalidated.md)
  An error that indicates the session became invalidated.
### Handling accessory errors
- [AccessoryTransportSession.Error.unsupported](accessorytransportsession/error/unsupported.md)
  An error that indicates the framework doesn’t support a provided value or attempted operation.
### Handling unknown errors
- [AccessoryTransportSession.Error.unknown](accessorytransportsession/error/unknown.md)
  An error that indicates a failure with an unknown underlying cause.
### Describing an error
- [var description: String](accessorytransportsession/error/description.md)
  A textual representation of this instance.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func cancel(error: AccessoryTransportSession.Error?)](accessorytransportsession/cancel(error:).md)
  Cancels the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/error)*