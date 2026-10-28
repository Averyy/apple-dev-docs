# freeCancellationDate

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

The time zone at the destination location of the payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
Date freeCancellationDate;
```

## Discussion

If you set `freeCancellationDate`, you need to set [`freeCancellationDateTimeZone`](./freecancellationdatetimezone.md) as well.

## See Also

### Describing a deferred payment
- [billingAgreement](./billingagreement.md)
  The localized billing agreement the framework displays to the user prior to payment authorization.
- [paymentDescription](./paymentdescription.md)
  A description of the deferred payment.
- [freeCancellationDateTimeZone](./freecancellationdatetimezone.md)
  The time zone at the destination location of the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaydeferredpaymentrequest/freecancellationdate)*