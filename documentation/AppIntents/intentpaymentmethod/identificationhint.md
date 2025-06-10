# identificationHint

**Framework**: App Intents  
**Kind**: property

A hint making it easier for the user to identify the payment method among others of similar name or type, such as the last several digits of a credit card number

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
var identificationHint: String? { get }
```

## See Also

- [var paymentType: IntentPaymentMethod.PaymentType](intentpaymentmethod/paymenttype-swift.property.md)
  The kind of payment method, such as a credit card or bank account
- [var name: String?](intentpaymentmethod/name.md)
  The user-visible name of the payment method
- [var icon: DisplayRepresentation.Image?](intentpaymentmethod/icon.md)
  The icon or image representing this payment method
- [IntentPaymentMethod.PaymentType](intentpaymentmethod/paymenttype-swift.enum.md)
  Constants that describe the available payment options, such as credit cards or bank accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentpaymentmethod/identificationhint)*