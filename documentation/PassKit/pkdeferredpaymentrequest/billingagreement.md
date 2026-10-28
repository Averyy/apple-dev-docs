# billingAgreement

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The localized billing agreement the framework displays to the user prior to payment authorization.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- visionOS 1.0+

## Declaration

```swift
var billingAgreement: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * billingAgreement;
```

## Discussion

This may include additional details about the cancellation period or penalties for late cancellation. This value is optional.

## See Also

### Describing a deferred payment
- [var freeCancellationDate: Date?](./freecancellationdate.md)
  The date before which you must cancel a deferred payment without incurring any cancellation charges.
- [var paymentDescription: String](./paymentdescription.md)
  A description of the deferred payment.
- [var freeCancellationDateTimeZone: TimeZone?](./freecancellationdatetimezone.md)
  The time zone at the destination location of the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdeferredpaymentrequest/billingagreement)*