# NEProvider

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

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

```objc
@interface NEProvider : NSObject
```

#### Overview

See the documentation for the `NEProvider` subclasses for details about how to create Network Extension Provider extensions.

The `NEProvider` class and its subclasses expose methods and properties that allow Network Extension Provider extensions to participate in and affect the network data path on iOS and macOS. For example, the `handleNewFlow:` method in [`NEFilterDataProvider`](./nefilterdataprovider.md) allows Filter Data Provider extensions to make pass/block decisions on TCP connections as the connections are established on the system.

##### Subclassing Notes

The `NEProvider` class should not be subclassed directly. Instead, you should create subclasses of `NEProvider` subclasses (and in some cases subsubclasses).

###### Methods to Override

- [`sleep(completionHandler:)`](./neprovider/sleep%28completionhandler%29.md)
- [`wake()`](./neprovider/wake%28%29.md)

## Topics

### Handling sleep and wake
- [func sleep(completionHandler: () -> Void)](./neprovider/sleep%28completionhandler%29.md)
  Handle a sleep event.
- [func wake()](./neprovider/wake%28%29.md)
  Handle a wake event.
### Creating network connections
- [func createTCPConnection(to: NWEndpoint, enableTLS: Bool, tlsParameters: NWTLSParameters?, delegate: Any?) -> NWTCPConnection](./neprovider/createtcpconnection%28to,enabletls,tlsparameters,delegate%29.md)
  Create a TCP connection.
- [func createUDPSession(to: NWEndpoint, from: NWHostEndpoint?) -> NWUDPSession](./neprovider/createudpsession%28to,from%29.md)
  Creates a UDP session.
### Monitoring the network state
- [var defaultPath: NWPath?](./neprovider/defaultpath.md)
  The current default network path used for connections created by the provider.
### Supporting system extensions
- [class func startSystemExtensionMode()](./neprovider/startsystemextensionmode%28%29.md)
  Starts the Network Extension machinery from inside a System Extension.
### Constants
- [enum NEProviderStopReason](./neproviderstopreason.md)
  Reasons why the provider extension was stopped.
### Displaying messages
- [func displayMessage(String, completionHandler: (Bool) -> Void)](./neprovider/displaymessage%28_,completionhandler%29.md)
  Call this method from your [`NEProvider`](./neprovider.md) subclass if you want to display a message to the person using the app.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NEAppPushProvider](./neapppushprovider.md)
- [NEDNSProxyProvider](./nednsproxyprovider.md)
- [NEFilterProvider](./nefilterprovider.md)
- [NETunnelProvider](./netunnelprovider.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### App proxy provider
- [class NEAppProxyProvider](./neappproxyprovider.md)
  The principal class for an app proxy provider app extension.
- [class NETunnelProvider](./netunnelprovider.md)
  An abstract base class shared by NEPacketTunnelProvider and NEAppProxyProvider.
- [class NETunnelNetworkSettings](./netunnelnetworksettings.md)
  The configuration for a tunnel provider’s virtual interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neprovider)*