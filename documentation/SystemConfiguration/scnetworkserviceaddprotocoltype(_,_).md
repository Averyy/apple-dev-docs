# SCNetworkServiceAddProtocolType(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Adds the network protocol of the specified type to the specified service.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkServiceAddProtocolType(_ service: SCNetworkService, _ protocolType: CFString) -> Bool
```

```c
Boolean SCNetworkServiceAddProtocolType(SCNetworkServiceRef service, CFStringRef protocolType);
```

#### Return Value

`TRUE` if the protocol was added to the service; `FALSE` if the protocol was already present or an error occurred.

#### Discussion

The protocol configuration is set to default values that are appropriate for the interface associated with the service.

## Parameters

- `service`: The network service.
- `protocolType`: The type of network protocol to add to the service.

## See Also

### Configuring Network Services
- [func SCNetworkServiceCopy(SCPreferences, CFString) -> SCNetworkService?](./scnetworkservicecopy%28_,_%29.md)
  Returns the network service with the specified identifier.
- [func SCNetworkServiceCopyAll(SCPreferences) -> CFArray?](./scnetworkservicecopyall%28_%29.md)
  Returns all available network services for the specified preferences.
- [func SCNetworkServiceCopyProtocol(SCNetworkService, CFString) -> SCNetworkProtocol?](./scnetworkservicecopyprotocol%28_,_%29.md)
  Returns the network protocol of the specified type for the specified service.
- [func SCNetworkServiceCopyProtocols(SCNetworkService) -> CFArray?](./scnetworkservicecopyprotocols%28_%29.md)
  Returns all network protocols associated with the specified service.
- [func SCNetworkServiceCreate(SCPreferences, SCNetworkInterface) -> SCNetworkService?](./scnetworkservicecreate%28_,_%29.md)
  Creates a new network service for the specified interface in the configuration.
- [func SCNetworkServiceEstablishDefaultConfiguration(SCNetworkService) -> Bool](./scnetworkserviceestablishdefaultconfiguration%28_%29.md)
  Establishes the default configuration for the specified network service.
- [func SCNetworkServiceGetEnabled(SCNetworkService) -> Bool](./scnetworkservicegetenabled%28_%29.md)
  Returns a Boolean value indicating whether the specified service is enabled.
- [func SCNetworkServiceGetInterface(SCNetworkService) -> SCNetworkInterface?](./scnetworkservicegetinterface%28_%29.md)
  Returns the network interface associated with the specified service.
- [func SCNetworkServiceGetName(SCNetworkService) -> CFString?](./scnetworkservicegetname%28_%29.md)
  Returns the user-specified name associated with the specified service.
- [func SCNetworkServiceGetServiceID(SCNetworkService) -> CFString?](./scnetworkservicegetserviceid%28_%29.md)
  Returns the identifier for the specified service.
- [func SCNetworkServiceGetTypeID() -> CFTypeID](./scnetworkservicegettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkService` instances.
- [func SCNetworkServiceRemove(SCNetworkService) -> Bool](./scnetworkserviceremove%28_%29.md)
  Removes the specified network service from the configuration.
- [func SCNetworkServiceRemoveProtocolType(SCNetworkService, CFString) -> Bool](./scnetworkserviceremoveprotocoltype%28_,_%29.md)
  Removes the network protocol of the specified type from the specified service.
- [func SCNetworkServiceSetEnabled(SCNetworkService, Bool) -> Bool](./scnetworkservicesetenabled%28_,_%29.md)
  Enables or disables the specified service.
- [func SCNetworkServiceSetName(SCNetworkService, CFString?) -> Bool](./scnetworkservicesetname%28_,_%29.md)
  Stores the user-specified name for the specified service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkserviceaddprotocoltype(_:_:))*