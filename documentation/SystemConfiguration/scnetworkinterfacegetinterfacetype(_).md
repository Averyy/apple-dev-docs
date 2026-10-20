# SCNetworkInterfaceGetInterfaceType(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the network interface type of the specified interface.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkInterfaceGetInterfaceType(_ interface: SCNetworkInterface) -> CFString?
```

```c
CFStringRefSCNetworkInterfaceGetInterfaceType(SCNetworkInterfaceRef interface);
```

#### Return Value

The interface type.

## Parameters

- `interface`: The network interface.

## See Also

### Configuring Network Interfaces
- [func SCNetworkInterfaceCopyAll() -> CFArray](./scnetworkinterfacecopyall%28%29.md)
  Returns all network-capable interfaces on the system.
- [func SCNetworkInterfaceCopyMTU(SCNetworkInterface, UnsafeMutablePointer<Int32>?, UnsafeMutablePointer<Int32>?, UnsafeMutablePointer<Int32>?) -> Bool](./scnetworkinterfacecopymtu%28_,_,_,_%29.md)
  Returns the current MTU setting and the range of allowable values for the specified network interface.
- [func SCNetworkInterfaceCopyMediaOptions(SCNetworkInterface, UnsafeMutablePointer<Unmanaged<CFDictionary>?>?, UnsafeMutablePointer<Unmanaged<CFDictionary>?>?, UnsafeMutablePointer<Unmanaged<CFArray>?>?, Bool) -> Bool](./scnetworkinterfacecopymediaoptions%28_,_,_,_,_%29.md)
  Returns information media options for the specified network interface.
- [func SCNetworkInterfaceCopyMediaSubTypeOptions(CFArray, CFString) -> CFArray?](./scnetworkinterfacecopymediasubtypeoptions%28_,_%29.md)
  Returns a list of available media options for the specified interface configuration options and subtype.
- [func SCNetworkInterfaceCopyMediaSubTypes(CFArray) -> CFArray?](./scnetworkinterfacecopymediasubtypes%28_%29.md)
  Returns a list of available media subtypes for the specified interface configuration options.
- [func SCNetworkInterfaceCreateWithInterface(SCNetworkInterface, CFString) -> SCNetworkInterface?](./scnetworkinterfacecreatewithinterface%28_,_%29.md)
  Creates a new network interface layered on top of the specified interface.
- [func SCNetworkInterfaceForceConfigurationRefresh(SCNetworkInterface) -> Bool](./scnetworkinterfaceforceconfigurationrefresh%28_%29.md)
  Sends a notification to interested network configuration agents to immediately retry their configuration.
- [func SCNetworkInterfaceGetBSDName(SCNetworkInterface) -> CFString?](./scnetworkinterfacegetbsdname%28_%29.md)
  Returns the BSD interface or device name for the specified interface.
- [func SCNetworkInterfaceGetConfiguration(SCNetworkInterface) -> CFDictionary?](./scnetworkinterfacegetconfiguration%28_%29.md)
  Returns the configuration settings associated with the specified interface.
- [func SCNetworkInterfaceGetExtendedConfiguration(SCNetworkInterface, CFString) -> CFDictionary?](./scnetworkinterfacegetextendedconfiguration%28_,_%29.md)
  Returns the extended configuration settings associated with the specified interface.
- [func SCNetworkInterfaceGetHardwareAddressString(SCNetworkInterface) -> CFString?](./scnetworkinterfacegethardwareaddressstring%28_%29.md)
  Returns a displayable link layer address for the specified interface.
- [func SCNetworkInterfaceGetInterface(SCNetworkInterface) -> SCNetworkInterface?](./scnetworkinterfacegetinterface%28_%29.md)
  Returns the underlying interface, for layered network interfaces.
- [func SCNetworkInterfaceGetLocalizedDisplayName(SCNetworkInterface) -> CFString?](./scnetworkinterfacegetlocalizeddisplayname%28_%29.md)
  Returns the localized display name, such as “Ethernet” or “FireWire”, for the specified interface.
- [func SCNetworkInterfaceGetSupportedInterfaceTypes(SCNetworkInterface) -> CFArray?](./scnetworkinterfacegetsupportedinterfacetypes%28_%29.md)
  Identifies all of the network interface types, such as PPP, that can be layered on top of the specified interface.
- [func SCNetworkInterfaceGetSupportedProtocolTypes(SCNetworkInterface) -> CFArray?](./scnetworkinterfacegetsupportedprotocoltypes%28_%29.md)
  Identifies all of the network protocol types, such as IPv4 and IPv6, that can be layered on top of the specified interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkinterfacegetinterfacetype(_:))*