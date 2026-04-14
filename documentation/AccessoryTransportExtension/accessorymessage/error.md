# AccessoryMessage.Error

**Framework**: Accessory Transport Extension  
**Kind**: enum

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
enum Error
```

## Topics

### Enumeration Cases
- [AccessoryMessage.Error.transportFailed](accessorymessage/error/transportfailed.md)
  Transport failed but may recover. Message will be sent again for retry.
- [AccessoryMessage.Error.transportUnavailable](accessorymessage/error/transportunavailable.md)
  Transport is unavailable. Retry will occur on different transport if applicable.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/error)*