# NEAppProxyProvider

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

The principal class for an app proxy provider app extension.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class NEAppProxyProvider
```

```objc
@interface NEAppProxyProvider : NETunnelProvider
```

## Mentions

- [Handling Flow Copying](./handling-flow-copying.md)

## Overview

The [`NEAppProxyProvider`](./neappproxyprovider.md) class provides access to flows of network data in the form of [`NEAppProxyFlow`](./neappproxyflow.md) objects. Each [`NEAppProxyFlow`](./neappproxyflow.md) object corresponds to a socket opened by an app that matches the app rules specified in the current App Proxy configuration. Your App Proxy Provider acts as a transparent network proxy for the flows of network data that it receives.

> ❗ **Important**:  The `com.apple.developer.networking.networkextension` entitlement is required to use the [`NEAppProxyProvider`](./neappproxyprovider.md) class. Enable this entitlement when creating an App ID in your developer account.

### DNS Handling

In addition to flows of raw network data from applications, the App Proxy Provider also receives flows of DNS queries in the form of [`NEAppProxyUDPFlow`](./neappproxyudpflow.md) objects. DNS query flows are received only for applications that use low-level DNS resolution APIs such as [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](../dnssd/dnsservicegetaddrinfo%28_,_,_,_,_,_,_%29.md)(). The App Proxy Provider can specify the DNS resolver configuration that will be used by these applications using the [`setTunnelNetworkSettings(_:completionHandler:)`](./netunnelprovider/settunnelnetworksettings%28_,completionhandler%29.md) method.

Applications that use higher-level networking APIs such as [`URLSession`](../Foundation/urlsession.md) and [`NSURLConnection`](../Foundation/nsurlconnection.md) do not generate DNS queries. Instead the destination hostname for the connection is included in the endpoint information of the [`NEAppProxyFlow`](./neappproxyflow.md) object.

### Creating an App Proxy Provider Extension

App Proxy Providers run as App Extensions for the `com.apple.networkextension.app-proxy` extension point.

To create a App Proxy Provider extension, first create a new App Extension target in your project.

For an example of an Xcode build target for this app extension, see the [SimpleTunnel: Customized Networking Using the NetworkExtension Framework](https://developer.apple.com/library/archive/samplecode/SimpleTunnel/Introduction/Intro.html#//apple_ref/doc/uid/TP40016140) sample code project.

Once you have a App Proxy Provider extension target, create a sub-class of `NEAppProxyProvider`. Then, set the `NSExtensionPrincipalClass` key in the the extension’s `Info.plist` to the name of your sub-class.

If it is not already done, set the `NSExtensionPointIdentifier` key in the extension’s `Info.plist` to `com.apple.networkextension.app-proxy`.

Here is an example of the NSExtension dictionary in a App Proxy Provider extension’s `Info.plist`:

```xml
<key>NSExtension</key>
<dict>
    <key>NSExtensionPointIdentifier</key>
    <string>com.apple.networkextension.app-proxy</string>
    <key>NSExtensionPrincipalClass</key>
    <string>MyCustomAppProxyProvider</string>
</dict>
```

Finally, add your App Proxy Provider extension target to your app’s Embed App Extensions build phase.

### Subclassing Notes

In order to create a App Proxy Provider extension, you must create a subclass of `NEAppProxyProvider` and override the methods listed below.

#### Methods to Override

- [`startProxy(options:completionHandler:)`](./neappproxyprovider/startproxy%28options,completionhandler%29.md)
- [`stopProxy(with:completionHandler:)`](./neappproxyprovider/stopproxy%28with,completionhandler%29.md)
- [`handleNewFlow(_:)`](./neappproxyprovider/handlenewflow%28_%29.md)

## Topics

### Managing the app proxy life cycle
- [func startProxy(options: [String : Any]?, completionHandler: ((any Error)?) -> Void)](./neappproxyprovider/startproxy%28options,completionhandler%29.md)
  Start the network proxy.
- [func stopProxy(with: NEProviderStopReason, completionHandler: () -> Void)](./neappproxyprovider/stopproxy%28with,completionhandler%29.md)
  Stop the network proxy.
- [func cancelProxyWithError((any Error)?)](./neappproxyprovider/cancelproxywitherror%28_%29.md)
  Stop the network proxy from the App Proxy Provider.
### Handling proxied flows
- [func handleNewFlow(NEAppProxyFlow) -> Bool](./neappproxyprovider/handlenewflow%28_%29.md)
  Handle a new flow of network data.
- [func handleNewUDPFlow(NEAppProxyUDPFlow, initialRemoteEndpoint: NWEndpoint) -> Bool](./neappproxyprovider/handlenewudpflow%28_,initialremoteendpoint%29.md)
  Handle a new UDP flow of network data.
### Instance Methods
- [- handleNewUDPFlow:initialRemoteFlowEndpoint:](./neappproxyprovider/handlenewudpflow_initialremoteflowendpoint_.md)

## Relationships

### Inherits From
- [NETunnelProvider](./netunnelprovider.md)
### Inherited By
- [NETransparentProxyProvider](./netransparentproxyprovider.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### App proxy provider
- [class NETunnelProvider](./netunnelprovider.md)
  An abstract base class shared by NEPacketTunnelProvider and NEAppProxyProvider.
- [class NEProvider](./neprovider.md)
  An abstract base class for all NetworkExtension providers.
- [class NETunnelNetworkSettings](./netunnelnetworksettings.md)
  The configuration for a tunnel provider’s virtual interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyprovider)*