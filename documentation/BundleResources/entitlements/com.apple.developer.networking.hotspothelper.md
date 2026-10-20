# HotSpot Helper

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An entitlement that permits an app to participate in navigating Wi-Fi network hotspots.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+

## Details

- **Name**: `com.apple.developer.networking.HotspotHelper`
- **Type**: boolean



**Default**: `true`

#### Discussion

Add this entitlement to your app to use the [Hotspot helper](../../NetworkExtension/hotspot-helper.md) API. For more information, see [TN3111: iOS Wi-Fi API overview](../../Technotes/tn3111-ios-wifi-api-overview.md).

To request this entitlement for your app, [fill out the request form](https://developer.apple.com/contact/request/hotspot-helper/).

## See Also

### Wireless interfaces
- [Access Wi-Fi Information Entitlement](./com.apple.developer.networking.wifi-info.md)
  A Boolean value indicating whether your app can access information about the connected Wi-Fi network.
- [Wireless Accessory Configuration Entitlement](./com.apple.external-accessory.wireless-configuration.md)
  A Boolean value that indicates whether your app may configure MFi Wi-Fi accessories.
- [Multipath Entitlement](./com.apple.developer.networking.multipath.md)
  A Boolean value indicating whether your app may use Multipath protocols to seamlessly transition between Wi-Fi and cellular networks.
- [Hotspot Configuration Entitlement](./com.apple.developer.networking.hotspotconfiguration.md)
  A Boolean value indicating whether your app can use the hotspot manager to configure Wi-Fi networks.
- [ISO18092 system codes for NFC Tag Reader Session](./com.apple.developer.nfc.readersession.felica.systemcodes.md)
  A list of FeliCa system codes that the app supports.
- [Near Field Communication Tag Reader Session Formats Entitlement](./com.apple.developer.nfc.readersession.formats.md)
  The Near Field Communication data formats an app can read.
- [ISO7816 application identifiers for NFC Tag Reader Session](./com.apple.developer.nfc.readersession.iso7816.select-identifiers.md)
  A list of application identifiers that the app supports.
- [com.apple.developer.nfc.hce](./com.apple.developer.nfc.hce.md)
  A Boolean value indicating whether your app can use the card session API.
- [com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes](./com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes.md)
  An array of identifier strings the app handles with the card session API.
- [com.apple.developer.nfc.hce.default-contactless-app](./com.apple.developer.nfc.hce.default-contactless-app.md)
  A Boolean value indicating whether your app can be a default app for contactless NFC with the card session API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.networking.hotspothelper)*