# RetentionOfferUpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes whose values you’re changing as part of the update request.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionOfferUpdateRequest.Data.Attributes
```

## Properties

- `customerEligibilityPaidSubscriptionDurationInMonths` (integer): The minimum number of months of paid subscription that makes a person eligible for the offer. Possible values are 1 to 24, 36, 48, and 60.
- `customerEligibilityWaitBetweenOffersInMonths` (integer): The number of months a person waits before they can redeem another retention offer for the same subscription. Possible values are 2 to 24.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionofferupdaterequest/data-data.dictionary/attributes-data.dictionary)*