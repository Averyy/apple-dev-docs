# ASAccessory.AccessoryState

**Framework**: AccessorySetupKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration of possible authorization states of an accessory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum AccessoryState
```

```c
enum ASAccessoryState : NSInteger;
```

## Topics

### Creating a state instance
- [init?(rawValue: Int)](./accessorystate/init%28rawvalue%29.md)
### Accessory states
- [ASAccessory.AccessoryState.unauthorized](./accessorystate/unauthorized.md)
  The accessory is invalid or unauthorized.
- [ASAccessory.AccessoryState.awaitingAuthorization](./accessorystate/awaitingauthorization.md)
  The accessory is selected, but full authorization is still pending.
- [ASAccessory.AccessoryState.authorized](./accessorystate/authorized.md)
  The accessory is authorized and available.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessory description
- [class ASAccessory](../asaccessory.md)
  An accessory discovered by the accessory session.
- [class ASDiscoveredAccessory](../asdiscoveredaccessory.md)
  A discovered accessory, for use in creating a customized picker display item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/accessorystate)*