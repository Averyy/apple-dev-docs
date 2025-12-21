# init(account:appleItemID:alternativeDistributionPackage:isUpdate:appShareURL:requestAgeException:)

**Framework**: MarketplaceKit  
**Kind**: init

Initializes an install metadata object with the given app information and exception request indicator.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
init(account: String, appleItemID: AppleItemID, alternativeDistributionPackage: URL, isUpdate: Bool, appShareURL: URL?, requestAgeException: Bool = false)
```

## Mentions

- [Providing age-rating appropriate content](providing-age-rating-appropriate-content.md)

#### Discussion

If the identifier refers to an app that has an age rating beyond the maximum allowed for the device (see [`maximumAllowedAgeRating`](applibrary/maximumallowedagerating.md)), pass `true` for the `requestAgeException` argument.

If your app sets the `requestAgeException` argument to `true` when it’s not needed, the framework throws [`MarketplaceKitError.ageRatingExceptionNotNeeded`](marketplacekiterror/ageratingexceptionnotneeded.md). Alternatively, if your app fails to set the `requestAgeException` argument to `true` when it is needed, the framework throws  [`MarketplaceKitError.cancelled`](marketplacekiterror/cancelled.md).

## See Also

- [init(account: String, appleItemID: AppleItemID, alternativeDistributionPackage: URL, isUpdate: Bool)](installmetadata/init(account:appleitemid:alternativedistributionpackage:isupdate:).md)
  Initializes an install metadata object with the given app information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/installmetadata/init(account:appleitemid:alternativedistributionpackage:isupdate:appshareurl:requestageexception:))*