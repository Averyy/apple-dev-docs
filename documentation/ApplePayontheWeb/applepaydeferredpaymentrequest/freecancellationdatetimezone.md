# freeCancellationDateTimeZone

**Framework**: Apple Pay on the Web  
**Kind**: property

The time zone at the destination location of the payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
DOMString freeCancellationDateTimeZone;
```

#### Discussion

For a hotel booking, for example, this refers to the local time zone of the hotel. On the payment sheet, this is the time zone the framework uses to format the cancellation date. If you set the `freeCancellationDateTimeZone` date, you need to set [`freeCancellationDate`](applepaydeferredpaymentrequest/freecancellationdate.md) as well.

## See Also

- [billingAgreement](applepaydeferredpaymentrequest/billingagreement.md)
  The localized billing agreement the framework displays to the user prior to payment authorization.
- [paymentDescription](applepaydeferredpaymentrequest/paymentdescription.md)
  A description of the deferred payment.
- [freeCancellationDate](applepaydeferredpaymentrequest/freecancellationdate.md)
  The time zone at the destination location of the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaydeferredpaymentrequest/freecancellationdatetimezone)*