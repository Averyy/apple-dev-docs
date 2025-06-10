# Default Dialer App

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an app can be the default dialer app on someone’s device.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

#### Discussion

Add the Default Dialer App entitlement by following these steps:

1. In the Xcode project navigator, select your app’s target, and then the Signing & Capabilities tab.
2. Add a new capability by clicking the + Capability button and then type “Default Dialer” in the search field.
3. Double-click the Default Dialer App entry to add the entitlement to your app.

Xcode displays the Default Dialer App entitlement, along with any other entitlements, in the capabilities list under your app’s signing information. For more information about becoming the default dialer app, refer to [`Preparing your app to be the default dialer app`](https://developer.apple.com/documentation/LiveCommunicationKit/preparing-your-app-to-be-the-default-dialer-app).

## See Also

- [Default Calling App](entitlements/com.apple.developer.calling-app.md)
  A Boolean value that indicates whether an app can be the default calling app on someone’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.dialing-app)*