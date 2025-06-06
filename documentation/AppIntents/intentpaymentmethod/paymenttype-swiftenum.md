# IntentPaymentMethod.PaymentType

**Framework**: App Intents  
**Kind**: enum

Constants that describe the available payment options, such as credit cards or bank accounts.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum PaymentType
```

## Topics

### Getting the payment options
- [IntentPaymentMethod.PaymentType.applePay](intentpaymentmethod/paymenttype-swift.enum/applepay.md)
- [IntentPaymentMethod.PaymentType.brokerage](intentpaymentmethod/paymenttype-swift.enum/brokerage.md)
- [IntentPaymentMethod.PaymentType.checking](intentpaymentmethod/paymenttype-swift.enum/checking.md)
- [IntentPaymentMethod.PaymentType.credit](intentpaymentmethod/paymenttype-swift.enum/credit.md)
- [IntentPaymentMethod.PaymentType.debit](intentpaymentmethod/paymenttype-swift.enum/debit.md)
- [IntentPaymentMethod.PaymentType.prepaid](intentpaymentmethod/paymenttype-swift.enum/prepaid.md)
- [IntentPaymentMethod.PaymentType.savings](intentpaymentmethod/paymenttype-swift.enum/savings.md)
- [IntentPaymentMethod.PaymentType.store](intentpaymentmethod/paymenttype-swift.enum/store.md)
- [IntentPaymentMethod.PaymentType.unknown](intentpaymentmethod/paymenttype-swift.enum/unknown.md)
### Operators
- [static func == (IntentPaymentMethod.PaymentType, IntentPaymentMethod.PaymentType) -> Bool](intentpaymentmethod/paymenttype-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](intentpaymentmethod/paymenttype-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](intentpaymentmethod/paymenttype-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](intentpaymentmethod/paymenttype-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var paymentType: IntentPaymentMethod.PaymentType](intentpaymentmethod/paymenttype-swift.property.md)
  The kind of payment method, such as a credit card or bank account
- [var name: String?](intentpaymentmethod/name.md)
  The user-visible name of the payment method
- [var identificationHint: String?](intentpaymentmethod/identificationhint.md)
  A hint making it easier for the user to identify the payment method among others of similar name or type, such as the last several digits of a credit card number
- [var icon: DisplayRepresentation.Image?](intentpaymentmethod/icon.md)
  The icon or image representing this payment method


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentpaymentmethod/paymenttype-swift.enum)*