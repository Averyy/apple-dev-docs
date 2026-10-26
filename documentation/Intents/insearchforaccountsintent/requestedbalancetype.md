# requestedBalanceType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The balance type requested by the user.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var requestedBalanceType: INBalanceType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INBalanceType requestedBalanceType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INBalanceType requestedBalanceType;
```

#### Discussion

If this property contains a value other than [`INBalanceType.unknown`](../inbalancetype/unknown.md), use the value to retrieve the balance associated with the specified account. Include the balance information in your response object.

## See Also

### Getting the Search Attributes
- [var accountNickname: INSpeakableString?](./accountnickname.md)
  The nickname that the user assigned to the account.
- [var accountType: INAccountType](./accounttype.md)
  The type of the account.
- [var organizationName: INSpeakableString?](./organizationname.md)
  The name of an organization attached to the account.
- [enum INBalanceType](../inbalancetype.md)
  Constants indicating the meaning of a balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintent/requestedbalancetype)*