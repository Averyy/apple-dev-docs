# INPaymentMethodType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants describing the available payment options.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INPaymentMethodType
```

```c
enum INPaymentMethodType : NSInteger;
```

## Topics

### Constants
- [INPaymentMethodType.unknown](./inpaymentmethodtype/unknown.md)
  An unspecified payment type.
- [INPaymentMethodType.checking](./inpaymentmethodtype/checking.md)
  Payment from a checking account.
- [INPaymentMethodType.savings](./inpaymentmethodtype/savings.md)
  Payment from a savings account.
- [INPaymentMethodType.brokerage](./inpaymentmethodtype/brokerage.md)
  Payment from a brokerage account.
- [INPaymentMethodType.debit](./inpaymentmethodtype/debit.md)
  Payment using a debit card.
- [INPaymentMethodType.credit](./inpaymentmethodtype/credit.md)
  Payment using a credit card.
- [INPaymentMethodType.prepaid](./inpaymentmethodtype/prepaid.md)
  Payment using a prepaid card or account.
- [INPaymentMethodType.store](./inpaymentmethodtype/store.md)
  Payment using a store charge card.
- [INPaymentMethodType.applePay](./inpaymentmethodtype/applepay.md)
  Payment using Apple Pay.
### Initializers
- [init?(rawValue: Int)](./inpaymentmethodtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Payment Information
- [var type: INPaymentMethodType](./inpaymentmethod/type.md)
  The type of account used as the source of funds.
- [var name: String?](./inpaymentmethod/name.md)
  The name of this payment type.
- [var identificationHint: String?](./inpaymentmethod/identificationhint.md)
  The hint for identifying the payment method.
- [var icon: INImage?](./inpaymentmethod/icon.md)
  The image representing the payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentmethodtype)*