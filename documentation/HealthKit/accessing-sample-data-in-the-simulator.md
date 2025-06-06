# Accessing Sample Data in the Simulator

**Framework**: HealthKit

Set up sample accounts to build and test your app.

#### Overview

You cannot create your own [`HKClinicalRecord`](hkclinicalrecord.md) samples. When you need sample data to build or test your app, you must either download real data from a supported healthcare institution, or access existing sample data.  Xcode provides three sample accounts in the simulator that you can use to build and test your app.

There are two steps to using the sample data:

- Add a sample account to provide the initial data for building and testing your app.
- Simulate updates by adding additional accounts.

##### Add Sample Accounts

To access the sample accounts, open the Health app on the simulator, and navigate to Health Data > Health Records.

![A screenshot of the Health Records view.](https://docs-assets.developer.apple.com/published/2602c7f73c72d661cb2887e345dc7d38/media-3040233%402x.png)

The Health Records view displays a message about adding accounts to healthcare institutions. Click Get Started. The system may ask to access your location, but you do not need to share that information in order to add the sample accounts. The system then shows the three sample accounts, and any supported healthcare institutions in your area if you shared your location.

![A screenshot showing the three sample accounts.](https://docs-assets.developer.apple.com/published/06e5bce582ca5c83637a10256f894b41/media-3040231%402x.png)

Select the sample account you want to add, and the system displays the data available for that account. Select the data to add it to HealthKit.

![A screenshot showing the sample data from the account.](https://docs-assets.developer.apple.com/published/5056589b0cee311c90f63e2aee003bf8/media-3040229%402x.png)

Health then displays a confirmation showing that it has added the account to HealthKit. Click the Done button to continue, and the Health Records view shows the account that you added. You can add additional accounts, as needed.

![A screenshot of the Health Records data, including data from the newly added account.](https://docs-assets.developer.apple.com/published/f1246d41e755ba49917c431a8738244e/media-3040232%402x.png)

Click on the account to view the data. You can browse all the clinical records associated with the account. This data is also available to your app while it is running on the simulator.

![A screenshot of the sample data downloaded from the account.](https://docs-assets.developer.apple.com/published/90789c7dd2e3804e06205befe3b11b73/media-3040228%402x.png)

##### Simulate Updates

When the user authorizes access to clinical records, they also select how the app handles new data: whether the app automatically receives the data or needs to ask for permission first. Your testing should cover both cases. For example, to test these cases manually, run your app in the simulator and enable permission to automatically receive updates. Then select Hardware > Erase All Contents and Settings, and run the app again. For this test, require your app to ask for permission to download updates.

Note that the sample accounts only provide static data; all the data is received as soon as the account is added. However, you can simulate the arrival of new clinical records by adding additional accounts. From the app’s perspective, adding a new account is the same as new data coming in for an existing account. By adding a new account, you can ensure that your app properly handles incoming data.

## See Also

- [Accessing Health Records](accessing-health-records.md)
  Read clinical record data from the HealthKit store.
- [Accessing a User’s Clinical Records](accessing-a-user-s-clinical-records.md)
  Request authorization to query HealthKit for a user’s clinical records and display them in your app.
- [Accessing Data from a SMART Health Card](accessing-data-from-a-smart-health-card.md)
  Query for and validate a verifiable clinical record.
- [class HKClinicalRecord](hkclinicalrecord.md)
  A sample that stores a clinical record.
- [class HKFHIRResource](hkfhirresource.md)
  An object containing Fast Healthcare Interoperability Resources (FHIR) data.
- [class HKVerifiableClinicalRecord](hkverifiableclinicalrecord.md)
  A sample that represents the contents of a SMART Health Card or EU Digital COVID Certificate.
- [class HKVerifiableClinicalRecordSubject](hkverifiableclinicalrecordsubject.md)
  The subject associated with a signed clinical record.
- [class HKCDADocumentSample](hkcdadocumentsample.md)
  A Clinical Document Architecture (CDA) sample that stores a single document.
- [class HKDocumentSample](hkdocumentsample.md)
  An abstract class that represents a health document in the HealthKit store.
- [static let CDA: HKDocumentTypeIdentifier](hkdocumenttypeidentifier/cda.md)
  The CDA Document type identifier, used when requesting permission to read or share CDA documents.
- [class HKDocumentType](hkdocumenttype.md)
  A sample type used to create queries for documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/accessing-sample-data-in-the-simulator)*