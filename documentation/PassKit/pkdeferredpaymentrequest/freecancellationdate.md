# freeCancellationDate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, strong, nullable) NSDate * freeCancellationDate;
```

## Discussion

If you set [`freeCancellationDate`](./freecancellationdate.md), you need to set [`freeCancellationDateTimeZone`](./freecancellationdatetimezone.md) as well.

## See Also

### Describing a deferred payment
- [var billingAgreement: String?](./billingagreement.md)
  The localized billing agreement the framework displays to the user prior to payment authorization.
- [var paymentDescription: String](./paymentdescription.md)
  A description of the deferred payment.
- [var freeCancellationDateTimeZone: TimeZone?](./freecancellationdatetimezone.md)
  The time zone at the destination location of the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdeferredpaymentrequest/freecancellationdate)*