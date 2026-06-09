# BetaLicenseAgreementsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list TestFlight license agreements.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaLicenseAgreementsResponse
```

## Properties

- `data` ([BetaLicenseAgreement]) *(required)*: The resource data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.
- `included` ([App])

## See Also

- [List beta license agreements](get-v1-betalicenseagreements.md)
  Find and list beta license agreements for all apps.
- [object BetaLicenseAgreement](betalicenseagreement.md)
  The custom terms and conditions presented to TestFlight testers before they begin testing an app.
- [object BetaLicenseAgreementUpdateRequest](betalicenseagreementupdaterequest.md)
  The request body you use to update a Beta License Agreement.
- [object BetaLicenseAgreementWithoutIncludesResponse](betalicenseagreementwithoutincludesresponse.md)
  A response containing a single TestFlight license agreement, without related resources.
- [object BetaLicenseAgreementResponse](betalicenseagreementresponse.md)
  The response body for endpoints that read or modify the TestFlight license agreement for an app.
- [object BetaLicenseAgreementAppLinkageResponse](betalicenseagreementapplinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betalicenseagreementsresponse)*