# consumptionPercentage

**Framework**: App Store Server API  
**Kind**: typealias

An integer that indicates the percentage, in milliunits, of the In-App Purchase the customer consumed.

**Availability**:
- App Store Server API 1.19+

## Declaration

```swift
int32 consumptionPercentage
```

#### Discussion

You can provide a consumption percentage in the [`ConsumptionRequest`](consumptionrequest.md) object when you call [`Send Consumption Information`](send-consumption-information.md) for consumable and non-consumable In-App Purchases and non-renewing subscriptions. The consumption percentage represents the portion of the product that the customer consumed.

The consumption percentage you provide is one of a variety of factors that the App Store uses to inform its refund decisions. The final refund percentage may differ from the value you provide.

Consider the following when you use this field:

- If you select `GRANT_PRORATED` for the [`refundPreference`](refundpreference.md) field, you need to provide a `consumptionPercentage` greater than `0` and less than `100000`.
- If the [`deliveryStatus`](deliverystatus.md) value isn’t `DELIVERED`, set the `consumptionPercentage` to `0`; otherwise, the request fails with an `HTTP 400` error [`UndeliveredConsumptionPercentageNonZeroError`](undeliveredconsumptionpercentagenonzeroerror.md).
- Don’t provide a consumption percentage for auto-renewable subscriptions, otherwise the request fails with an `HTTP 400` error [`ConsumptionPercentageAutoRenewableSubscriptionError`](consumptionpercentageautorenewablesubscriptionerror.md). The system automatically calculates the consumption percentage for auto-renewable subscriptions based on elapsed time.

Use the consumption percentage to indicate the amount of the product the customer consumed. The percentage value allows for three decimal places of precision, and is expressed as an integer, in milliunits. The following table shows several examples of valid consumption percentages, and their milliunit equivalents:

| Percentage | Integer equivalent, in milliunits |
| --- | --- |
| 67.932% | 67932 |
| 0.015% | 15 |
| 40% | 40000 |
| 100% | 100000 |

For example, if a transaction contains a quantity of two consumable In-App Purchases, and the customer fully consumed one of them, the `consumptionPercentage` is `50000`, which represents 50%.

If the system approves a prorated refund, the [`revocationPercentage`](revocationpercentage.md) field in the [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md) contains the revoked percentage of the transaction.

## See Also

- [type customerConsented](customerconsented.md)
  A Boolean value that indicates whether the customer consented to provide consumption data to the App Store.
- [type deliveryStatus](deliverystatus.md)
  A value that indicates whether the app successfully delivered an In-App Purchase that works properly.
- [type refundPreference](refundpreference.md)
  A value that indicates your preferred outcome for the refund request.
- [type sampleContentProvided](samplecontentprovided.md)
  A Boolean value that indicates whether you provided, prior to its purchase, a free sample or trial of the content, or information about its functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/consumptionpercentage)*