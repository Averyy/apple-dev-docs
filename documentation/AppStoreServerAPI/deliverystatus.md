# deliveryStatus

**Framework**: App Store Server API  
**Kind**: typealias

A value that indicates whether the app successfully delivered an In-App Purchase that works properly.

**Availability**:
- App Store Server API 1.19+

## Declaration

```swift
string deliveryStatus
```

#### Discussion

Use these delivery status values in the [`ConsumptionRequest`](consumptionrequest.md) request body.

> **Note**: If the delivery status isn’t `DELIVERED`, set the [`consumptionPercentage`](consumptionpercentage.md) to `0`; otherwise, the request fails with an error.

## See Also

- [type customerConsented](customerconsented.md)
  A Boolean value that indicates whether the customer consented to provide consumption data to the App Store.
- [type consumptionPercentage](consumptionpercentage.md)
  An integer that indicates the percentage, in milliunits, of the In-App Purchase the customer consumed.
- [type refundPreference](refundpreference.md)
  A value that indicates your preferred outcome for the refund request.
- [type sampleContentProvided](samplecontentprovided.md)
  A Boolean value that indicates whether you provided, prior to its purchase, a free sample or trial of the content, or information about its functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/deliverystatus)*