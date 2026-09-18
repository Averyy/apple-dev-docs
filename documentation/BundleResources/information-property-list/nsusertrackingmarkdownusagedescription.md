# NSUserTrackingMarkdownUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that explains the purpose for accessing data that an application can use to track a person or device.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)



**Type**: string

#### Discussion

If your application uses the [`App Tracking Transparency`](https://developer.apple.com/documentation/apptrackingtransparency) framework, use this key to provide a *usage-description string* to explain your app’s purpose for accessing data that the app can use to track the person or the device. The system displays the string value in a full-page authorization sheet from which the person can grant or deny permission to access the tracking data.

The format of the string is Markdown text; you can apply bold or italic style, but it doesn’t support underline. You can include bullet lists and paragraph breaks.

This key is optional. The system uses the [`NSUserTrackingUsageDescription`](information-property-list/nsusertrackingusagedescription.md) if your app’s target properties omit this key.

This key has regional availability. To use this key, the system requires that the device be located in a specific European Union (EU) country and signed in with an Apple Account that has its country or region set to a specific EU country or region:

- **France, Germany, Italy, Poland, and Romania**: The system uses this key, if available.
- **The European Union**: The system uses this key if available when your app calls [`requestTrackingAuthorization(usingExpandedInterface:additionalInformationAction:completionHandler:)`](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(usingexpandedinterface:additionalinformationaction:completionhandler:)), passing `preferExpandedInterface` a value of `true`.

Outside of the EU, the system uses the [`NSUserTrackingUsageDescription`](information-property-list/nsusertrackingusagedescription.md) key instead of this key.

> 💡 **Tip**: Keep the text of your description short and specific. The system displays your app name in the prompt so you don’t need to include it in the string. For example usage descriptions, see [`Apple’s Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/).

## See Also

- [NSUpdateSecurityPolicy](information-property-list/nsupdatesecuritypolicy.md)
  A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.
- [NSAppBundlesUsageDescription](information-property-list/nsappbundlesusagedescription.md)
  A message that tells people why the app needs to access the contents of other apps’ bundles.
- [NSAppDataUsageDescription](information-property-list/nsappdatausagedescription.md)
  A message that tells people why the app needs to access files in other apps’ sandbox containers.
- [NSUserTrackingUsageDescription](information-property-list/nsusertrackingusagedescription.md)
  A message that explains the purpose for accessing data that an app can use to track a person or device.
- [NSAppleEventsUsageDescription](information-property-list/nsappleeventsusagedescription.md)
  A message that tells people why the app is requesting the ability to send Apple events.
- [NSSystemAdministrationUsageDescription](information-property-list/nssystemadministrationusagedescription.md)
  A message in macOS that tells people why the app is requesting to manipulate the system configuration.
- [ITSAppUsesNonExemptEncryption](information-property-list/itsappusesnonexemptencryption.md)
  A Boolean value indicating whether the app uses encryption.
- [ITSEncryptionExportComplianceCode](information-property-list/itsencryptionexportcompliancecode.md)
  The export compliance code provided by App Store Connect for apps that require it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsusertrackingmarkdownusagedescription)*