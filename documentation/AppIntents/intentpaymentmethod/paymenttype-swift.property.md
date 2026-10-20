# paymentType

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

The kind of payment method, such as a credit card or bank account

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
var paymentType: IntentPaymentMethod.PaymentType { get }
```

## See Also

### Getting the payment details
- [var name: String?](./name.md)
  The user-visible name of the payment method
- [var identificationHint: String?](./identificationhint.md)
  A hint making it easier for the user to identify the payment method among others of similar name or type, such as the last several digits of a credit card number
- [var icon: DisplayRepresentation.Image?](./icon.md)
  The icon or image representing this payment method
- [IntentPaymentMethod.PaymentType](./paymenttype-swift.enum.md)
  Constants that describe the available payment options, such as credit cards or bank accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentpaymentmethod/paymenttype-swift.property)*