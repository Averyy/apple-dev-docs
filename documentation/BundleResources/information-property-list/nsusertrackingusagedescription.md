# NSUserTrackingUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that explains the purpose for accessing data that an app can use to track a person or device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- tvOS 14.0+
- visionOS 1.0+



**Type**: string

#### Discussion

If your application uses the [`App Tracking Transparency`](https://developer.apple.com/documentation/apptrackingtransparency) framework, you need to provide a *usage-description string* to explain the purpose for accessing app-related data that the app can use to track a person or device. The system displays the string in a modal UI from which the person can grant or deny permission to access the tracking data.

This key is required. Your app crashes if it attempts to use the [`App Tracking Transparency`](https://developer.apple.com/documentation/apptrackingtransparency) framework without including the key in your target’s properties in Xcode.

The system displays this key’s string in a modal UI when your app requests authorization to access app-related data that the app can use to track the person or the device by calling either method:

- [`requestTrackingAuthorization(completionHandler:)`](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:))
- [`requestTrackingAuthorization(usingExpandedInterface:additionalInformationAction:completionHandler:)`](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(usingexpandedinterface:additionalinformationaction:completionhandler:))

> ❗ **Important**: Alternatively, in the European Union, your app can provide a tracking-usage description that supports rich text elements by using markdown format (see [`NSUserTrackingMarkdownUsageDescription`](information-property-list/nsusertrackingmarkdownusagedescription.md)).

Keep the text of your description short and specific. The system displays your app name in the prompt, so you don’t need to include it in the string. For example usage descriptions, see [`Apple’s Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/).

## See Also

- [NSUpdateSecurityPolicy](information-property-list/nsupdatesecuritypolicy.md)
  A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.
- [NSAppBundlesUsageDescription](information-property-list/nsappbundlesusagedescription.md)
  A message that tells people why the app needs to access the contents of other apps’ bundles.
- [NSAppDataUsageDescription](information-property-list/nsappdatausagedescription.md)
  A message that tells people why the app needs to access files in other apps’ sandbox containers.
- [NSUserTrackingMarkdownUsageDescription](information-property-list/nsusertrackingmarkdownusagedescription.md)
  A message that explains the purpose for accessing data that an application can use to track a person or device.
- [NSAppleEventsUsageDescription](information-property-list/nsappleeventsusagedescription.md)
  A message that tells people why the app is requesting the ability to send Apple events.
- [NSSystemAdministrationUsageDescription](information-property-list/nssystemadministrationusagedescription.md)
  A message in macOS that tells people why the app is requesting to manipulate the system configuration.
- [ITSAppUsesNonExemptEncryption](information-property-list/itsappusesnonexemptencryption.md)
  A Boolean value indicating whether the app uses encryption.
- [ITSEncryptionExportComplianceCode](information-property-list/itsencryptionexportcompliancecode.md)
  The export compliance code provided by App Store Connect for apps that require it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsusertrackingusagedescription)*