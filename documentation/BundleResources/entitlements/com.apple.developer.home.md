# com.apple.developer.home

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

**Availability**:
- iOS 27.2+
- iPadOS 27.2+

## Details

- **Name**: `com.apple.developer.home`
- **Type**: boolean

## Discussion

Add this entitlement to a Home app extension that uses the Home Extensions framework to provide content for accessories in the Home app. Xcode adds the entitlement when you add a Home Extension target to your project.

If your extension communicates with HomeKit or Matter accessories, it also needs the corresponding entitlements, such as [HomeKit Entitlement](./com.apple.developer.homekit.md) and [Matter Allow Setup Payload](./com.apple.developer.matter.allow-setup-payload.md).

## See Also

### Related Documentation
- [HomeKit Entitlement](./com.apple.developer.homekit.md)
  A Boolean value that indicates whether users of the app may manage HomeKit-compatible accessories.
### Home automation
- [HomeKit Entitlement](./com.apple.developer.homekit.md)
  A Boolean value that indicates whether users of the app may manage HomeKit-compatible accessories.
- [Matter Allow Setup Payload](./com.apple.developer.matter.allow-setup-payload.md)
  A Boolean value that allows an app to provide an optional Matter Setup payload while setting up a Matter device in an ecosystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.home)*