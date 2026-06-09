# BetaBuildLocalizationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify localized TestFlight build metadata.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaBuildLocalizationResponse
```

## Properties

- `data` (BetaBuildLocalization) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.
- `included` ([Build])

## See Also

- [Create a beta build localization](post-v1-betabuildlocalizations.md)
  Create localized What’s New text for a build.
- [object BetaBuildLocalization](betabuildlocalization.md)
  The localized ‘What’s New’ text shown to TestFlight testers in a specific language for a build.
- [object BetaBuildLocalizationsWithoutIncludesResponse](betabuildlocalizationswithoutincludesresponse.md)
  A response containing a list of TestFlight build localizations, without related resources.
- [object BetaBuildLocalizationCreateRequest](betabuildlocalizationcreaterequest.md)
  The request body you use to create a Beta Build Localization.
- [object BetaBuildLocalizationUpdateRequest](betabuildlocalizationupdaterequest.md)
  The request body you use to update a Beta Build Localization.
- [object BetaBuildLocalizationsResponse](betabuildlocalizationsresponse.md)
  The response body for endpoints that list localized TestFlight build metadata entries.
- [object BetaBuildLocalizationBuildLinkageResponse](betabuildlocalizationbuildlinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betabuildlocalizationresponse)*