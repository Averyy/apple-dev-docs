# presentAgeExceptionApproveInPersonSheet()

**Framework**: MarketplaceKit  
**Kind**: method  
**Role**: Instance Method

Presents a sheet that enables a parent or guardian to approve age-exception requests.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
@MainActor
final func presentAgeExceptionApproveInPersonSheet() async throws
```

## Mentions

- [Providing age-rating appropriate content](../../providing-age-rating-appropriate-content.md)

## Discussion

Call this method when a person wants to display a sheet that enables a parent or guardian to review an installation exception request in person. For more information, see [Providing age-rating appropriate content](../../providing-age-rating-appropriate-content.md).

The framework throws [`MarketplaceKitError.missingAgeRatingExceptionRequest`](../../marketplacekiterror/missingageratingexceptionrequest.md) if your app calls this method when there’s no age-rating exception requests for the app in the [`currentAgeExceptionRequests()`](../currentageexceptionrequests%28%29.md) list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/app/presentageexceptionapproveinpersonsheet())*