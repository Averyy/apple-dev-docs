# refundPreference

**Framework**: App Store Server API  
**Kind**: typealias

A value that indicates your preferred outcome for the refund request.

**Availability**:
- App Store Server API 1.19+

## Declaration

```swift
string refundPreference
```

#### Discussion

Use these values in the `refundPreference` field of a [`ConsumptionRequest`](consumptionrequest.md).

The following constraints apply to the `GRANT_PRORATED` option:

- If the product is a consumable or non-consumable In-App Purchase or a non-renewing subscription, you may include a [`consumptionPercentage`](consumptionpercentage.md) value in the `ConsumptionRequest`.
- If the product is an auto-renewable subscription, don’t include a [`consumptionPercentage`](consumptionpercentage.md) value in the `ConsumptionRequest`. The system calculates the consumption automatically for auto-renewable subscriptions.

Your refund preference is one of a variety of factors that the App Store uses to inform its refund decisions.

## See Also

- [type customerConsented](customerconsented.md)
  A Boolean value that indicates whether the customer consented to provide consumption data to the App Store.
- [type consumptionPercentage](consumptionpercentage.md)
  An integer that indicates the percentage, in milliunits, of the In-App Purchase the customer consumed.
- [type deliveryStatus](deliverystatus.md)
  A value that indicates whether the app successfully delivered an In-App Purchase that works properly.
- [type sampleContentProvided](samplecontentprovided.md)
  A Boolean value that indicates whether you provided, prior to its purchase, a free sample or trial of the content, or information about its functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/refundpreference)*