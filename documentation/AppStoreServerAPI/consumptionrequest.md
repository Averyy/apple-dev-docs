# ConsumptionRequest

**Framework**: App Store Server API  
**Kind**: dictionary

The request body that contains consumption information for an In-App Purchase.

**Availability**:
- App Store Server API 1.19+

## Declaration

```swift
object ConsumptionRequest
```

#### Discussion

Use `ConsumptionRequest` to provide information about the customer’s In-App Purchase when you call the [`Send Consumption Information`](send-consumption-information.md) endpoint.

> **Note**: The App Store server rejects requests that have a [`customerConsented`](customerconsented.md) value other than `true` by returning an `HTTP 400` error with an [`InvalidCustomerConsentedError`](invalidcustomerconsentederror.md).

You can provide consumption information for any type of product: consumable, non-consumable, non-renewing subscription, and auto-renewable subscription.

Consider the following constraints when providing an optional [`refundPreference`](consumptionrequest/refundpreference.md):

- The system supports the `GRANT_FULL` and `DECLINE` values for all product types.
- If you choose `GRANT_PRORATED` for an auto-renewable subscription, don’t include a [`consumptionPercentage`](consumptionrequest/consumptionpercentage.md). The system automatically calculates the percentage.

If the [`deliveryStatus`](consumptionrequest/deliverystatus.md) isn’t `DELIVERED`, set the `consumptionPercentage` to `0`; otherwise the request fails with an error.

## Topics

### Consumption data types
- [type customerConsented](customerconsented.md)
  A Boolean value that indicates whether the customer consented to provide consumption data to the App Store.
- [type consumptionPercentage](consumptionpercentage.md)
  An integer that indicates the percentage, in milliunits, of the In-App Purchase the customer consumed.
- [type deliveryStatus](deliverystatus.md)
  A value that indicates whether the app successfully delivered an In-App Purchase that works properly.
- [type refundPreference](refundpreference.md)
  A value that indicates your preferred outcome for the refund request.
- [type sampleContentProvided](samplecontentprovided.md)
  A Boolean value that indicates whether you provided, prior to its purchase, a free sample or trial of the content, or information about its functionality.

## See Also

- [Send Consumption Information](send-consumption-information.md)
  Send consumption information about an In-App Purchase to the App Store after your server receives a consumption request notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/consumptionrequest)*