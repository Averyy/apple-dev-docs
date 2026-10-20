# Camera entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app may interact with the built-in and external cameras, and capture movies and still images.

**Availability**:
- macOS 10.7+

## Details

- **Name**: `com.apple.security.device.camera` (Camera)
- **Type**: boolean

#### Discussion

To add this entitlement to your app, first enable the App Sandbox or Hardened Runtime capability in Xcode, and then select Camera.

In macOS 10.14 and later, the user must explicitly grant permission for each app to access cameras. See [Requesting Authorization for Media Capture on macOS](../requesting-authorization-for-media-capture-on-macos.md).

## See Also

### Device access
- [Audio Input Entitlement](./com.apple.security.device.audio-input.md)
  A Boolean value that indicates whether the app may record audio using the built-in microphone and access audio input using Core Audio.
- [com.apple.security.device.microphone](./com.apple.security.device.microphone.md)
  A Boolean value that indicates whether the app may use the microphone.
- [com.apple.security.device.usb](./com.apple.security.device.usb.md)
  A Boolean value indicating whether your app may interact with USB devices.
- [com.apple.security.print](./com.apple.security.print.md)
  A Boolean value indicating whether your app may print a document.
- [com.apple.security.device.bluetooth](./com.apple.security.device.bluetooth.md)
  A Boolean value indicating whether your app may interact with Bluetooth devices.
- [com.apple.security.smartcard](./com.apple.security.smartcard.md)
  A Boolean that indicates whether your app has access to smart card slots and smart cards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.device.camera)*