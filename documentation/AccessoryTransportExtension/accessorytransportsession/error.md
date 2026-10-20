# AccessoryTransportSession.Error

**Framework**: Accessory Transport Extension  
**Kind**: enum  
**Role**: Enumeration

Errors that can occur with an accessory transport session.

**Availability**:
- iOS 26.2+

## Declaration

```swift
enum Error
```

## Topics

### Identifying session errors
- [AccessoryTransportSession.Error.invalidated](./error/invalidated.md)
  An error that indicates the session is invalidated.
- [AccessoryTransportSession.Error.unsupported](./error/unsupported.md)
  An error that indicates the framework doesn’t support an client-provided value or operation.
- [AccessoryTransportSession.Error.unknown](./error/unknown.md)
  An error that indicates a failure with an unknown cause.
### Describing an error
- [var description: String](./error/description.md)
  A string that describes the transport-session error.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/error)*