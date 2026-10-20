# AccessoryMessage.Error

**Framework**: Accessory Transport Extension  
**Kind**: enum  
**Role**: Enumeration

An enumeration of errors that can occur during message transmission.

**Availability**:
- iOS 26.5+

## Declaration

```swift
enum Error
```

## Topics

### Identifying error types
- [AccessoryMessage.Error.transportFailed](./error/transportfailed.md)
  An error indicating the transport failed but may recover.
- [AccessoryMessage.Error.transportUnavailable](./error/transportunavailable.md)
  An error indicating the transport is unavailable.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Assessing outcomes
- [AccessoryMessage.Result](./result.md)
  An enumeration of results for message transmission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/error)*