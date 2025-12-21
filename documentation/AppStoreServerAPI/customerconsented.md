# customerConsented

**Framework**: App Store Server API  
**Kind**: typealias

A Boolean value that indicates whether the customer consented to provide consumption data to the App Store.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
boolean customerConsented
```

#### Discussion

Set this field to `true` if the customer provided consent to send the App Store the consumption data related to their refund request, including all the data you provide in the [`ConsumptionRequest`](consumptionrequest.md) or [`ConsumptionRequestV1`](consumptionrequestv1.md) request body. If not, don’t respond to the `CONSUMPTION_REQUEST` notification.

## See Also

- [type consumptionPercentage](consumptionpercentage.md)
  An integer that indicates the percentage, in milliunits, of the In-App Purchase the customer consumed.
- [type deliveryStatus](deliverystatus.md)
  A value that indicates whether the app successfully delivered an In-App Purchase that works properly.
- [type refundPreference](refundpreference.md)
  A value that indicates your preferred outcome for the refund request.
- [type sampleContentProvided](samplecontentprovided.md)
  A Boolean value that indicates whether you provided, prior to its purchase, a free sample or trial of the content, or information about its functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/customerconsented)*