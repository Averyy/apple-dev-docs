# NWParametersProvider

**Framework**: Network  
**Kind**: protocol  
**Role**: Protocol

Types that conform to the NWParametersProvider protocol can be used to generate an NWParameters.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol NWParametersProvider
```

## Topics

### Instance Properties
- [var parameters: NWParameters](./nwparametersprovider/parameters.md)
  The generated NWParameters.
### Instance Methods
- [func constrainedPathsProhibited(Bool) -> Self](./nwparametersprovider/constrainedpathsprohibited%28_%29.md)
  Prohibit using constrained paths.
- [func dnssecValidationRequired(Bool) -> Self](./nwparametersprovider/dnssecvalidationrequired%28_%29.md)
  Require DNSSEC validation when resolving an endpoint before making a connection.
- [func expensivePathsProhibited(Bool) -> Self](./nwparametersprovider/expensivepathsprohibited%28_%29.md)
  Prohibit using expensive paths.
- [func expiredDNSBehavior(NWParameters.ExpiredDNSBehavior) -> Self](./nwparametersprovider/expireddnsbehavior%28_%29.md)
  Allow or prohibit the use of expired DNS answers during connection establishment.
- [func fastOpenAllowed(Bool) -> Self](./nwparametersprovider/fastopenallowed%28_%29.md)
  Allow fast open to be used on a connection.
- [func localEndpoint(NWEndpoint?) -> Self](./nwparametersprovider/localendpoint%28_%29.md)
  Specify a specific endpoint to use as the local endpoint.
- [func localEndpointReuseAllowed(Bool) -> Self](./nwparametersprovider/localendpointreuseallowed%28_%29.md)
  Allow local endpoint reuse.
- [func localOnly(Bool) -> Self](./nwparametersprovider/localonly%28_%29.md)
  Limit inbound connections to peers attached to the local link.
- [func localPort(NWEndpoint.Port) -> Self](./nwparametersprovider/localport%28_%29.md)
  Specify a specific port to use as the local endpoint, letting the system select the address.
- [func multipathServiceType(NWParameters.MultipathServiceType) -> Self](./nwparametersprovider/multipathservicetype%28_%29.md)
  Set the multipath service to use for connections.
- [func noProxiesPreferred(Bool) -> Self](./nwparametersprovider/noproxiespreferred%28_%29.md)
  Prefer not using proxies when making connections.
- [func peerToPeerIncluded(Bool) -> Self](./nwparametersprovider/peertopeerincluded%28_%29.md)
  Include peer-to-peer interfaces when connecting, listening, and browsing.
- [func prohibitedInterfaceTypes([NWInterface.InterfaceType]) -> Self](./nwparametersprovider/prohibitedinterfacetypes%28_%29.md)
  Prohibit certain interface types from being used to connect, listen, and browse.
- [func prohibitedInterfaces([NWInterface]) -> Self](./nwparametersprovider/prohibitedinterfaces%28_%29.md)
  Prohibit certain interfaces from being used to connect, listen, and browse.
- [func requiredInterface(NWInterface) -> Self](./nwparametersprovider/requiredinterface%28_%29.md)
  Require an interface when connecting, listening, and browsing.
- [func requiredInterfaceType(NWInterface.InterfaceType) -> Self](./nwparametersprovider/requiredinterfacetype%28_%29.md)
  Require an interface type when connecting, listening, and browsing.
- [func serviceClass(NWParameters.ServiceClass) -> Self](./nwparametersprovider/serviceclass%28_%29.md)
  Set the data service class to use for connections.
- [func ultraConstrainedPathsAllowed(Bool) -> Self](./nwparametersprovider/ultraconstrainedpathsallowed%28_%29.md)
  Allow connection to use interfaces considered ultra-constrained by the system

## Relationships

### Conforming Types
- [NWParameters](./nwparameters.md)
- [NWParametersBuilder](./nwparametersbuilder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider)*