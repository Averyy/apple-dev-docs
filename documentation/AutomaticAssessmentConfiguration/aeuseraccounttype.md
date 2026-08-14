# AEUserAccountType

**Framework**: Automatic Assessment Configuration  
**Kind**: enum

Specifies the type of account required for an assessment session.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
@frozen
enum AEUserAccountType
```

## Topics

### Enumeration Cases
- [AEUserAccountType.any](aeuseraccounttype/any.md)
  No specific account type is required.
- [AEUserAccountType.guest](aeuseraccounttype/guest.md)
  Requires a guest user account.
- [AEUserAccountType.standard](aeuseraccounttype/standard.md)
  Requires a standard user account.
### Initializers
- [init?(rawValue: Int)](aeuseraccounttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeuseraccounttype)*