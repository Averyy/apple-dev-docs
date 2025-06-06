# ITSAppUsesNonExemptEncryption

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether the app uses encryption.

**Availability**:
- macOS 10.0+

#### Discussion

Set the value for this key to `NO` in your app’s [`Information Property List`](information-property-list.md) file to indicate that your app—including any third-party libraries you link against—either uses no encryption, or only uses encryption that’s exempt from export compliance requirements, as described in [`Determine your export compliance requirements`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev63c95e436). Set the value to `YES` to indicate that your app uses non-exempt encryption.

If you set the value to `YES`, you typically also provide a value for the [`ITSEncryptionExportComplianceCode`](information-property-list/itsencryptionexportcompliancecode.md) key. You set that key’s value using a code Apple provides after successfully reviewing your export compliance documentation.

If you don’t have the [`ITSAppUsesNonExemptEncryption`](information-property-list/itsappusesnonexemptencryption.md) key in your app’s `Info.plist` file, App Store Connect walks you through an export compliance questionnaire every time you upload a new version of your app. Including the key streamlines the app submission process.

For additional information, see [`Complying with Encryption Export Regulations`](https://developer.apple.com/documentation/Security/complying-with-encryption-export-regulations).

## See Also

- [NSUpdateSecurityPolicy](information-property-list/nsupdatesecuritypolicy.md)
  A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.
- [NSAppDataUsageDescription](information-property-list/nsappdatausagedescription.md)
  A message that tells the user why the app needs to access files in other apps’ sandbox containers.
- [NSUserTrackingUsageDescription](information-property-list/nsusertrackingusagedescription.md)
  A message that informs the user why an app is requesting permission to use data for tracking the user or the device.
- [NSAppleEventsUsageDescription](information-property-list/nsappleeventsusagedescription.md)
  A message that tells the user why the app is requesting the ability to send Apple events.
- [NSSystemAdministrationUsageDescription](information-property-list/nssystemadministrationusagedescription.md)
  A message in macOS that tells the user why the app is requesting to manipulate the system configuration.
- [ITSEncryptionExportComplianceCode](information-property-list/itsencryptionexportcompliancecode.md)
  The export compliance code provided by App Store Connect for apps that require it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/itsappusesnonexemptencryption)*