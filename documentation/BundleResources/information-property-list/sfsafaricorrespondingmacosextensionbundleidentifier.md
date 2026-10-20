# SFSafariCorrespondingMacOSExtensionBundleIdentifier

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A string bundle ID that identifies the corresponding content blocker extension or Safari web extension on macOS.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Details

- **Name**: `SFSafariCorrespondingMacOSExtensionBundleIdentifier` (Safari - Associated macOS Extension Bundle Identifier)
- **Type**: string

#### Discussion

To enable extension syncing for your iOS content blocker extension or Safari web extension, specify the bundle ID of the corresponding macOS content blocker extension or Safari web extension.

Only add this to your `Info.plist` if the bundle ID for your iOS app is different from the bundle ID for your macOS app.

For more information, see [Syncing Safari web extensions across devices and platforms](../../SafariServices/syncing-safari-web-extensions-across-devices-and-platforms.md).

## See Also

### Safari services
- [SFSafariCorrespondingIOSAppBundleIdentifier](./sfsafaricorrespondingiosappbundleidentifier.md)
  A string bundle ID that identifies the corresponding iOS app that contains a content blocker or Safari web extension.
- [SFSafariCorrespondingIOSExtensionBundleIdentifier](./sfsafaricorrespondingiosextensionbundleidentifier.md)
  A string bundle ID that identifies the corresponding content blocker extension or Safari web extension on iOS.
- [SFSafariCorrespondingMacOSAppBundleIdentifier](./sfsafaricorrespondingmacosappbundleidentifier.md)
  A string bundle ID that identifies the corresponding macOS app that contains a content blocker or Safari web extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/sfsafaricorrespondingmacosextensionbundleidentifier)*