# BetaAppLocalizationsWithoutIncludesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of TestFlight app localizations, without related resources.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object BetaAppLocalizationsWithoutIncludesResponse
```

## Properties

- `data` ([BetaAppLocalization]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object BetaAppLocalization](betaapplocalization.md)
  The localized feedback URL, marketing URL, and privacy policy URL shown to TestFlight testers for a specific language.
- [object BetaAppLocalizationCreateRequest](betaapplocalizationcreaterequest.md)
  The request body you use to create a Beta App Localization.
- [object BetaAppLocalizationResponse](betaapplocalizationresponse.md)
  The response body for endpoints that create, read, or modify localized TestFlight app metadata.
- [object BetaAppLocalizationUpdateRequest](betaapplocalizationupdaterequest.md)
  The request body you use to update a Beta App Localization.
- [object BetaAppLocalizationsResponse](betaapplocalizationsresponse.md)
  The response body for endpoints that list localized TestFlight app metadata entries.
- [object BetaAppLocalizationAppLinkageResponse](betaapplocalizationapplinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaapplocalizationswithoutincludesresponse)*