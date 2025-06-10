# NEDNSProxyProvider

**Framework**: Network Extension  
**Kind**: class

The principal class for a DNS proxy provider app extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class NEDNSProxyProvider
```

## Mentions

- [Handling Flow Copying](handling-flow-copying.md)

#### Overview

A DNS proxy allows your app to intercept all DNS traffic generated on a device. You can use this capability to provide services like DNS traffic encryption, typically by redirecting DNS traffic to your own server. You usually do this in the context of managed devices, such as those owned by a school or an enterprise.

You create a DNS proxy as an app extension based on a custom subclass of the [`NEDNSProxyProvider`](nednsproxyprovider.md) class. Once active, the proxy receives access to flows of DNS traffic in the form of [`NEAppProxyFlow`](neappproxyflow.md) instances. Each flow corresponds to a socket opened by an app to UDP port 53 or TCP port 53. Your DNS proxy provider acts as a transparent DNS proxy for the flows of network data that it receives.

> ❗ **Important**:  To use the [`NEDNSProxyProvider`](nednsproxyprovider.md) class, you must enable the Network Extensions capability in Xcode and select the DNS Proxy capability. See [`Configure network extensions`](https://developer.apple.comhttp://help.apple.com/xcode/mac/current/#/dev0b2ef6f08).

When you subclass [`NEDNSProxyProvider`](nednsproxyprovider.md), you must provide implementations for the following methods:

- [`startProxy(options:completionHandler:)`](nednsproxyprovider/startproxy(options:completionhandler:).md)
- [`stopProxy(with:completionHandler:)`](nednsproxyprovider/stopproxy(with:completionhandler:).md)
- [`handleNewFlow(_:)`](nednsproxyprovider/handlenewflow(_:).md)

## Topics

### Managing the DNS proxy life cycle
- [func startProxy(options: [String : Any]?, completionHandler: ((any Error)?) -> Void)](nednsproxyprovider/startproxy(options:completionhandler:).md)
  Starts the DNS proxy.
- [func stopProxy(with: NEProviderStopReason, completionHandler: () -> Void)](nednsproxyprovider/stopproxy(with:completionhandler:).md)
  Stops the DNS proxy.
- [func cancelProxyWithError((any Error)?)](nednsproxyprovider/cancelproxywitherror(_:).md)
  Cancels the DNS proxy.
### Handling proxied DNS flow
- [func handleNewFlow(NEAppProxyFlow) -> Bool](nednsproxyprovider/handlenewflow(_:).md)
  Handles a new flow of DNS traffic.
- [func handleNewUDPFlow(NEAppProxyUDPFlow, initialRemoteEndpoint: NWEndpoint) -> Bool](nednsproxyprovider/handlenewudpflow(_:initialremoteendpoint:).md)
  Handles a new flow of UDP traffic.
### Getting system DNS settings
- [var systemDNSSettings: [NEDNSSettings]?](nednsproxyprovider/systemdnssettings.md)
  The current system DNS settings.

## Relationships

### Inherits From
- [NEProvider](neprovider.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEDNSSettings](nednssettings.md)
  The DNS resolver settings of a network tunnel or a system-wide configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxyprovider)*