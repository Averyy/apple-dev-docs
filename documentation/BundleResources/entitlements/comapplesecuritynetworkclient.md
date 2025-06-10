# com.apple.security.network.client

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether your app may open outgoing network connections.

**Availability**:
- macOS 10.7+

#### Discussion

Use this key to allow your sandboxed app to connect to a server process running on another machine, or on the same machine.

> **Note**:  For TCP sockets, the `com.apple.security.network.client` and [`com.apple.security.network.server`](entitlements/com.apple.security.network.server.md) entitlements restrict only the initiation of a network connection, not the flow of data. Outgoing and incoming connections can both send and receive data. For UDP sockets, the network entitlements restrict both initiation and data flow. For example, an app with only the client entitlement enabled can send, but not receive, data. Apps using UDP usually require both entitlements.

To add this entitlement to your app, enable the App Sandbox capability in Xcode, and under Network, select Outgoing Connections (Client).

## See Also

- [com.apple.security.network.server](entitlements/com.apple.security.network.server.md)
  A Boolean value indicating whether your app may listen for incoming network connections.
- [App Attest Environment](entitlements/com.apple.developer.devicecheck.appattest-environment.md)
  The environment for an app that uses the App Attest service to validate itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.network.client)*