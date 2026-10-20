# AppInfo.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe an App Infos resource.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```
object AppInfo.Attributes
```

## Mentions

- [App Store Connect API 3.3 release notes](../app-store-connect-api-3-3-release-notes.md)
- [App Store Connect API 3.7 release notes](../app-store-connect-api-3-7-release-notes.md)
- [App Store Connect API 3.8 release notes](../app-store-connect-api-3-8-release-notes.md)
- [App Store Connect API 4.2 release notes](../app-store-connect-api-4-2-release-notes.md)

##### Discussion

> **Note**: For more information about `australiaAgeRating` and `koreaAgeRating`, see [Age Ratings in App Store Connect Help](https://developer.apple.com/help/app-store-connect/reference/age-ratings).

## Properties

- `appStoreAgeRating` (AppStoreAgeRating): The app’s age rating as it appears on the App Store for all platforms.
- `appStoreState` (AppStoreVersionState): This attribute is deprecated. Use `state` instead.
- `australiaAgeRating` (string) *(deprecated)*: **Allowed Values**: `FIFTEEN`, `EIGHTEEN`
- `brazilAgeRating` (BrazilAgeRating): This attribute is deprecated. Use `brazilAgeRatingV2` instead.
- `brazilAgeRatingV2` (string) *(deprecated)*: The app’s age rating as it appears on the App Store in Brazil for all platforms.

  **Allowed Values**: `SELF_RATED_L`, `SELF_RATED_TEN`, `SELF_RATED_TWELVE`, `SELF_RATED_FOURTEEN`, `SELF_RATED_SIXTEEN`, `SELF_RATED_EIGHTEEN`, `OFFICIAL_L`, `OFFICIAL_TEN`, `OFFICIAL_TWELVE`, `OFFICIAL_FOURTEEN`, `OFFICIAL_SIXTEEN`, `OFFICIAL_EIGHTEEN`
- `franceAgeRating` (string) *(deprecated)*: **Allowed Values**: `EIGHTEEN`
- `koreaAgeRating` (string) *(deprecated)*: **Allowed Values**: `ALL`, `TWELVE`, `FIFTEEN`, `NINETEEN`, `NOT_APPLICABLE`
- `state` (string): **Allowed Values**: `ACCEPTED`, `DEVELOPER_REJECTED`, `IN_REVIEW`, `PENDING_RELEASE`, `PREPARE_FOR_SUBMISSION`, `READY_FOR_DISTRIBUTION`, `READY_FOR_REVIEW`, `REJECTED`, `REPLACED_WITH_NEW_INFO`, `WAITING_FOR_REVIEW`

## See Also

### Objects
- [object AppInfo.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appinfo/attributes-data.dictionary)*