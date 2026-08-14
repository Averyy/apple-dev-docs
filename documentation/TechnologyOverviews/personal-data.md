# Personal data

**Framework**: Technology Overviews

Access the personal data that people keep on their devices.

Apple devices manage a lot of personal information, including a person’s contacts, their photos, and even their health data. Although people use system apps to manage many types of data, other apps can access that data too. For example, a running app might add each new workout to the person’s health data. For some types of data, you can also contribute new data your app collects.

#### Request Authorization to Access Personal Data

The data people put on their devices belongs to them, and much of it is personal information they might not want to share. Before you access any personal data, request permission to do so and provide a reason why you need that data.

Before you access any personal data, each Apple technology has specific API you must call to request access to that data. The first time your app calls one of these API, the system displays a special panel to inform the person of your request. The person then uses this panel to grant or deny access, and the system records their choice and typically doesn’t display the panel again. Subsequent requests for access simply return the previously requested choice.

When the system prompts someone to grant or deny a request, the panel displays a *usage description* string that you provide. This string is your opportunity to tell the person how you intend to use their data. People use these strings to decide whether or not to grant access, so it’s important to provide a compelling reason for access. Be clear about how your intentions, and communicate the benefits you provide with access to the data. For example, a running app might indicate that it contributes the workout data it collects to the person’s health records.

#### Fetch Different Types of Personal Data

Access or modify someone’s personal data using the appropriate system frameworks. The following table lists the types of data you can retrieve, the frameworks you use to access or modify that data, and the usage description keys you can include in the Info pane of your project in Xcode. When multiple keys are available, choose the ones that match the type of access you’re requesting.

| Data | Framework | Usage description keys |
| --- | --- | --- |
| Contacts | [`Contacts`](https://developer.apple.com/documentation/contacts), [`Contacts UI`](https://developer.apple.com/documentation/contactsui) | [`NSContactsUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nscontactsusagedescription) |
| Calendar events | [`EventKit`](https://developer.apple.com/documentation/eventkit), [`EventKit UI`](https://developer.apple.com/documentation/eventkitui) | [`NSCalendarsFullAccessUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nscalendarsfullaccessusagedescription), [`NSCalendarsWriteOnlyAccessUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nscalendarswriteonlyaccessusagedescription) |
| Health information | [`HealthKit`](https://developer.apple.com/documentation/healthkit) | [`NSHealthClinicalHealthRecordsShareUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nshealthclinicalhealthrecordsshareusagedescription), [`NSHealthShareUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nshealthshareusagedescription), [`NSHealthUpdateUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nshealthupdateusagedescription) |
| Location | [`Core Location`](https://developer.apple.com/documentation/corelocation), [`CoreLocationUI`](https://developer.apple.com/documentation/corelocationui) | [`NSLocationWhenInUseUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationwheninuseusagedescription), [`NSLocationAlwaysAndWhenInUseUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription), [`NSLocationTemporaryUsageDescriptionDictionary`](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationtemporaryusagedescriptiondictionary) |
| Music | [`MusicKit`](https://developer.apple.com/documentation/musickit), [`Apple Music API`](https://developer.apple.com/documentation/applemusicapi) | [`NSAppleMusicUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapplemusicusagedescription) |
| Photos | [`PhotoKit`](https://developer.apple.com/documentation/photokit) | [`NSPhotoLibraryAddUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsphotolibraryaddusagedescription), [`NSPhotoLibraryUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsphotolibraryusagedescription) |
| Reminders | [`EventKit`](https://developer.apple.com/documentation/eventkit), [`EventKit UI`](https://developer.apple.com/documentation/eventkitui) | [`NSRemindersFullAccessUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsremindersfullaccessusagedescription) |
| Financial data | [`PKPassLibrary`](https://developer.apple.com/documentation/passkit/pkpasslibrary) |  |
| Game Center friends | [`GameKit`](https://developer.apple.com/documentation/gamekit) | [`NSGKFriendListUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsgkfriendlistusagedescription) |
| TV provider account information | [`Video Subscriber Account`](https://developer.apple.com/documentation/videosubscriberaccount) | [`NSVideoSubscriberAccountUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsvideosubscriberaccountusagedescription) |

---

#### Access Environmental Data on Apple Vision Pro

The cameras on Apple Vision Pro generate significant amounts of data about a person’s environment. To protect people’s privacy, visionOS limits the types of information apps can receive directly from these cameras. For example, the system provides a 3D mesh of a person’s environment to detect collisions with virtual content, but it doesn’t provide direct access to the cameras or LiDAR sensor it uses to generate that mesh. Similarly, the system handles many standard hand gestures, and makes hand positions and movements available through special APIs.

Most of the environmental data you receive in visionOS comes from the [`ARKit`](https://developer.apple.com/documentation/arkit) framework. This framework helps you detect items in a person’s environment in a privacy friendly way. You can perform and track, detect planes, build a mesh of the environment, track objects and images, and much more.

---

#### Verify Someones Identity

Many state and federal governments let people verify their identity digitally using their iPhone. Support for mobile driver’s licenses and national identity cards gives people a way to prove their identity in a more privacy friendly way than showing the corresponding documents. On iPhone, people store the digital versions of these documents in the Wallet app.

If you create an app that requires an identity verification element, you can request access to documents in someone’s Wallet using the [`Verify with Wallet API`](https://developer.apple.comhttps://developer.apple.com/wallet/get-started-with-verify-with-wallet/). Apps that adopt this API request an [`entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/verify-with-wallet/) that includes the reason why you need this information. After receiving the entitlement, make
[`Requesting identity data from a Wallet pass`](https://developer.apple.com/documentation/passkit/requesting-identity-data-from-a-wallet-pass) using the APIs of the [`Wallet`](https://developer.apple.com/documentation/passkit/wallet).

If your app manages digital documents using the Digital Credentials API from the W3C, register as a document provider using the [`IdentityDocumentServices`](https://developer.apple.com/documentation/identitydocumentservices) framework. When someone chooses to verify a person’s name, age, or other identity-related details using the documents your app manages, the system forwards the request to your [`IdentityDocumentServicesUI`](https://developer.apple.com/documentation/identitydocumentservicesui), which processes the request and delivers the response.

If you need to verify identity information on someone else’s iPhone, use the [`ProximityReader`](https://developer.apple.com/documentation/proximityreader) framework to read that data in a secure and private manner. For example, an app that provides an age verification service for patrons entering a bar might use this approach. Before entering the bar, the host would ask people to present their iPhone, which the host would then scan using the app. The host only receives confirmation that the person is the required age, and doesn’t receive any other personal information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/personal-data)*