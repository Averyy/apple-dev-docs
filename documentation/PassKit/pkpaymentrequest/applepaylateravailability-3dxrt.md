# applePayLaterAvailability

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A value that indicates whether Apple Pay Later is available for a transaction.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var applePayLaterAvailability: PKPaymentRequest.ApplePayLaterAvailability { get set }
```

#### Discussion

Defaults to enabled.

Use this property to suppress Apple Pay Later for a specific transaction. Only set this property if you have a specific requirement to disable Apple Pay Later.

Ensure you select the correct mode that matches your requirement, because the framework displays Apple Pay Later availability to the user.

> ❗ **Important**:  If you later decide to stop providing Apple Pay Later in your app, contact your acquirer or payment service provider (PSP) and notify them that you no longer wish to participate in the Mastercard Installments Program. You can always change this decision later.

 If you later decide to stop providing Apple Pay Later in your app, contact your acquirer or payment service provider (PSP) and notify them that you no longer wish to participate in the Mastercard Installments Program. You can always change this decision later.

## See Also

- [PKPaymentRequest.ApplePayLaterAvailability](pkpaymentrequest/applepaylateravailability-swift.enum.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.
- [struct PKAddressField](pkaddressfield.md)
  Billing or shipping address fields.
- [enum PKApplePayLaterAvailability](pkapplepaylateravailability.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/applepaylateravailability-3dxrt)*