# SCNetworkServiceEstablishDefaultConfiguration(_:)

**Framework**: System Configuration  
**Kind**: func

Establishes the default configuration for the specified network service.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SCNetworkServiceEstablishDefaultConfiguration(_ service: SCNetworkService) -> Bool
```

#### Return Value

`TRUE` if the configuration was updated; `FALSE` if an error occurred.

#### Discussion

The default configuration includes the addition of network protocols for the service (with default configuration options).

## Parameters

- `service`: The network service.

## See Also

- [func SCNetworkServiceAddProtocolType(SCNetworkService, CFString) -> Bool](scnetworkserviceaddprotocoltype(_:_:).md)
  Adds the network protocol of the specified type to the specified service.
- [func SCNetworkServiceCopy(SCPreferences, CFString) -> SCNetworkService?](scnetworkservicecopy(_:_:).md)
  Returns the network service with the specified identifier.
- [func SCNetworkServiceCopyAll(SCPreferences) -> CFArray?](scnetworkservicecopyall(_:).md)
  Returns all available network services for the specified preferences.
- [func SCNetworkServiceCopyProtocol(SCNetworkService, CFString) -> SCNetworkProtocol?](scnetworkservicecopyprotocol(_:_:).md)
  Returns the network protocol of the specified type for the specified service.
- [func SCNetworkServiceCopyProtocols(SCNetworkService) -> CFArray?](scnetworkservicecopyprotocols(_:).md)
  Returns all network protocols associated with the specified service.
- [func SCNetworkServiceCreate(SCPreferences, SCNetworkInterface) -> SCNetworkService?](scnetworkservicecreate(_:_:).md)
  Creates a new network service for the specified interface in the configuration.
- [func SCNetworkServiceGetEnabled(SCNetworkService) -> Bool](scnetworkservicegetenabled(_:).md)
  Returns a Boolean value indicating whether the specified service is enabled.
- [func SCNetworkServiceGetInterface(SCNetworkService) -> SCNetworkInterface?](scnetworkservicegetinterface(_:).md)
  Returns the network interface associated with the specified service.
- [func SCNetworkServiceGetName(SCNetworkService) -> CFString?](scnetworkservicegetname(_:).md)
  Returns the user-specified name associated with the specified service.
- [func SCNetworkServiceGetServiceID(SCNetworkService) -> CFString?](scnetworkservicegetserviceid(_:).md)
  Returns the identifier for the specified service.
- [func SCNetworkServiceGetTypeID() -> CFTypeID](scnetworkservicegettypeid().md)
  Returns the type identifier of all `SCNetworkService` instances.
- [func SCNetworkServiceRemove(SCNetworkService) -> Bool](scnetworkserviceremove(_:).md)
  Removes the specified network service from the configuration.
- [func SCNetworkServiceRemoveProtocolType(SCNetworkService, CFString) -> Bool](scnetworkserviceremoveprotocoltype(_:_:).md)
  Removes the network protocol of the specified type from the specified service.
- [func SCNetworkServiceSetEnabled(SCNetworkService, Bool) -> Bool](scnetworkservicesetenabled(_:_:).md)
  Enables or disables the specified service.
- [func SCNetworkServiceSetName(SCNetworkService, CFString?) -> Bool](scnetworkservicesetname(_:_:).md)
  Stores the user-specified name for the specified service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkserviceestablishdefaultconfiguration(_:))*