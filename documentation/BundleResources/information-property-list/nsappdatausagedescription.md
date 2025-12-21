# NSAppDataUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that tells people why the app needs to access files in other apps’ sandbox containers.

**Availability**:
- macOS 14.0+

#### Discussion

When your app tries to open a file that’s in another app’s sandbox container, the system requests permission from the person using the app and presents this message. If your app doesn’t have a value for the `NSAppDataUsageDescription` key in its information property list, the system presents a default message.

The system uses this message any time your app tries to access files in another app’s container, and your app can’t provide different messages for attempts to access containers from different apps.

## See Also

- [NSUpdateSecurityPolicy](information-property-list/nsupdatesecuritypolicy.md)
  A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsappdatausagedescription)*