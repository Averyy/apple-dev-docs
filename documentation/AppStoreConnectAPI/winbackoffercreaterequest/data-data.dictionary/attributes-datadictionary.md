# WinBackOfferCreateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a winback offer resource.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object WinBackOfferCreateRequest.Data.Attributes
```

## Mentions

- [Creating and configuring win-back offers](creating-and-configuring-win-back-offers.md)

## Properties

- `customerEligibilityPaidSubscriptionDurationInMonths` (integer) *(required)*: How long a customer was a subscriber. Possible values: - **`1-24`**: 1 to 24 months, as integers
- **`36`**: 3 years
- **`48`**: 4 years
- **`60`**: 5 years
- `customerEligibilityTimeSinceLastSubscribedInMonths` (IntegerRange) *(required)*: How long since the subscribe last had an active subscription.
- `customerEligibilityWaitBetweenOffersInMonths` (integer): How long since the subscribe last had an active subscription.
- `duration` (SubscriptionOfferDuration) *(required)*: The length of time for the offer period.
- `endDate` (date): Minimum length for a win-back offer is 3 days.
- `offerId` (string) *(required)*: (Required) string of alphanumeric characters, periods, and underscores, up to 100 characters. Use a unique value that you have not used for a promotional offer, offer code, or introductory offer, when you create your win-back offer.
- `offerMode` (SubscriptionOfferMode) *(required)*: (Required) Describes how payment is configured for a win-back offer.
- `periodCount` (integer) *(required)*: (Required) The number of subscription duration intervals.
- `priority` (string) *(required)*: Select how this offer ranks among your other offers and in-app events. `HIGH` priority offers will appear above other offers and events on your appʼs product page.
- `promotionIntent` (string): You can promote this offer on your App Store product page. Promoted offers can also display in search results and may be featured on the Today, Games, and Apps tabs. If your win-back offer is live and `promotionIntent` is set to `USE_AUTO_GENERATED_ASSETS` you need to delete the win-back offer in order to remove it from promotion.
- `referenceName` (string) *(required)*: A string of alphanumeric characters, spaces, periods, and underscores, up to 65 characters. Use a unique value that you have not used for a promotional offer, offer code, or introductory offer, when you create your win-back offer.
- `startDate` (date) *(required)*: First available date is today + 1 day.

## See Also

- [object WinBackOfferCreateRequest.Data.Relationships](winbackoffercreaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/winbackoffercreaterequest/data-data.dictionary/attributes-data.dictionary)*