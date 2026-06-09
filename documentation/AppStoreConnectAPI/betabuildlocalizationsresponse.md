# BetaBuildLocalizationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list localized TestFlight build metadata entries.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaBuildLocalizationsResponse
```

## Properties

- `data` ([BetaBuildLocalization]) *(required)*: The resource data.
- `included` ([Build])
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.

## See Also

- [List beta build localizations](get-v1-betabuildlocalizations.md)
  Find and list beta build localizations currently associated with apps.
- [object BetaBuildLocalization](betabuildlocalization.md)
  The localized ‘What’s New’ text shown to TestFlight testers in a specific language for a build.
- [object BetaBuildLocalizationResponse](betabuildlocalizationresponse.md)
  The response body for endpoints that create, read, or modify localized TestFlight build metadata.
- [object BetaBuildLocalizationsWithoutIncludesResponse](betabuildlocalizationswithoutincludesresponse.md)
  A response containing a list of TestFlight build localizations, without related resources.
- [object BetaBuildLocalizationCreateRequest](betabuildlocalizationcreaterequest.md)
  The request body you use to create a Beta Build Localization.
- [object BetaBuildLocalizationUpdateRequest](betabuildlocalizationupdaterequest.md)
  The request body you use to update a Beta Build Localization.
- [object BetaBuildLocalizationBuildLinkageResponse](betabuildlocalizationbuildlinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betabuildlocalizationsresponse)*