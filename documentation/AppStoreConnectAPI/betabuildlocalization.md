# BetaBuildLocalization

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a Beta Build Localizations resource.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaBuildLocalization
```

## Topics

### Objects
- [object BetaBuildLocalization.Attributes](betabuildlocalization/attributes-data.dictionary.md)
  Attributes that describe a Beta Build Localizations resource.
- [object BetaBuildLocalization.Relationships](betabuildlocalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (BetaBuildLocalization.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (BetaBuildLocalization.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

- [object BetaBuildLocalizationResponse](betabuildlocalizationresponse.md)
  A response that contains a single Beta Build Localizations resource.
- [object BetaBuildLocalizationsWithoutIncludesResponse](betabuildlocalizationswithoutincludesresponse.md)
- [object BetaBuildLocalizationCreateRequest](betabuildlocalizationcreaterequest.md)
  The request body you use to create a Beta Build Localization.
- [object BetaBuildLocalizationUpdateRequest](betabuildlocalizationupdaterequest.md)
  The request body you use to update a Beta Build Localization.
- [object BetaBuildLocalizationsResponse](betabuildlocalizationsresponse.md)
  A response that contains a list of Beta Build Localization resources.
- [object BetaBuildLocalizationBuildLinkageResponse](betabuildlocalizationbuildlinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betabuildlocalization)*