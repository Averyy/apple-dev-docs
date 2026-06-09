# EndUserLicenseAgreementResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read or modify a custom end user license agreement for an app.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object EndUserLicenseAgreementResponse
```

## Properties

- `data` (EndUserLicenseAgreement) *(required)*
- `included` ([*])
- `links` (DocumentLinks) *(required)*

## See Also

- [object EndUserLicenseAgreement](enduserlicenseagreement.md)
  A custom end-user license agreement (EULA) for an app, targeting specific territories where it applies.
- [object EndUserLicenseAgreementCreateRequest](enduserlicenseagreementcreaterequest.md)
  The request body you use to create an End User License Agreement.
- [object EndUserLicenseAgreementUpdateRequest](enduserlicenseagreementupdaterequest.md)
  The request body you use to update an End User License Agreement.
- [object EndUserLicenseAgreementWithoutIncludesResponse](enduserlicenseagreementwithoutincludesresponse.md)
  A response containing a single EULA, without including territory details.
- [object AppEndUserLicenseAgreementLinkageResponse](appenduserlicenseagreementlinkageresponse.md)
- [object EndUserLicenseAgreementTerritoriesLinkagesResponse](enduserlicenseagreementterritorieslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/enduserlicenseagreementresponse)*