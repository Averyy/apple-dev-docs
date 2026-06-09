# BetaLicenseAgreement

**Framework**: App Store Connect API  
**Kind**: dictionary

The custom terms and conditions presented to TestFlight testers before they begin testing an app.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaLicenseAgreement
```

## Topics

### Objects
- [object BetaLicenseAgreement.Attributes](betalicenseagreement/attributes-data.dictionary.md)
  Attributes that describe a Beta License Agreements resource.
- [object BetaLicenseAgreement.Relationships](betalicenseagreement/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (BetaLicenseAgreement.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (BetaLicenseAgreement.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object BetaLicenseAgreementUpdateRequest](betalicenseagreementupdaterequest.md)
  The request body you use to update a Beta License Agreement.
- [object BetaLicenseAgreementWithoutIncludesResponse](betalicenseagreementwithoutincludesresponse.md)
  A response containing a single TestFlight license agreement, without related resources.
- [object BetaLicenseAgreementsResponse](betalicenseagreementsresponse.md)
  The response body for endpoints that list TestFlight license agreements.
- [object BetaLicenseAgreementResponse](betalicenseagreementresponse.md)
  The response body for endpoints that read or modify the TestFlight license agreement for an app.
- [object BetaLicenseAgreementAppLinkageResponse](betalicenseagreementapplinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betalicenseagreement)*