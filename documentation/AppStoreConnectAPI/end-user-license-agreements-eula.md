# End User License Agreements (EULA)

**Framework**: App Store Connect API

Manage custom End User License Agreements (EULA) that are related to territories.

#### Overview

`endUserLicenseAgreements` represents the custom End User License Agreement (EULA) that you provide. Apple provides a standard EULA that applies in all territories. If you need to provide a custom EULA, use this resource to provide your agreement text. Relate it to the app and territories for which it applies using the [`Territories`](territories.md) resource.

For more information, see App Store Connect Help: [`Create a new version`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/update-your-app/create-a-new-version).

## Topics

### Creating, Modifying, and Deleting an EULA
- [Create an End User License Agreement](post-v1-enduserlicenseagreements.md)
  Add a custom end user license agreement (EULA) to an app and configure the territories to which it applies.
- [Modify an End User License Agreement](patch-v1-enduserlicenseagreements-_id_.md)
  Update the text or territories for your custom end user license agreement.
- [Delete an End User License Agreement](delete-v1-enduserlicenseagreements-_id_.md)
  Delete the custom end user license agreement that is associated with an app.
### Reading EULA and Listing Territories
- [Read End User License Agreement Information](get-v1-enduserlicenseagreements-_id_.md)
  Get the custom end user license agreement associated with an app, and the territories it applies to.
- [Read the End User License Agreement Information of an App](get-v1-apps-_id_-enduserlicenseagreement.md)
  Get the custom end user license agreement (EULA) for a specific app and the territories where the agreement applies.
- [List All Territories for an End User License Agreement](get-v1-enduserlicenseagreements-_id_-territories.md)
  List all the App Store territories to which a specific custom app license agreement applies.
### Objects
- [object EndUserLicenseAgreement](enduserlicenseagreement.md)
  The data structure that represents the End User License Agreement resource.
- [object EndUserLicenseAgreementCreateRequest](enduserlicenseagreementcreaterequest.md)
  The request body you use to create an End User License Agreement.
- [object EndUserLicenseAgreementUpdateRequest](enduserlicenseagreementupdaterequest.md)
  The request body you use to update an End User License Agreement.
- [object EndUserLicenseAgreementResponse](enduserlicenseagreementresponse.md)
  A response that contains a single End User License Agreements resource.
- [object EndUserLicenseAgreementWithoutIncludesResponse](enduserlicenseagreementwithoutincludesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/end-user-license-agreements-eula)*