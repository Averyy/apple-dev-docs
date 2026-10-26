# INBalanceType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the meaning of a balance.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum INBalanceType
```

```c
enum INBalanceType : NSInteger;
```

## Topics

### Constants
- [INBalanceType.unknown](./inbalancetype/unknown.md)
  An unknown balance type.
- [INBalanceType.money](./inbalancetype/money.md)
  A monetary balance involving a known currency.
- [INBalanceType.points](./inbalancetype/points.md)
  A balance of points, such as those associated with a reward or bonus program.
- [INBalanceType.miles](./inbalancetype/miles.md)
  A balance of miles, such as those associated with a frequent flier program.
### Initializers
- [init?(rawValue: Int)](./inbalancetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Search Attributes
- [var accountNickname: INSpeakableString?](./insearchforaccountsintent/accountnickname.md)
  The nickname that the user assigned to the account.
- [var accountType: INAccountType](./insearchforaccountsintent/accounttype.md)
  The type of the account.
- [var organizationName: INSpeakableString?](./insearchforaccountsintent/organizationname.md)
  The name of an organization attached to the account.
- [var requestedBalanceType: INBalanceType](./insearchforaccountsintent/requestedbalancetype.md)
  The balance type requested by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbalancetype)*