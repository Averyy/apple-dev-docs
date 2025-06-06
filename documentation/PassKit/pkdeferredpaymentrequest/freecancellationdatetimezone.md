# freeCancellationDateTimeZone

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The time zone at the destination location of the payment.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- visionOS 1.0+

## Declaration

```swift
var freeCancellationDateTimeZone: TimeZone? { get set }
```

#### Discussion

For a hotel booking, for example, this refers to the local time zone of the hotel. On the payment sheet, this is the time zone the framework uses to format the cancellation date. If you set the `freeCancellationDateTimeZone` date, you need to set [`freeCancellationDate`](pkdeferredpaymentrequest/freecancellationdate.md) as well.

## See Also

- [var freeCancellationDate: Date?](pkdeferredpaymentrequest/freecancellationdate.md)
  The date before which you must cancel a deferred payment without incurring any cancellation charges.
- [var billingAgreement: String?](pkdeferredpaymentrequest/billingagreement.md)
  The localized billing agreement the framework displays to the user prior to payment authorization.
- [var paymentDescription: String](pkdeferredpaymentrequest/paymentdescription.md)
  A description of the deferred payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdeferredpaymentrequest/freecancellationdatetimezone)*