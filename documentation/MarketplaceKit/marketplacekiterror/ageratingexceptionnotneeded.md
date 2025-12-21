# MarketplaceKitError.ageRatingExceptionNotNeeded

**Framework**: MarketplaceKit  
**Kind**: case

An error that indicates the app requests an unnecessary age-rating exception.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
case ageRatingExceptionNotNeeded
```

## Mentions

- [Providing age-rating appropriate content](providing-age-rating-appropriate-content.md)

#### Discussion

The framework throws this error if your app sets [`requestAgeException`](installmetadata/requestageexception.md) to `true` when it’s not needed — that is, when the app to install has an age rating that’s within the allowed range for the device (as determined by [`maximumAllowedAgeRating`](applibrary/maximumallowedagerating.md)).

## See Also

- [MarketplaceKitError.missingAgeRatingExceptionRequest](marketplacekiterror/missingageratingexceptionrequest.md)
  An error that indicates the app needs to request an age-rating exception.
- [MarketplaceKitError.ratingRestricted](marketplacekiterror/ratingrestricted.md)
  An error that indicates the requested app’s age rating is beyond that allowed for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplacekiterror/ageratingexceptionnotneeded)*