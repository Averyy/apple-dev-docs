# Inter-App Audio Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app may exchange audio with other Inter-App Audio-enabled apps.

**Availability**:
- iOS 2.2+ - Deprecated in 13.0
- iPadOS 2.2+ - Deprecated in 13.0

> **Deprecated**: Inter-App Audio is deprecated in iOS 13 and is unavailable when running iPad apps in macOS.

## Details

- **Name**: `inter-app-audio` (Inter-App Audio)
- **Type**: boolean

#### Discussion

Enabling Inter-App Audio allows your app to send and receive audio from other Inter-App Audio enabled apps and provides access to Audio Unit extensions.

To add this entitlement to your app, enable the Inter-App Audio capability in Xcode.

## See Also

### Deprecated entitlements
- [Maps Entitlement](./com.apple.developer.maps.md)
  A Boolean value that indicates whether the app may provide directions beyond what Maps supports, such as subway routes, hiking trails, and bike paths.
- [All files entitlement](./com.apple.security.files.all.md)
  A Boolean value that indicates whether the app may have access to all files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/inter-app-audio)*