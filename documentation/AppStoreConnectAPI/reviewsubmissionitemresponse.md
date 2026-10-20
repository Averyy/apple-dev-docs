# ReviewSubmissionItemResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that create, read, or modify a single review submission item.

**Availability**:
- App Store Connect API 1.7+

## Declaration

```
object ReviewSubmissionItemResponse
```

## Properties

- `data` (ReviewSubmissionItem) *(required)*
- `included` ([*]): **Allowed Types**: `AppAssetLibraryImage`, `AppAssetLibraryVideo`, `AppCustomProductPageVersion`, `AppEvent`, `AppStoreVersionExperiment`, `AppStoreVersion`, `BackgroundAssetVersion`, `GameCenterAchievementVersionV2`, `GameCenterActivityVersion`, `GameCenterChallengeVersion`, `GameCenterLeaderboardSetVersionV2`, `GameCenterLeaderboardVersionV2`, `InAppPurchaseVersion`, `SubscriptionGroupVersion`, `SubscriptionVersion`
- `links` (DocumentLinks) *(required)*

## See Also

### Objects
- [object ReviewSubmissionItemCreateRequest](./reviewsubmissionitemcreaterequest.md)
  The request body you use to create a review submission item.
- [object ReviewSubmissionItemUpdateRequest](./reviewsubmissionitemupdaterequest.md)
  The request body you use to update a review submission item update request.
- [object ReviewSubmissionItemsResponse](./reviewsubmissionitemsresponse.md)
  The response body for endpoints that list items in a review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/reviewsubmissionitemresponse)*