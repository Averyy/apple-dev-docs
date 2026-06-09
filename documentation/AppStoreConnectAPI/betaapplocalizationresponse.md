# BetaAppLocalizationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify localized TestFlight app metadata.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaAppLocalizationResponse
```

## Properties

- `data` (BetaAppLocalization) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.
- `included` ([App])

## See Also

- [Create a beta app localization](post-v1-betaapplocalizations.md)
  Create localized descriptive information for an app.
- [object BetaAppLocalization](betaapplocalization.md)
  The localized feedback URL, marketing URL, and privacy policy URL shown to TestFlight testers for a specific language.
- [object BetaAppLocalizationCreateRequest](betaapplocalizationcreaterequest.md)
  The request body you use to create a Beta App Localization.
- [object BetaAppLocalizationsWithoutIncludesResponse](betaapplocalizationswithoutincludesresponse.md)
  A response containing a list of TestFlight app localizations, without related resources.
- [object BetaAppLocalizationUpdateRequest](betaapplocalizationupdaterequest.md)
  The request body you use to update a Beta App Localization.
- [object BetaAppLocalizationsResponse](betaapplocalizationsresponse.md)
  The response body for endpoints that list localized TestFlight app metadata entries.
- [object BetaAppLocalizationAppLinkageResponse](betaapplocalizationapplinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaapplocalizationresponse)*