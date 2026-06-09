# BetaLicenseAgreementResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read or modify the TestFlight license agreement for an app.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaLicenseAgreementResponse
```

## Properties

- `data` (BetaLicenseAgreement) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.
- `included` ([App])

## See Also

- [Read the beta license agreement of an app](get-v1-apps-_id_-betalicenseagreement.md)
  Get the beta license agreement for a specific app.
- [object BetaLicenseAgreement](betalicenseagreement.md)
  The custom terms and conditions presented to TestFlight testers before they begin testing an app.
- [object BetaLicenseAgreementUpdateRequest](betalicenseagreementupdaterequest.md)
  The request body you use to update a Beta License Agreement.
- [object BetaLicenseAgreementWithoutIncludesResponse](betalicenseagreementwithoutincludesresponse.md)
  A response containing a single TestFlight license agreement, without related resources.
- [object BetaLicenseAgreementsResponse](betalicenseagreementsresponse.md)
  The response body for endpoints that list TestFlight license agreements.
- [object BetaLicenseAgreementAppLinkageResponse](betalicenseagreementapplinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betalicenseagreementresponse)*