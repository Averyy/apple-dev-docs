# NEProvider

**Framework**: Network Extension  
**Kind**: class

An abstract base class for all NetworkExtension providers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEProvider
```

#### Overview

See the documentation for the `NEProvider` subclasses for details about how to create Network Extension Provider extensions.

The `NEProvider` class and its subclasses expose methods and properties that allow Network Extension Provider extensions to participate in and affect the network data path on iOS and macOS. For example, the `handleNewFlow:` method in [`NEFilterDataProvider`](nefilterdataprovider.md) allows Filter Data Provider extensions to make pass/block decisions on TCP connections as the connections are established on the system.

##### Subclassing Notes

The `NEProvider` class should not be subclassed directly. Instead, you should create subclasses of `NEProvider` subclasses (and in some cases subsubclasses).

###### Methods to Override

- [`sleep(completionHandler:)`](neprovider/sleep(completionhandler:).md)
- [`wake()`](neprovider/wake().md)

## Topics

### Handling sleep and wake
- [func sleep(completionHandler: () -> Void)](neprovider/sleep(completionhandler:).md)
  Handle a sleep event.
- [func wake()](neprovider/wake.md)
  Handle a wake event.
### Creating network connections
- [func createTCPConnection(to: NWEndpoint, enableTLS: Bool, tlsParameters: NWTLSParameters?, delegate: Any?) -> NWTCPConnection](neprovider/createtcpconnection(to:enabletls:tlsparameters:delegate:).md)
  Create a TCP connection.
- [func createUDPSession(to: NWEndpoint, from: NWHostEndpoint?) -> NWUDPSession](neprovider/createudpsession(to:from:).md)
  Creates a UDP session.
### Monitoring the network state
- [var defaultPath: NWPath?](neprovider/defaultpath.md)
  The current default network path used for connections created by the provider.
### Supporting system extensions
- [class func startSystemExtensionMode()](neprovider/startsystemextensionmode.md)
  Starts the Network Extension machinery from inside a System Extension.
### Constants
- [enum NEProviderStopReason](neproviderstopreason.md)
  Reasons why the provider extension was stopped.
### Displaying messages
- [func displayMessage(String, completionHandler: (Bool) -> Void)](neprovider/displaymessage(_:completionhandler:).md)
  Call this method from your [`NEProvider`](neprovider.md) subclass if you want to display a message to the person using the app.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NEAppPushProvider](neapppushprovider.md)
- [NEDNSProxyProvider](nednsproxyprovider.md)
- [NEFilterProvider](nefilterprovider.md)
- [NETunnelProvider](netunnelprovider.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEAppProxyProvider](neappproxyprovider.md)
  The principal class for an app proxy provider app extension.
- [class NETunnelProvider](netunnelprovider.md)
  An abstract base class shared by NEPacketTunnelProvider and NEAppProxyProvider.
- [class NETunnelNetworkSettings](netunnelnetworksettings.md)
  The configuration for a tunnel provider’s virtual interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neprovider)*