# AppStoreVersion.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe an App Store Versions resource.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppStoreVersion.Attributes
```

## Mentions

- [App Store Connect API 3.3 release notes](app-store-connect-api-3-3-release-notes.md)
- [App Store Connect API 3.7 release notes](app-store-connect-api-3-7-release-notes.md)

## Properties

- `platform` (Platform)
- `appStoreState` (AppStoreVersionState): This attribute is deprecated. Use [`AppVersionState`](appversionstate.md) instead.
- `copyright` (string)
- `earliestReleaseDate` (date-time)
- `releaseType` (string)
- `versionString` (string)
- `createdDate` (date-time)
- `downloadable` (boolean)
- `appVersionState` (AppVersionState)
- `reviewType` (string)
- `usesIdfa` (boolean)

## See Also

- [object AppStoreVersion.Relationships](appstoreversion/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstoreversion/attributes-data.dictionary)*