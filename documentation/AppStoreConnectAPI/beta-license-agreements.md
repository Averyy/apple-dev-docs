# Beta License Agreements

**Framework**: App Store Connect API

Beta license agreements for apps.

#### Overview

A `betaLicenseAgreements` resource contains the license agreement text for users who test the app through TestFlight. Each app has a single beta license agreement. You can edit the agreement text.

## Topics

### Getting Beta License Agreement Information
- [List beta license agreements](get-v1-betalicenseagreements.md)
  Find and list beta license agreements for all apps.
- [Read beta license agreement information](get-v1-betalicenseagreements-_id_.md)
  Get a specific beta license agreement.
- [Read the app information of a beta license agreement](get-v1-betalicenseagreements-_id_-app.md)
  Get the app information for a specific beta license agreement.
- [Get the app ID for a beta license agreement](get-v1-betalicenseagreements-_id_-relationships-app.md)
### Modifying Beta License Agreements
- [Modify a beta license agreement](patch-v1-betalicenseagreements-_id_.md)
  Update the text for your beta license agreement.
### Objects
- [object BetaLicenseAgreement](betalicenseagreement.md)
  The custom terms and conditions presented to TestFlight testers before they begin testing an app.
- [object BetaLicenseAgreementUpdateRequest](betalicenseagreementupdaterequest.md)
  The request body you use to update a Beta License Agreement.
- [object BetaLicenseAgreementWithoutIncludesResponse](betalicenseagreementwithoutincludesresponse.md)
  A response containing a single TestFlight license agreement, without related resources.
- [object BetaLicenseAgreementsResponse](betalicenseagreementsresponse.md)
  The response body for endpoints that list TestFlight license agreements.
- [object BetaLicenseAgreementResponse](betalicenseagreementresponse.md)
  The response body for endpoints that read or modify the TestFlight license agreement for an app.
- [object BetaLicenseAgreementAppLinkageResponse](betalicenseagreementapplinkageresponse.md)

## See Also

- [Prerelease Versions](prerelease-versions.md)
  Platform-specific versions of your app intended for distribution to beta testers.
- [Beta App Localizations](beta-app-localizations.md)
  Beta test information about apps, specific to a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/beta-license-agreements)*