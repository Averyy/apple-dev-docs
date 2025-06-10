# com.apple.security.network.server

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether your app may listen for incoming network connections.

**Availability**:
- macOS 10.7+

#### Discussion

Use this key to allow other computers to initiate network connections to your sandboxed app.

> **Note**:  For TCP sockets, the `com.apple.security.network.server` and [`com.apple.security.network.client`](entitlements/com.apple.security.network.client.md) entitlements restrict only the initiation of a network connection, not the flow of data. Outgoing and incoming connections can both send and receive data. For UDP sockets, the network entitlements restrict both initiation and data flow. For example, an app with only the server entitlement enabled can receive, but not send, data. Apps using UDP usually require both entitlements.

To add this entitlement to your app, enable the App Sandbox capability in Xcode, and under Network, select Incoming Connections (Server).

## See Also

- [com.apple.security.network.client](entitlements/com.apple.security.network.client.md)
  A Boolean value indicating whether your app may open outgoing network connections.
- [App Attest Environment](entitlements/com.apple.developer.devicecheck.appattest-environment.md)
  The environment for an app that uses the App Attest service to validate itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.network.server)*