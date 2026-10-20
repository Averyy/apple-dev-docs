# NSSystemAdministrationUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A message in macOS that tells people why the app is requesting to manipulate the system configuration.

**Availability**:
- macOS 10.14+

## Details

- **Name**: `NSSystemAdministrationUsageDescription` (Privacy - System Administration Usage Description)
- **Type**: string

#### Discussion

Use this key if your app uses certain APIs that manipulate system configuration, like [`ODRecordSetValue(_:_:_:_:)`](../../OpenDirectory/odrecordsetvalue%28_,_,_,_%29.md).

> ❗ **Important**:  This key is required if your app uses APIs that manipulate the system configuration.

## See Also

### Security
- [NSUpdateSecurityPolicy](./nsupdatesecuritypolicy.md)
  A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.
- [NSAppBundlesUsageDescription](./nsappbundlesusagedescription.md)
  A message that tells people why the app needs to access the contents of other apps’ bundles.
- [NSAppDataUsageDescription](./nsappdatausagedescription.md)
  A message that tells people why the app needs to access files in other apps’ sandbox containers.
- [NSUserTrackingUsageDescription](./nsusertrackingusagedescription.md)
  A message that explains the purpose for accessing data that an app can use to track a person or device.
- [NSUserTrackingMarkdownUsageDescription](./nsusertrackingmarkdownusagedescription.md)
  A message that explains the purpose for accessing data that an application can use to track a person or device.
- [NSAppleEventsUsageDescription](./nsappleeventsusagedescription.md)
  A message that tells people why the app is requesting the ability to send Apple events.
- [ITSAppUsesNonExemptEncryption](./itsappusesnonexemptencryption.md)
  A Boolean value indicating whether the app uses encryption.
- [ITSEncryptionExportComplianceCode](./itsencryptionexportcompliancecode.md)
  The export compliance code provided by App Store Connect for apps that require it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nssystemadministrationusagedescription)*