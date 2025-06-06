# NSSystemAdministrationUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message in macOS that tells the user why the app is requesting to manipulate the system configuration.

**Availability**:
- macOS 10.14+

#### Discussion

Use this key if your app uses certain APIs that manipulate system configuration, like [`ODRecordSetValue(_:_:_:_:)`](https://developer.apple.com/documentation/OpenDirectory/ODRecordSetValue(_:_:_:_:)).

> ❗ **Important**:  This key is required if your app uses APIs that manipulate the system configuration.

 This key is required if your app uses APIs that manipulate the system configuration.

## See Also

- [NSUpdateSecurityPolicy](information-property-list/nsupdatesecuritypolicy.md)
  A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.
- [NSAppDataUsageDescription](information-property-list/nsappdatausagedescription.md)
  A message that tells the user why the app needs to access files in other apps’ sandbox containers.
- [NSUserTrackingUsageDescription](information-property-list/nsusertrackingusagedescription.md)
  A message that informs the user why an app is requesting permission to use data for tracking the user or the device.
- [NSAppleEventsUsageDescription](information-property-list/nsappleeventsusagedescription.md)
  A message that tells the user why the app is requesting the ability to send Apple events.
- [ITSAppUsesNonExemptEncryption](information-property-list/itsappusesnonexemptencryption.md)
  A Boolean value indicating whether the app uses encryption.
- [ITSEncryptionExportComplianceCode](information-property-list/itsencryptionexportcompliancecode.md)
  The export compliance code provided by App Store Connect for apps that require it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nssystemadministrationusagedescription)*