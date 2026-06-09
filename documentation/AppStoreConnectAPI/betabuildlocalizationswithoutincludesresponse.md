# BetaBuildLocalizationsWithoutIncludesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of TestFlight build localizations, without related resources.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object BetaBuildLocalizationsWithoutIncludesResponse
```

## Properties

- `data` ([BetaBuildLocalization]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object BetaBuildLocalization](betabuildlocalization.md)
  The localized ‘What’s New’ text shown to TestFlight testers in a specific language for a build.
- [object BetaBuildLocalizationResponse](betabuildlocalizationresponse.md)
  The response body for endpoints that create, read, or modify localized TestFlight build metadata.
- [object BetaBuildLocalizationCreateRequest](betabuildlocalizationcreaterequest.md)
  The request body you use to create a Beta Build Localization.
- [object BetaBuildLocalizationUpdateRequest](betabuildlocalizationupdaterequest.md)
  The request body you use to update a Beta Build Localization.
- [object BetaBuildLocalizationsResponse](betabuildlocalizationsresponse.md)
  The response body for endpoints that list localized TestFlight build metadata entries.
- [object BetaBuildLocalizationBuildLinkageResponse](betabuildlocalizationbuildlinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betabuildlocalizationswithoutincludesresponse)*