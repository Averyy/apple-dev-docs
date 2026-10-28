# init(nickname:number:accountType:organizationName:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a payment account object with the specified account information.

**Availability**:
- iOS 10.3+ - Deprecated in 11.0
- iPadOS 10.3+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use [`init(nickname:number:accountType:organizationName:balance:secondaryBalance:)`](./init%28nickname,number,accounttype,organizationname,balance,secondarybalance%29.md) instead.

## Declaration

```swift
convenience init?(nickname: INSpeakableString, number: String?, accountType: INAccountType, organizationName: INSpeakableString?)
```

```objc
- (instancetype) initWithNickname:(INSpeakableString *) nickname number:(NSString *) number accountType:(INAccountType) accountType organizationName:(INSpeakableString *) organizationName;
```

## Return Value

An initialized [`INPaymentAccount`](../inpaymentaccount.md) object.

## Discussion

Use this method to create payment accounts associated with the user.

## Parameters

- `nickname`: A user-defined name that identifies the account in your app. Never include account numbers or other potentially sensitive user information in this parameter.
- `number`: A string to help the user differentiate between similar accounts. Typically, you use this parameter to specify only the last few digits of the user’s account. Never specify the user’s full account number.
- `accountType`: The type of the account. Typical account types include checking accounts, savings accounts, credit accounts, and many others. For a complete list, see [`INAccountType`](../inaccounttype.md).
- `organizationName`: The organization that provides the account for the user. For example, this parameter might contain the name of the user’s bank. Never include account numbers or other potentially sensitive user information in this parameter.

## See Also

### Initializing the Payment Account
- [init(nickname: INSpeakableString, number: String?, accountType: INAccountType, organizationName: INSpeakableString?, balance: INBalanceAmount?, secondaryBalance: INBalanceAmount?)](./init%28nickname,number,accounttype,organizationname,balance,secondarybalance%29.md)
  Initializes a payment account object with the specified account information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentaccount/init(nickname:number:accounttype:organizationname:))*