# EndUserLicenseAgreement

**Framework**: App Store Connect API  
**Kind**: dictionary

A custom end-user license agreement (EULA) for an app, targeting specific territories where it applies.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object EndUserLicenseAgreement
```

## Topics

### Objects
- [object EndUserLicenseAgreement.Attributes](enduserlicenseagreement/attributes-data.dictionary.md)
  Attributes that describe an End User License Agreements resource.
- [object EndUserLicenseAgreement.Relationships](enduserlicenseagreement/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (EndUserLicenseAgreement.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (EndUserLicenseAgreement.Relationships)
- `type` (string) *(required)*

## See Also

- [object EndUserLicenseAgreementCreateRequest](enduserlicenseagreementcreaterequest.md)
  The request body you use to create an End User License Agreement.
- [object EndUserLicenseAgreementUpdateRequest](enduserlicenseagreementupdaterequest.md)
  The request body you use to update an End User License Agreement.
- [object EndUserLicenseAgreementResponse](enduserlicenseagreementresponse.md)
  The response body for endpoints that read or modify a custom end user license agreement for an app.
- [object EndUserLicenseAgreementWithoutIncludesResponse](enduserlicenseagreementwithoutincludesresponse.md)
  A response containing a single EULA, without including territory details.
- [object AppEndUserLicenseAgreementLinkageResponse](appenduserlicenseagreementlinkageresponse.md)
- [object EndUserLicenseAgreementTerritoriesLinkagesResponse](enduserlicenseagreementterritorieslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/enduserlicenseagreement)*