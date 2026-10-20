# SecKeyOperationType

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The types of operations that you can use a cryptographic key to perform.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum SecKeyOperationType
```

```c
enum SecKeyOperationType : CFIndex;
```

## Topics

### Enumeration Cases
- [SecKeyOperationType.decrypt](./seckeyoperationtype/decrypt.md)
- [SecKeyOperationType.encrypt](./seckeyoperationtype/encrypt.md)
- [SecKeyOperationType.keyExchange](./seckeyoperationtype/keyexchange.md)
- [SecKeyOperationType.sign](./seckeyoperationtype/sign.md)
- [SecKeyOperationType.verify](./seckeyoperationtype/verify.md)
### Initializers
- [init?(rawValue: CFIndex)](./seckeyoperationtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyoperationtype)*