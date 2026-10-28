# Default Dialer App

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether an app can be the default dialer app on someone’s device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Details

- **Name**: `com.apple.developer.dialing-app`
- **Type**: boolean



**Default**: `NO`

## Discussion

Add the Default Dialer App entitlement by following these steps:

1. In the Xcode project navigator, select your app’s target, and then the Signing & Capabilities tab.
2. Add a new capability by clicking the + Capability button and then type “Default Dialer” in the search field.
3. Double-click the Default Dialer App entry to add the entitlement to your app.

Xcode displays the Default Dialer App entitlement, along with any other entitlements, in the capabilities list under your app’s signing information. For more information about becoming the default dialer app, refer to [Preparing your app to be the default dialer app](../../LiveCommunicationKit/preparing-your-app-to-be-the-default-dialer-app.md).

## See Also

### LiveCommunicationKit
- [Default Calling App](./com.apple.developer.calling-app.md)
  A Boolean value that indicates whether an app can be the default calling app on someone’s device.
- [com.apple.developer.conversation-accessibility](./com.apple.developer.conversation-accessibility.md)
  A Boolean value that indicates whether the app can provide live assistance services, such as sign language interpreting or captioning, during FaceTime calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.dialing-app)*