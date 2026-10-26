# accountType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of the account.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var accountType: INAccountType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INAccountType accountType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INAccountType accountType;
```

#### Discussion

If this property contains a value other than [`INAccountType.unknown`](../inaccounttype/unknown.md), use the value to limit your search to accounts of the specified type.

## See Also

### Getting the Search Attributes
- [var accountNickname: INSpeakableString?](./accountnickname.md)
  The nickname that the user assigned to the account.
- [var organizationName: INSpeakableString?](./organizationname.md)
  The name of an organization attached to the account.
- [var requestedBalanceType: INBalanceType](./requestedbalancetype.md)
  The balance type requested by the user.
- [enum INBalanceType](../inbalancetype.md)
  Constants indicating the meaning of a balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintent/accounttype)*