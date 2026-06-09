# EndUserLicenseAgreementCreateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to create an End User License Agreement.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object EndUserLicenseAgreementCreateRequest
```

## Topics

### Objects
- [object EndUserLicenseAgreementCreateRequest.Data](enduserlicenseagreementcreaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (EndUserLicenseAgreementCreateRequest.Data) *(required)*

## See Also

- [object EndUserLicenseAgreement](enduserlicenseagreement.md)
  A custom end-user license agreement (EULA) for an app, targeting specific territories where it applies.
- [object EndUserLicenseAgreementUpdateRequest](enduserlicenseagreementupdaterequest.md)
  The request body you use to update an End User License Agreement.
- [object EndUserLicenseAgreementResponse](enduserlicenseagreementresponse.md)
  The response body for endpoints that read or modify a custom end user license agreement for an app.
- [object EndUserLicenseAgreementWithoutIncludesResponse](enduserlicenseagreementwithoutincludesresponse.md)
  A response containing a single EULA, without including territory details.
- [object AppEndUserLicenseAgreementLinkageResponse](appenduserlicenseagreementlinkageresponse.md)
- [object EndUserLicenseAgreementTerritoriesLinkagesResponse](enduserlicenseagreementterritorieslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/enduserlicenseagreementcreaterequest)*