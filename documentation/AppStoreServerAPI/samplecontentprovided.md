# sampleContentProvided

**Framework**: App Store Server API  
**Kind**: typealias

A Boolean value that indicates whether you provided, prior to its purchase, a free sample or trial of the content, or information about its functionality.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
boolean sampleContentProvided
```

#### Discussion

Set this value to `true` if you provided any of the following prior to the customer’s purchase:

- A free sample or free trial of the purchased content
- Information about the content and how it works, such as expected game play

Set this value to `false` otherwise.

## See Also

- [type customerConsented](customerconsented.md)
  A Boolean value that indicates whether the customer consented to provide consumption data to the App Store.
- [type consumptionPercentage](consumptionpercentage.md)
  An integer that indicates the percentage, in milliunits, of the In-App Purchase the customer consumed.
- [type deliveryStatus](deliverystatus.md)
  A value that indicates whether the app successfully delivered an In-App Purchase that works properly.
- [type refundPreference](refundpreference.md)
  A value that indicates your preferred outcome for the refund request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/samplecontentprovided)*