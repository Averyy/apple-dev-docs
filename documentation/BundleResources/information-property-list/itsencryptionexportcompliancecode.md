# ITSEncryptionExportComplianceCode

**Framework**: Bundle Resources  
**Kind**: typealias

The export compliance code provided by App Store Connect for apps that require it.

**Availability**:
- macOS 10.0+

#### Discussion

Include this key in your app’s [`Information Property List`](information-property-list.md) file if you set the [`ITSAppUsesNonExemptEncryption`](information-property-list/itsappusesnonexemptencryption.md) key’s value to `YES`. Set the value for this key to the code that Apple sends you after successfully reviewing export compliance documentation that you provide through App Store Connect.

For additional information, see [`Complying with Encryption Export Regulations`](https://developer.apple.com/documentation/Security/complying-with-encryption-export-regulations).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/itsencryptionexportcompliancecode)*