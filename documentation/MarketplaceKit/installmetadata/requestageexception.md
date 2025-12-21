# requestAgeException

**Framework**: MarketplaceKit  
**Kind**: property

A Boolean value that indicates whether the person needs approval to install the app.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
var requestAgeException: Bool
```

## Mentions

- [Providing age-rating appropriate content](providing-age-rating-appropriate-content.md)

#### Discussion

Set this property to `true` if the app to install has an age rating beyond the maximum allowed for the device (see [`maximumAllowedAgeRating`](applibrary/maximumallowedagerating.md)). Instead of installing the app, the framework presents a sheet that enables the person to send an installation exception request to the parent or guardian. For more information, see [`Providing age-rating appropriate content`](providing-age-rating-appropriate-content.md).

If your app sets this property to `true` when it’s not needed, the framework throws [`MarketplaceKitError.ageRatingExceptionNotNeeded`](marketplacekiterror/ageratingexceptionnotneeded.md). Alternatively, if your app fails to set this property to `true` when it is needed, the framework throws  [`MarketplaceKitError.cancelled`](marketplacekiterror/cancelled.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/installmetadata/requestageexception)*