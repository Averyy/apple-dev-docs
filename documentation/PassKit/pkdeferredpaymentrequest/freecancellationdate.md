# freeCancellationDate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The date before which you must cancel a deferred payment without incurring any cancellation charges.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- visionOS 1.0+

## Declaration

```swift
var freeCancellationDate: Date? { get set }
```

#### Discussion

If you set [`freeCancellationDate`](pkdeferredpaymentrequest/freecancellationdate.md), you need to set [`freeCancellationDateTimeZone`](pkdeferredpaymentrequest/freecancellationdatetimezone.md) as well.

## See Also

- [var billingAgreement: String?](pkdeferredpaymentrequest/billingagreement.md)
  The localized billing agreement the framework displays to the user prior to payment authorization.
- [var paymentDescription: String](pkdeferredpaymentrequest/paymentdescription.md)
  A description of the deferred payment.
- [var freeCancellationDateTimeZone: TimeZone?](pkdeferredpaymentrequest/freecancellationdatetimezone.md)
  The time zone at the destination location of the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdeferredpaymentrequest/freecancellationdate)*