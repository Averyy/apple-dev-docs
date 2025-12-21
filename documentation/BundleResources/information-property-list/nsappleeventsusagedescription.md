# NSAppleEventsUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that tells people why the app is requesting the ability to send Apple events.

**Availability**:
- macOS 10.14+

#### Discussion

An app using Apple events to control another app might be able to gain access to sensitive user data. For example, the Mail app stores a lot of personal information in its local database that other apps can’t access directly. But because Mail can be automated with Apple events, other apps can use Mail to gain access to the data indirectly.

> ❗ **Important**:  This key is required if your app uses APIs that send Apple events.

## See Also

- [NSUpdateSecurityPolicy](information-property-list/nsupdatesecuritypolicy.md)
  A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.
- [NSAppDataUsageDescription](information-property-list/nsappdatausagedescription.md)
  A message that tells people why the app needs to access files in other apps’ sandbox containers.
- [NSUserTrackingUsageDescription](information-property-list/nsusertrackingusagedescription.md)
  A message that informs the user why an app is requesting permission to use data for tracking the user or the device.
- [NSSystemAdministrationUsageDescription](information-property-list/nssystemadministrationusagedescription.md)
  A message in macOS that tells people why the app is requesting to manipulate the system configuration.
- [ITSAppUsesNonExemptEncryption](information-property-list/itsappusesnonexemptencryption.md)
  A Boolean value indicating whether the app uses encryption.
- [ITSEncryptionExportComplianceCode](information-property-list/itsencryptionexportcompliancecode.md)
  The export compliance code provided by App Store Connect for apps that require it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsappleeventsusagedescription)*