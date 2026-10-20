# NetServiceDelegate

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

The interface a net service uses to inform its delegate about the state of the service it offers.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol NetServiceDelegate : NSObjectProtocol
```

```objc
@protocol NSNetServiceDelegate <NSObject>
```

#### Overview

The [`NetServiceDelegate`](./netservicedelegate.md) protocol defines the optional methods implemented by delegates of [`NetService`](./netservice.md) objects.

## Topics

### Using Network Services
- [func netServiceWillPublish(NetService)](./netservicedelegate/netservicewillpublish%28_%29.md)
  Notifies the delegate that the network is ready to publish the service.
- [func netService(NetService, didNotPublish: [String : NSNumber])](./netservicedelegate/netservice%28_,didnotpublish%29.md)
  Notifies the delegate that a service could not be published.
- [func netServiceDidPublish(NetService)](./netservicedelegate/netservicedidpublish%28_%29.md)
  Notifies the delegate that a service was successfully published.
- [func netServiceWillResolve(NetService)](./netservicedelegate/netservicewillresolve%28_%29.md)
  Notifies the delegate that the network is ready to resolve the service.
- [func netService(NetService, didNotResolve: [String : NSNumber])](./netservicedelegate/netservice%28_,didnotresolve%29.md)
  Informs the delegate that an error occurred during resolution of a given service.
- [func netServiceDidResolveAddress(NetService)](./netservicedelegate/netservicedidresolveaddress%28_%29.md)
  Informs the delegate that the address for a given service was resolved.
- [func netService(NetService, didUpdateTXTRecord: Data)](./netservicedelegate/netservice%28_,didupdatetxtrecord%29.md)
  Notifies the delegate that the TXT record for a given service has been updated.
- [func netServiceDidStop(NetService)](./netservicedelegate/netservicedidstop%28_%29.md)
  Informs the delegate that a [`publish()`](./netservice/publish%28%29.md) or [`resolve(withTimeout:)`](./netservice/resolve%28withtimeout%29.md) request was stopped.
### Accepting Connections
- [func netService(NetService, didAcceptConnectionWith: InputStream, outputStream: OutputStream)](./netservicedelegate/netservice%28_,didacceptconnectionwith,outputstream%29.md)
  Called when a client connects to a service managed by Bonjour.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Local Network Services
- [class NetService](./netservice.md)
  A network service that broadcasts its availability using multicast DNS.
- [NSBonjourServices](../BundleResources/information-property-list/nsbonjourservices.md)
  Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../BundleResources/information-property-list/nslocalnetworkusagedescription.md)
  A message that tells people why the app is requesting access to the local network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicedelegate)*