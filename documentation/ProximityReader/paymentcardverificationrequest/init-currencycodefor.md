# init(currencyCode:for:)

**Framework**: ProximityReader  
**Kind**: init

Creates a new verification request using the specified currency and reason information.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
init(currencyCode: String, for reason: PaymentCardVerificationRequest.Reason = .other)
```

## Parameters

- `currencyCode`: The ISO 4217 code for the requested currency type. Specify the   currency you intend to verify. If you specify an empty string, the system throws   .
- `reason`: The reason for the verification request. Based on the reason   you select, the system displays an appropriate message in the system UI   to inform the user about the purpose of the verification process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardverificationrequest/init(currencycode:for:))*