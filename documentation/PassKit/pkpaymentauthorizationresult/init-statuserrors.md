# init(status:errors:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Initializes the result with the status code and list of errors.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(status: PKPaymentAuthorizationStatus, errors: [any Error]?)
```

## Parameters

- `status`: The status of the payment.
- `errors`: Any errors returned from the authorization status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationresult/init(status:errors:))*