# accountNickname

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The nickname that the user assigned to the account.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@NSCopying
var accountNickname: INSpeakableString? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpeakableString * accountNickname;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpeakableString * accountNickname;
```

## Discussion

When the user provides a nickname, look for an account whose name contains all or part of the specified string. Match the string against the user-visible nickname shown by your app.

## See Also

### Getting the Search Attributes
- [var accountType: INAccountType](./accounttype.md)
  The type of the account.
- [var organizationName: INSpeakableString?](./organizationname.md)
  The name of an organization attached to the account.
- [var requestedBalanceType: INBalanceType](./requestedbalancetype.md)
  The balance type requested by the user.
- [enum INBalanceType](../inbalancetype.md)
  Constants indicating the meaning of a balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintent/accountnickname)*