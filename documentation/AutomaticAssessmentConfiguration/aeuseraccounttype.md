# AEUserAccountType

**Framework**: Automatic Assessment Configuration  
**Kind**: enum  
**Role**: Enumeration

Specifies the type of account required for an assessment session.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
@frozen
enum AEUserAccountType
```

```c
enum AEUserAccountType : NSInteger;
```

## Topics

### Enumeration Cases
- [AEUserAccountType.any](./aeuseraccounttype/any.md)
  No specific account type is required.
- [AEUserAccountType.guest](./aeuseraccounttype/guest.md)
  Requires a guest user account.
- [AEUserAccountType.standard](./aeuseraccounttype/standard.md)
  Requires a standard user account.
### Initializers
- [init?(rawValue: Int)](./aeuseraccounttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeuseraccounttype)*