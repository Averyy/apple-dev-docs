# init(nickname:number:accountType:organizationName:balance:secondaryBalance:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a payment account object with the specified account information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(nickname: INSpeakableString, number: String?, accountType: INAccountType, organizationName: INSpeakableString?, balance: INBalanceAmount?, secondaryBalance: INBalanceAmount?)
```

```objc
- (instancetype) initWithNickname:(INSpeakableString *) nickname number:(NSString *) number accountType:(INAccountType) accountType organizationName:(INSpeakableString *) organizationName balance:(INBalanceAmount *) balance secondaryBalance:(INBalanceAmount *) secondaryBalance;
```

#### Return Value

An initialized [`INPaymentAccount`](../inpaymentaccount.md) object.

#### Discussion

Use this method to create payment accounts associated with the user.

## Parameters

- `nickname`: A user-defined name that identifies the account in your app. Never include account numbers or other potentially sensitive user information in this parameter.
- `number`: A string to help the user differentiate between similar accounts. Typically, you use this parameter to specify only the last few digits of the user’s account. Never specify the user’s full account number.
- `accountType`: The type of the account. Typical account types include checking accounts, savings accounts, credit accounts, and many others. For a complete list, see [`INAccountType`](../inaccounttype.md).
- `organizationName`: The organization that provides the account for the user. For example, this parameter might contain the name of the user’s bank. Never include account numbers or other potentially sensitive user information in this parameter.
- `balance`: The primary balance for the account.
- `secondaryBalance`: A secondary balance associated with the account. For example, a credit card account might have points or frequent flier miles based on the user’s purchases.

## See Also

### Initializing the Payment Account
- [convenience init?(nickname: INSpeakableString, number: String?, accountType: INAccountType, organizationName: INSpeakableString?)](./init%28nickname,number,accounttype,organizationname%29.md)
  Initializes a payment account object with the specified account information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentaccount/init(nickname:number:accounttype:organizationname:balance:secondarybalance:))*