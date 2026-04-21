# AccessoryMessage.Error

**Framework**: Accessory Transport Extension  
**Kind**: enum

An enumeration of errors that can occur during message transmission.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)
- Mac Catalyst 26.5+ (Beta)

## Declaration

```swift
enum Error
```

## Topics

### Identifying error types
- [AccessoryMessage.Error.transportFailed](accessorymessage/error/transportfailed.md)
  An error indicating the transport failed but may recover.
- [AccessoryMessage.Error.transportUnavailable](accessorymessage/error/transportunavailable.md)
  An error indicating the transport is unavailable.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AccessoryMessage.Result](accessorymessage/result.md)
  An enumeration of results for message transmission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/error)*