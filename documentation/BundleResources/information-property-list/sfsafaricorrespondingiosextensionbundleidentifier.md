# SFSafariCorrespondingIOSExtensionBundleIdentifier

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A string bundle ID that identifies the corresponding content blocker extension or Safari web extension on iOS.

**Availability**:
- macOS 13.0+

## Details

- **Name**: `SFSafariCorrespondingIOSExtensionBundleIdentifier` (Safari - Associated iOS Extension Bundle Identifier)
- **Type**: string

#### Discussion

To enable extension syncing for your macOS content blocker extension or Safari web extension, specify the bundle ID of the corresponding iOS content blocker extension or Safari web extension.

Only add this to your `Info.plist` if the bundle ID for your macOS app is different from the bundle ID for your iOS app.

For more information, see [Syncing Safari web extensions across devices and platforms](../../SafariServices/syncing-safari-web-extensions-across-devices-and-platforms.md).

## See Also

### Safari services
- [SFSafariCorrespondingIOSAppBundleIdentifier](./sfsafaricorrespondingiosappbundleidentifier.md)
  A string bundle ID that identifies the corresponding iOS app that contains a content blocker or Safari web extension.
- [SFSafariCorrespondingMacOSAppBundleIdentifier](./sfsafaricorrespondingmacosappbundleidentifier.md)
  A string bundle ID that identifies the corresponding macOS app that contains a content blocker or Safari web extension.
- [SFSafariCorrespondingMacOSExtensionBundleIdentifier](./sfsafaricorrespondingmacosextensionbundleidentifier.md)
  A string bundle ID that identifies the corresponding content blocker extension or Safari web extension on macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/sfsafaricorrespondingiosextensionbundleidentifier)*