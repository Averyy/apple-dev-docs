# IntentPaymentMethod.PaymentType

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the available payment options, such as credit cards or bank accounts.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
enum PaymentType
```

## Topics

### Getting the payment options
- [IntentPaymentMethod.PaymentType.applePay](./paymenttype-swift.enum/applepay.md)
- [IntentPaymentMethod.PaymentType.brokerage](./paymenttype-swift.enum/brokerage.md)
- [IntentPaymentMethod.PaymentType.checking](./paymenttype-swift.enum/checking.md)
- [IntentPaymentMethod.PaymentType.credit](./paymenttype-swift.enum/credit.md)
- [IntentPaymentMethod.PaymentType.debit](./paymenttype-swift.enum/debit.md)
- [IntentPaymentMethod.PaymentType.prepaid](./paymenttype-swift.enum/prepaid.md)
- [IntentPaymentMethod.PaymentType.savings](./paymenttype-swift.enum/savings.md)
- [IntentPaymentMethod.PaymentType.store](./paymenttype-swift.enum/store.md)
- [IntentPaymentMethod.PaymentType.unknown](./paymenttype-swift.enum/unknown.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the payment details
- [var paymentType: IntentPaymentMethod.PaymentType](./paymenttype-swift.property.md)
  The kind of payment method, such as a credit card or bank account
- [var name: String?](./name.md)
  The user-visible name of the payment method
- [var identificationHint: String?](./identificationhint.md)
  A hint making it easier for the user to identify the payment method among others of similar name or type, such as the last several digits of a credit card number
- [var icon: DisplayRepresentation.Image?](./icon.md)
  The icon or image representing this payment method


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentpaymentmethod/paymenttype-swift.enum)*