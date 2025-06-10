# Beta License Agreements

**Framework**: App Store Connect API

Beta license agreements for apps.

#### Overview

A `betaLicenseAgreements` resource contains the license agreement text for users who test the app through TestFlight. Each app has a single beta license agreement. You can edit the agreement text.

## Topics

### Getting Beta License Agreement Information
- [List Beta License Agreements](get-v1-betalicenseagreements.md)
  Find and list beta license agreements for all apps.
- [Read Beta License Agreement Information](get-v1-betalicenseagreements-_id_.md)
  Get a specific beta license agreement.
- [Read the App Information of a Beta License Agreement](get-v1-betalicenseagreements-_id_-app.md)
  Get the app information for a specific beta license agreement.
- [GET /v1/betaLicenseAgreements/{id}/relationships/app](get-v1-betalicenseagreements-_id_-relationships-app.md)
### Modifying Beta License Agreements
- [Modify a Beta License Agreement](patch-v1-betalicenseagreements-_id_.md)
  Update the text for your beta license agreement.
### Objects
- [object BetaLicenseAgreement](betalicenseagreement.md)
  The data structure that represents a Beta License Agreements resource.
- [object BetaLicenseAgreementUpdateRequest](betalicenseagreementupdaterequest.md)
  The request body you use to update a Beta License Agreement.
- [object BetaLicenseAgreementWithoutIncludesResponse](betalicenseagreementwithoutincludesresponse.md)
- [object BetaLicenseAgreementsResponse](betalicenseagreementsresponse.md)
  A response that contains a list of Beta License Agreement resources.
- [object BetaLicenseAgreementResponse](betalicenseagreementresponse.md)
  A response that contains a single Beta License Agreements resource.
- [object BetaLicenseAgreementAppLinkageResponse](betalicenseagreementapplinkageresponse.md)

## See Also

- [Prerelease Versions](prerelease-versions.md)
  Platform-specific versions of your app intended for distribution to beta testers.
- [Beta App Localizations](beta-app-localizations.md)
  Beta test information about apps, specific to a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-license-agreements)*