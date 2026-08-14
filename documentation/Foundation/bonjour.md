# Bonjour

**Framework**: Foundation

Advertise services for easy discovery on local networks, or discover services advertised by others.

## Topics

### Local Network Services
- [class NetService](netservice.md)
  A network service that broadcasts its availability using multicast DNS.
- [protocol NetServiceDelegate](netservicedelegate.md)
  The interface a net service uses to inform its delegate about the state of the service it offers.
- [NSBonjourServices](../bundleresources/information-property-list/nsbonjourservices.md)
  Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../bundleresources/information-property-list/nslocalnetworkusagedescription.md)
  A message that tells people why the app is requesting access to the local network.
### Service Discovery
- [class NetServiceBrowser](netservicebrowser.md)
  A network service browser that finds published services on a network using multicast DNS.
- [protocol NetServiceBrowserDelegate](netservicebrowserdelegate.md)
  The interface a net service browser uses to inform a delegate about the state of service discovery.

## See Also

- [URL Loading System](url-loading-system.md)
  Interact with URLs and communicate with servers using standard Internet protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bonjour)*