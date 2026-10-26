# INAccountType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the type of account involved in a financial transaction.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INAccountType
```

```c
enum INAccountType : NSInteger;
```

## Topics

### Constants
- [INAccountType.unknown](./inaccounttype/unknown.md)
  An unknown type of account.
- [INAccountType.checking](./inaccounttype/checking.md)
  A checking account.
- [INAccountType.credit](./inaccounttype/credit.md)
  A credit card account.
- [INAccountType.debit](./inaccounttype/debit.md)
  A debit account.
- [INAccountType.investment](./inaccounttype/investment.md)
  An investment account.
- [INAccountType.mortgage](./inaccounttype/mortgage.md)
  A mortgage account.
- [INAccountType.prepaid](./inaccounttype/prepaid.md)
  A prepaid account.
- [INAccountType.saving](./inaccounttype/saving.md)
  A savings account.
### Initializers
- [init?(rawValue: Int)](./inaccounttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data Objects
- [class INCurrencyAmount](./incurrencyamount.md)
  An amount of money to transfer during a financial transaction.
- [class INPaymentAccount](./inpaymentaccount.md)
  A user account that provides the funds when making a payment.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaccounttype)*