# Protected resources

**Framework**: Bundle Resources

Control an app’s access to protected system services and user data.

#### Overview

Before your app can access certain protected resources, like the Bluetooth interface, location information, or the user’s photos, the system asks the user for permission on behalf of your app. The prompt that the system displays includes a `UsageDescription` string you provide, explaining why your app needs to access the protected resource. Enter the string in the Signing and Capabilities editor for your app’s target, as described in [`Requesting access to protected resources`](https://developer.apple.com/documentation/UIKit/requesting-access-to-protected-resources). Xcode adds the string as the value for the relevant [`Information Property List`](information-property-list.md) key in your app’s build settings. The topics below list the keys you use to provide usage-description strings for protected resources.

## Topics

### Essentials
- [Requesting access to protected resources](../UIKit/requesting-access-to-protected-resources.md)
  Provide a purpose string that explains to a person why you need access to protected resources on their device.
- [Inspecting app activity data](../Network/inspecting-app-activity-data.md)
  Verify that your app accesses only the user data and network resources that you expect it to access.
### Bluetooth
- [NSBluetoothAlwaysUsageDescription](information-property-list/nsbluetoothalwaysusagedescription.md)
  A message that tells people why the app needs access to Bluetooth.
- [NSBluetoothPeripheralUsageDescription](information-property-list/nsbluetoothperipheralusagedescription.md)
  A message that tells people why the app is requesting the ability to connect to Bluetooth peripherals.
### Calendar and reminders
- [NSCalendarsFullAccessUsageDescription](information-property-list/nscalendarsfullaccessusagedescription.md)
  A message that tells people why the app is requesting access to read and write their calendar data.
- [NSCalendarsWriteOnlyAccessUsageDescription](information-property-list/nscalendarswriteonlyaccessusagedescription.md)
  A message that tells people why the app is requesting access to create calendar events.
- [NSRemindersFullAccessUsageDescription](information-property-list/nsremindersfullaccessusagedescription.md)
  A message that tells people why the app is requesting access to read and write their reminders data.
- [Accessing the event store](../EventKit/accessing-the-event-store.md)
  Request access to a person’s calendar data through the event store.
### Camera and sound
- [Requesting authorization to capture and save media](../AVFoundation/requesting-authorization-to-capture-and-save-media.md)
  Prompt the user to authorize access to the camera, microphone, and photo library.
- [Requesting Authorization for Media Capture on macOS](requesting-authorization-for-media-capture-on-macos.md)
  Prompt the user to authorize access to the camera and microphone.
- [NSAudioCaptureUsageDescription](information-property-list/nsaudiocaptureusagedescription.md)
  A message that tells people why your app is requesting access to capture system audio on macOS.
- [NSCameraUsageDescription](information-property-list/nscamerausagedescription.md)
  A message that tells people why the app is requesting access to the device’s camera.
- [NSMainCameraUsageDescription](information-property-list/nsmaincamerausagedescription.md)
  A message that tells people why the app is requesting access to the device’s main camera.
- [NSMicrophoneUsageDescription](information-property-list/nsmicrophoneusagedescription.md)
  A message that tells people why the app is requesting access to the device’s microphone.
### Contacts
- [Accessing the contact store](../Contacts/accessing-the-contact-store.md)
  Request permission from the person to read and write their contact data.
- [NSContactsUsageDescription](information-property-list/nscontactsusagedescription.md)
  A message that tells people why the app is requesting access to their contacts.
### Face ID
- [Logging a User into Your App with Face ID or Touch ID](../LocalAuthentication/logging-a-user-into-your-app-with-face-id-or-touch-id.md)
  Supplement your own authentication scheme with biometric authentication, making it easy for users to access sensitive parts of your app.
- [NSFaceIDUsageDescription](information-property-list/nsfaceidusagedescription.md)
  A message that tells people why the app is requesting the ability to authenticate with Face ID.
### Files and folders
- [NSDesktopFolderUsageDescription](information-property-list/nsdesktopfolderusagedescription.md)
  A message that tells people why the app needs access to their Desktop folder.
- [NSDocumentsFolderUsageDescription](information-property-list/nsdocumentsfolderusagedescription.md)
- [NSDownloadsFolderUsageDescription](information-property-list/nsdownloadsfolderusagedescription.md)
  A message that tells people why the app needs access to the user’s Downloads folder.
- [NSNetworkVolumesUsageDescription](information-property-list/nsnetworkvolumesusagedescription.md)
  A message that tells people why the app needs access to files on a network volume.
- [NSRemovableVolumesUsageDescription](information-property-list/nsremovablevolumesusagedescription.md)
  A message that tells people why the app needs access to files on a removable volume.
- [NSFileProviderDomainUsageDescription](information-property-list/nsfileproviderdomainusagedescription.md)
  A message that tells people why the app needs access to files managed by a file provider.
### Game Center
- [NSGKFriendListUsageDescription](information-property-list/nsgkfriendlistusagedescription.md)
  A message that tells people why the app needs access to their Game Center friends list.
### Health
- [Setting up HealthKit](../HealthKit/setting-up-healthkit.md)
  Set up and configure your HealthKit store.
- [NSHealthClinicalHealthRecordsShareUsageDescription](information-property-list/nshealthclinicalhealthrecordsshareusagedescription.md)
  A message to the user that explains why the app requested permission to read clinical records.
- [NSHealthShareUsageDescription](information-property-list/nshealthshareusagedescription.md)
  A message that explains to people why the app requests permission to read samples from the HealthKit store.
- [NSHealthUpdateUsageDescription](information-property-list/nshealthupdateusagedescription.md)
  A message to the user that explains why the app requested permission to save samples to the HealthKit store.
- [NSHealthRequiredReadAuthorizationTypeIdentifiers](information-property-list/nshealthrequiredreadauthorizationtypeidentifiers.md)
  The clinical record data types that your app must get permission to read.
### Home
- [Enabling HomeKit in your app](../HomeKit/enabling-homekit-in-your-app.md)
  Declare your app’s intention to use HomeKit, and get permission from the user to access home automation accessories.
- [NSHomeKitUsageDescription](information-property-list/nshomekitusagedescription.md)
  A message that tells people why the app is requesting access to their HomeKit configuration data.
### Location
- [Choosing the  Location Services Authorization to Request](choosing-the-location-services-authorization-to-request.md)
  Determine the authorization your app needs to access location data.
- [NSLocationAlwaysAndWhenInUseUsageDescription](information-property-list/nslocationalwaysandwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information at all times.
- [NSLocationUsageDescription](information-property-list/nslocationusagedescription.md)
  A message that tells people why the app is requesting access to their location information.
- [NSLocationWhenInUseUsageDescription](information-property-list/nslocationwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationTemporaryUsageDescriptionDictionary](information-property-list/nslocationtemporaryusagedescriptiondictionary.md)
  A collection of messages that explain why the app is requesting temporary access to their location.
- [NSLocationAlwaysUsageDescription](information-property-list/nslocationalwaysusagedescription.md)
  A message that tells people why the app is requesting access to their location at all times.
- [NSWidgetWantsLocation](information-property-list/nswidgetwantslocation.md)
  A Boolean value that indicates a widget uses the user’s location information.
- [NSLocationDefaultAccuracyReduced](information-property-list/nslocationdefaultaccuracyreduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.
### MediaPlayer
- [Requesting Access to Apple Music Library](../StoreKit/requesting-access-to-apple-music-library.md)
  Prompt the customer to authorize access to Apple Music library.
- [NSAppleMusicUsageDescription](information-property-list/nsapplemusicusagedescription.md)
  A message that tells people why the app is requesting access to their media library.
### Messages
- [NSCriticalMessagingUsageDescription](information-property-list/nscriticalmessagingusagedescription.md)
  A message that tells people why the app needs to send SMS messages.
### Motion
- [NSMotionUsageDescription](information-property-list/nsmotionusagedescription.md)
  A message that tells people why the app is requesting access to the device’s motion data.
- [NSFallDetectionUsageDescription](information-property-list/nsfalldetectionusagedescription.md)
  A message to the user that explains the app’s request for permission to access fall detection event data.
### Networking
- [NSLocalNetworkUsageDescription](information-property-list/nslocalnetworkusagedescription.md)
  A message that tells people why the app is requesting access to the local network.
- [NSNearbyInteractionUsageDescription](information-property-list/nsnearbyinteractionusagedescription.md)
  A request for user permission to begin an interaction session with nearby devices.
- [NSNearbyInteractionAllowOnceUsageDescription](information-property-list/nsnearbyinteractionallowonceusagedescription.md)
  A one-time request for user permission to begin an interaction session with nearby devices.
### NFC
- [NFCReaderUsageDescription](information-property-list/nfcreaderusagedescription.md)
  A message that tells people why the app is requesting access to the device’s NFC hardware.
### Photos
- [Delivering an Enhanced Privacy Experience in Your Photos App](../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)
  Adopt the latest privacy enhancements to deliver advanced user-privacy controls.
- [NSPhotoLibraryAddUsageDescription](information-property-list/nsphotolibraryaddusagedescription.md)
  A message that tells people why the app is requesting add-only access to their photo library.
- [NSPhotoLibraryUsageDescription](information-property-list/nsphotolibraryusagedescription.md)
  A message that tells people why the app is requesting access to their photo library.
### Scripting
- [NSAppleScriptEnabled](information-property-list/nsapplescriptenabled.md)
  A Boolean value indicating whether AppleScript is enabled.
### Security
- [NSUpdateSecurityPolicy](information-property-list/nsupdatesecuritypolicy.md)
  A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.
- [NSAppDataUsageDescription](information-property-list/nsappdatausagedescription.md)
  A message that tells people why the app needs to access files in other apps’ sandbox containers.
- [NSUserTrackingUsageDescription](information-property-list/nsusertrackingusagedescription.md)
  A message that informs the user why an app is requesting permission to use data for tracking the user or the device.
- [NSAppleEventsUsageDescription](information-property-list/nsappleeventsusagedescription.md)
  A message that tells people why the app is requesting the ability to send Apple events.
- [NSSystemAdministrationUsageDescription](information-property-list/nssystemadministrationusagedescription.md)
  A message in macOS that tells people why the app is requesting to manipulate the system configuration.
- [ITSAppUsesNonExemptEncryption](information-property-list/itsappusesnonexemptencryption.md)
  A Boolean value indicating whether the app uses encryption.
- [ITSEncryptionExportComplianceCode](information-property-list/itsencryptionexportcompliancecode.md)
  The export compliance code provided by App Store Connect for apps that require it.
### Sensors
- [NSSensorKitUsageDescription](information-property-list/nssensorkitusagedescription.md)
  A short description of the purpose of your app’s research study.
- [NSSensorKitUsageDetail](information-property-list/nssensorkitusagedetail.md)
  A dictionary that includes keys for the specific information your app collects.
- [NSSensorKitPrivacyPolicyURL](information-property-list/nssensorkitprivacypolicyurl.md)
  A hyperlink to a webpage that displays the privacy policy for your app’s research study.
### Siri
- [Requesting Authorization to Use Siri](../SiriKit/requesting-authorization-to-use-siri.md)
  Request permission from the user for Siri and Maps to communicate with your app or Intents app extension.
- [NSSiriUsageDescription](information-property-list/nssiriusagedescription.md)
  A message that tells people why the app is requesting to send user data to Siri.
### Speech
- [Asking Permission to Use Speech Recognition](../Speech/asking-permission-to-use-speech-recognition.md)
  Ask the user’s permission to perform speech recognition using Apple’s servers.
- [NSSpeechRecognitionUsageDescription](information-property-list/nsspeechrecognitionusagedescription.md)
  A message that tells people why the app is requesting to send user data to Apple’s speech recognition servers.
### System Extensions
- [NSSystemExtensionUsageDescription](information-property-list/nssystemextensionusagedescription.md)
  A message that tells people why the app is trying to install a system extension bundle.
- [OSBundleUsageDescription](information-property-list/osbundleusagedescription.md)
  A message that tells people why the app is trying to install a driver extension bundle.
### TV
- [NSVideoSubscriberAccountUsageDescription](information-property-list/nsvideosubscriberaccountusagedescription.md)
  A message that tells people why the app is requesting access to their TV provider account.
### Vision
- [NSWorldSensingUsageDescription](information-property-list/nsworldsensingusagedescription.md)
  A message that tells people why the app is requesting access to image tracking, plane detection, or scene reconstruction.
- [NSHandsTrackingUsageDescription](information-property-list/nshandstrackingusagedescription.md)
  A message that tells people why the app is requesting access to track their hand position and location.
- [NSAccessoryTrackingUsageDescription](information-property-list/nsaccessorytrackingusagedescription.md)
  A message that tells a person why the app is requesting access to track accessory position and location.
### Wallet
- [NSFinancialDataUsageDescription](information-property-list/nsfinancialdatausagedescription.md)
  A message that tells people why the app is requesting access to financial data stored in Wallet.
- [NSIdentityUsageDescription](information-property-list/nsidentityusagedescription.md)
  A message that tells people why the app is requesting identity information.
### Wi-Fi
- [UIRequiresPersistentWiFi](information-property-list/uirequirespersistentwifi.md)
  A Boolean value that indicates whether the app requires a Wi-Fi connection.
### Deprecated keys
- [NSCalendarsUsageDescription](information-property-list/nscalendarsusagedescription.md)
  A message that tells people why the app is requesting access to their calendar data.
- [NSEnterpriseMCAMUsageDescription](information-property-list/nsenterprisemcamusagedescription.md)
  A message that tells people why the app is requesting access to the device’s main camera.
- [NSRemindersUsageDescription](information-property-list/nsremindersusagedescription.md)
  A message that tells people why the app is requesting access to their reminders.

## See Also

- [Data and storage](data-and-storage.md)
  Regulate documents, URLs, and other kinds of data movement and storage.
- [App services](app-services.md)
  Configure services provided by the app, like support for giving directions or using game controllers.
- [Kernel and drivers](kernel-and-drivers.md)
  Configure device drivers provided by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/protected-resources)*