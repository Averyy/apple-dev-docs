# HomeKit Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether users of the app may manage HomeKit-compatible accessories.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Details

- **Name**: `com.apple.developer.homekit` (HomeKit)
- **Type**: boolean

## Discussion

This key Indicates whether the users of an app may manage HomeKit-compatible accessories, such as switches, lights, fans, locks, and thermostats.

To add this entitlement to your app, enable the HomeKit capability in Xcode. For more information, see [Enabling HomeKit in your app](../../HomeKit/enabling-homekit-in-your-app.md).

## See Also

### Home automation
- [com.apple.developer.home](./com.apple.developer.home.md)
- [Matter Allow Setup Payload](./com.apple.developer.matter.allow-setup-payload.md)
  A Boolean value that allows an app to provide an optional Matter Setup payload while setting up a Matter device in an ecosystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.homekit)*