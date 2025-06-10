# NWParametersProvider

**Framework**: Network  
**Kind**: protocol

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
protocol NWParametersProvider
```

## Topics

### Instance Properties
- [var parameters: NWParameters](nwparametersprovider/parameters.md)
### Instance Methods
- [func constrainedPathsProhibited(Bool) -> Self](nwparametersprovider/constrainedpathsprohibited(_:).md)
- [func dnssecValidationRequired(Bool) -> Self](nwparametersprovider/dnssecvalidationrequired(_:).md)
- [func expensivePathsProhibited(Bool) -> Self](nwparametersprovider/expensivepathsprohibited(_:).md)
- [func expiredDNSBehavior(NWParameters.ExpiredDNSBehavior) -> Self](nwparametersprovider/expireddnsbehavior(_:).md)
- [func fastOpenAllowed(Bool) -> Self](nwparametersprovider/fastopenallowed(_:).md)
- [func localEndpoint(NWEndpoint?) -> Self](nwparametersprovider/localendpoint(_:).md)
- [func localEndpointReuseAllowed(Bool) -> Self](nwparametersprovider/localendpointreuseallowed(_:).md)
- [func localOnly(Bool) -> Self](nwparametersprovider/localonly(_:).md)
- [func multipathServiceType(NWParameters.MultipathServiceType) -> Self](nwparametersprovider/multipathservicetype(_:).md)
- [func noProxiesPreferred(Bool) -> Self](nwparametersprovider/noproxiespreferred(_:).md)
- [func peerToPeerIncluded(Bool) -> Self](nwparametersprovider/peertopeerincluded(_:).md)
- [func prohibitedInterfaceTypes([NWInterface.InterfaceType]?) -> Self](nwparametersprovider/prohibitedinterfacetypes(_:).md)
- [func prohibitedInterfaces([NWInterface?]?) -> Self](nwparametersprovider/prohibitedinterfaces(_:).md)
- [func requiredInterface(NWInterface?) -> Self](nwparametersprovider/requiredinterface(_:).md)
- [func requiredInterfaceType(NWInterface.InterfaceType) -> Self](nwparametersprovider/requiredinterfacetype(_:).md)
- [func serviceClass(NWParameters.ServiceClass) -> Self](nwparametersprovider/serviceclass(_:).md)

## Relationships

### Conforming Types
- [NWParameters](nwparameters.md)
- [NWParametersBuilder](nwparametersbuilder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider)*