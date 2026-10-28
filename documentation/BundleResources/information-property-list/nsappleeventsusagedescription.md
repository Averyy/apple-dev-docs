# NSAppleEventsUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A message that tells people why the app is requesting the ability to send Apple events.

**Availability**:
- macOS 10.14+

## Details

- **Name**: `NSAppleEventsUsageDescription` (Privacy - AppleEvents Sending Usage Description)
- **Type**: string

## Discussion

An app using Apple events to control another app might be able to gain access to sensitive user data. For example, the Mail app stores a lot of personal information in its local database that other apps can’t access directly. But because Mail can be automated with Apple events, other apps can use Mail to gain access to the data indirectly.

> ❗ **Important**:  This key is required if your app uses APIs that send Apple events.

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
- [NSSystemAdministrationUsageDescription](./nssystemadministrationusagedescription.md)
  A message in macOS that tells people why the app is requesting to manipulate the system configuration.
- [ITSAppUsesNonExemptEncryption](./itsappusesnonexemptencryption.md)
  A Boolean value indicating whether the app uses encryption.
- [ITSEncryptionExportComplianceCode](./itsencryptionexportcompliancecode.md)
  The export compliance code provided by App Store Connect for apps that require it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsappleeventsusagedescription)*