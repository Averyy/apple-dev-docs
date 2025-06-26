# Audio Input Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app may record audio using the built-in microphone and access audio input using Core Audio.

**Availability**:
- macOS 10.7+

#### Discussion

To add this entitlement to your app, first enable the Hardened Runtime capability in Xcode, and then under Resource Access, select Audio Input.

## See Also

- [Camera entitlement](entitlements/com.apple.security.device.camera.md)
  A Boolean value that indicates whether the app may interact with the built-in and external cameras, and capture movies and still images.
- [com.apple.security.device.microphone](entitlements/com.apple.security.device.microphone.md)
  A Boolean value that indicates whether the app may use the microphone.
- [com.apple.security.device.usb](entitlements/com.apple.security.device.usb.md)
  A Boolean value indicating whether your app may interact with USB devices.
- [com.apple.security.print](entitlements/com.apple.security.print.md)
  A Boolean value indicating whether your app may print a document.
- [com.apple.security.device.bluetooth](entitlements/com.apple.security.device.bluetooth.md)
  A Boolean value indicating whether your app may interact with Bluetooth devices.
- [com.apple.security.smartcard](entitlements/com.apple.security.smartcard.md)
  A Boolean that indicates whether your app has access to smart card slots and smart cards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.device.audio-input)*