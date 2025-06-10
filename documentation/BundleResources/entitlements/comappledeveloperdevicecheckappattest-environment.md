# App Attest Environment

**Framework**: Bundle Resources  
**Kind**: typealias

The environment for an app that uses the App Attest service to validate itself.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

#### Discussion

To add this entitlement to your app, add the key to your app’s entitlements file manually, choose the `String` type, and set the associated value to either `development` or `production`. Alternatively, add the App Attest capability to your app target. This adds the entry to the app’s entitlements file with `development` as the associated value. If you omit the entitlement during development, your app uses the App Attest sandbox servers by default. You can test your app during development against the App Attest production servers by setting the entitlement to `production`.

After distributing your app through TestFlight, the App Store, or the Apple Developer Enterprise Program, your app ignores the entitlement you set and uses the production environment.

> ❗ **Important**:  If you use the App Attest service in an App Clip, be sure to add the App Attest capability and the corresponding entry for both your app and your App Clip. Similarly, if you use the App Attest service in your app and an app extension, make sure to configure the capability and the App Attest sandbox environment for both your app and your extension.

## See Also

- [com.apple.security.network.server](entitlements/com.apple.security.network.server.md)
  A Boolean value indicating whether your app may listen for incoming network connections.
- [com.apple.security.network.client](entitlements/com.apple.security.network.client.md)
  A Boolean value indicating whether your app may open outgoing network connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.devicecheck.appattest-environment)*