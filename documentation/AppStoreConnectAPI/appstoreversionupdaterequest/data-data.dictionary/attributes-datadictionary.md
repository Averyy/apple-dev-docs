# AppStoreVersionUpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes whose values you’re changing as part of the update request.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppStoreVersionUpdateRequest.Data.Attributes
```

## Mentions

- [Configuring alternative marketplaces and alternative marketplace apps](configuring-alternative-marketplaces-and-alternative-marketplace-apps.md)

## Properties

- `copyright` (string)
- `earliestReleaseDate` (date-time)
- `releaseType` (string)
- `versionString` (string)
- `downloadable` (boolean)
- `reviewType` (string): `NOTARIZATION` is alternative app marketplace distribution. All eligible app versions default to both `APP_STORE` and `NOTARIZATION.` An app can be distributed on either or both.
- `usesIdfa` (boolean)

## See Also

- [object AppStoreVersionUpdateRequest.Data.Relationships](appstoreversionupdaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The data and links that describe the relationship between the resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstoreversionupdaterequest/data-data.dictionary/attributes-data.dictionary)*