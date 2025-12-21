# MarketplaceKitError.missingAgeRatingExceptionRequest

**Framework**: MarketplaceKit  
**Kind**: case

An error that indicates the app needs to request an age-rating exception.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
case missingAgeRatingExceptionRequest
```

## Mentions

- [Providing age-rating appropriate content](providing-age-rating-appropriate-content.md)

#### Discussion

The framework throws this error if your app calls [`presentAgeExceptionApproveInPersonSheet()`](applibrary/app/presentageexceptionapproveinpersonsheet().md) when there’s no age-rating exception requests for the app in the [`currentAgeExceptionRequests()`](applibrary/currentageexceptionrequests().md) list.

## See Also

- [MarketplaceKitError.ageRatingExceptionNotNeeded](marketplacekiterror/ageratingexceptionnotneeded.md)
  An error that indicates the app requests an unnecessary age-rating exception.
- [MarketplaceKitError.ratingRestricted](marketplacekiterror/ratingrestricted.md)
  An error that indicates the requested app’s age rating is beyond that allowed for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplacekiterror/missingageratingexceptionrequest)*