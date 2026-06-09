# BetaAppLocalizationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list localized TestFlight app metadata entries.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaAppLocalizationsResponse
```

## Properties

- `data` ([BetaAppLocalization]) *(required)*: The resource data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.
- `included` ([App])

## See Also

- [List beta app localizations](get-v1-betaapplocalizations.md)
  Find and list beta app localizations for all apps and locales.
- [object BetaAppLocalization](betaapplocalization.md)
  The localized feedback URL, marketing URL, and privacy policy URL shown to TestFlight testers for a specific language.
- [object BetaAppLocalizationCreateRequest](betaapplocalizationcreaterequest.md)
  The request body you use to create a Beta App Localization.
- [object BetaAppLocalizationResponse](betaapplocalizationresponse.md)
  The response body for endpoints that create, read, or modify localized TestFlight app metadata.
- [object BetaAppLocalizationsWithoutIncludesResponse](betaapplocalizationswithoutincludesresponse.md)
  A response containing a list of TestFlight app localizations, without related resources.
- [object BetaAppLocalizationUpdateRequest](betaapplocalizationupdaterequest.md)
  The request body you use to update a Beta App Localization.
- [object BetaAppLocalizationAppLinkageResponse](betaapplocalizationapplinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaapplocalizationsresponse)*