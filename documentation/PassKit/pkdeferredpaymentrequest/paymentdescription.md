# paymentDescription

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A description of the deferred payment.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- visionOS 1.0+

## Declaration

```swift
var paymentDescription: String { get set }
```

#### Discussion

Use a plain language description that explains what the payment is for, for example “Hotel stay, 2 nights.”

## See Also

- [var freeCancellationDate: Date?](pkdeferredpaymentrequest/freecancellationdate.md)
  The date before which you must cancel a deferred payment without incurring any cancellation charges.
- [var billingAgreement: String?](pkdeferredpaymentrequest/billingagreement.md)
  The localized billing agreement the framework displays to the user prior to payment authorization.
- [var freeCancellationDateTimeZone: TimeZone?](pkdeferredpaymentrequest/freecancellationdatetimezone.md)
  The time zone at the destination location of the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdeferredpaymentrequest/paymentdescription)*