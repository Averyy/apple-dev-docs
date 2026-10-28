# billingAgreement

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

The localized billing agreement the framework displays to the user prior to payment authorization.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
DOMString billingAgreement;
```

## Discussion

This may include additional details about the cancellation period or penalties for late cancellation. This value is optional.

## See Also

### Describing a deferred payment
- [paymentDescription](./paymentdescription.md)
  A description of the deferred payment.
- [freeCancellationDate](./freecancellationdate.md)
  The time zone at the destination location of the payment.
- [freeCancellationDateTimeZone](./freecancellationdatetimezone.md)
  The time zone at the destination location of the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaydeferredpaymentrequest/billingagreement)*