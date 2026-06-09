# BetaAppLocalization

**Framework**: App Store Connect API  
**Kind**: dictionary

The localized feedback URL, marketing URL, and privacy policy URL shown to TestFlight testers for a specific language.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaAppLocalization
```

## Topics

### Objects
- [object BetaAppLocalization.Attributes](betaapplocalization/attributes-data.dictionary.md)
  Attributes that describe a Beta App Localizations resource.
- [object BetaAppLocalization.Relationships](betaapplocalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (BetaAppLocalization.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (BetaAppLocalization.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [object BetaAppLocalizationCreateRequest](betaapplocalizationcreaterequest.md)
  The request body you use to create a Beta App Localization.
- [object BetaAppLocalizationResponse](betaapplocalizationresponse.md)
  The response body for endpoints that create, read, or modify localized TestFlight app metadata.
- [object BetaAppLocalizationsWithoutIncludesResponse](betaapplocalizationswithoutincludesresponse.md)
  A response containing a list of TestFlight app localizations, without related resources.
- [object BetaAppLocalizationUpdateRequest](betaapplocalizationupdaterequest.md)
  The request body you use to update a Beta App Localization.
- [object BetaAppLocalizationsResponse](betaapplocalizationsresponse.md)
  The response body for endpoints that list localized TestFlight app metadata entries.
- [object BetaAppLocalizationAppLinkageResponse](betaapplocalizationapplinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaapplocalization)*