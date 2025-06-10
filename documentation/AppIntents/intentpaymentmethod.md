# IntentPaymentMethod

**Framework**: App Intents  
**Kind**: struct

Information about a form of payment supported by your app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct IntentPaymentMethod
```

#### Overview

An `IntentPaymentMethod` type describes a way someone pays for goods and services. This type contains information you can display in your interface to convey the payment type to people. Specifically, it stores the name of the payment service and an icon for any related brand information. Typical payment methods include credit cards and bank accounts.

## Topics

### Creating a payment method
- [init(type: IntentPaymentMethod.PaymentType, name: LocalizedStringResource?, identificationHint: String?, icon: DisplayRepresentation.Image?)](intentpaymentmethod/init(type:name:identificationhint:icon:).md)
### Getting the payment details
- [var paymentType: IntentPaymentMethod.PaymentType](intentpaymentmethod/paymenttype-swift.property.md)
  The kind of payment method, such as a credit card or bank account
- [var name: String?](intentpaymentmethod/name.md)
  The user-visible name of the payment method
- [var identificationHint: String?](intentpaymentmethod/identificationhint.md)
  A hint making it easier for the user to identify the payment method among others of similar name or type, such as the last several digits of a credit card number
- [var icon: DisplayRepresentation.Image?](intentpaymentmethod/icon.md)
  The icon or image representing this payment method
- [IntentPaymentMethod.PaymentType](intentpaymentmethod/paymenttype-swift.enum.md)
  Constants that describe the available payment options, such as credit cards or bank accounts.
### Type Aliases
- [IntentPaymentMethod.Specification](intentpaymentmethod/specification.md)
- [IntentPaymentMethod.UnwrappedType](intentpaymentmethod/unwrappedtype.md)
- [IntentPaymentMethod.ValueType](intentpaymentmethod/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: EmptyResolverSpecification<IntentPaymentMethod>](intentpaymentmethod/defaultresolverspecification.md)
### Default Implementations
- [InstanceDisplayRepresentable Implementations](intentpaymentmethod/instancedisplayrepresentable-implementations.md)
- [TypeDisplayRepresentable Implementations](intentpaymentmethod/typedisplayrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [DisplayRepresentable](displayrepresentable.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)

## See Also

- [struct IntentCurrencyAmount](intentcurrencyamount.md)
  An amount of money to transfer during a financial transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentpaymentmethod)*