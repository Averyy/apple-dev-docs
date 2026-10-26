# INPaymentAccount

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A user account that provides the funds when making a payment.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INPaymentAccount
```

```objc
@interface INPaymentAccount : NSObject
```

#### Overview

An [`INPaymentAccount`](./inpaymentaccount.md) object represents a user account known to your app. When paying bills, you use the specified payment account as the source of any funds involved in the financial transaction. Your app must have the authority to transfer funds from the designated account to any payees.

## Topics

### Initializing the Payment Account
- [init(nickname: INSpeakableString, number: String?, accountType: INAccountType, organizationName: INSpeakableString?, balance: INBalanceAmount?, secondaryBalance: INBalanceAmount?)](./inpaymentaccount/init%28nickname,number,accounttype,organizationname,balance,secondarybalance%29.md)
  Initializes a payment account object with the specified account information.
- [convenience init?(nickname: INSpeakableString, number: String?, accountType: INAccountType, organizationName: INSpeakableString?)](./inpaymentaccount/init%28nickname,number,accounttype,organizationname%29.md)
  Initializes a payment account object with the specified account information.
### Getting the Account Details
- [var nickname: INSpeakableString?](./inpaymentaccount/nickname.md)
  A user-defined name that identifies the account.
- [var organizationName: INSpeakableString?](./inpaymentaccount/organizationname.md)
  The name of the organization that supplies the account to the user.
- [var accountType: INAccountType](./inpaymentaccount/accounttype.md)
  The type of the account.
- [enum INAccountType](./inaccounttype.md)
  Constants indicating the type of account involved in a financial transaction.
- [var accountNumber: String?](./inpaymentaccount/accountnumber.md)
  A string to help the user differentiate between similar accounts.
### Getting the Account Balance
- [var balance: INBalanceAmount?](./inpaymentaccount/balance.md)
  The primary balance associated with the account.
- [var secondaryBalance: INBalanceAmount?](./inpaymentaccount/secondarybalance.md)
  A secondary balance, if any, associated with the account.
- [class INBalanceAmount](./inbalanceamount.md)
  A balance associated with an account.
### Initializers
- [init?(coder: NSCoder)](./inpaymentaccount/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Data Objects
- [enum INAccountType](./inaccounttype.md)
  Constants indicating the type of account involved in a financial transaction.
- [class INCurrencyAmount](./incurrencyamount.md)
  An amount of money to transfer during a financial transaction.
- [class INPaymentAmount](./inpaymentamount.md)
  The amount of money to apply to a bill payment.
- [class INPaymentMethod](./inpaymentmethod.md)
  Information about a form of payment supported by your app.
- [class INPaymentRecord](./inpaymentrecord.md)
  Detailed information about a financial transaction made between two users.
- [enum INPaymentStatus](./inpaymentstatus.md)
  Constants indicating the state of the financial transaction.
- [class INPerson](./inperson.md)
  Information about a person participating in a SiriKit interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentaccount)*