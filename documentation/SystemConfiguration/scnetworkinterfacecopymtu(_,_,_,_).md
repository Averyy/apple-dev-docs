# SCNetworkInterfaceCopyMTU(_:_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the current MTU setting and the range of allowable values for the specified network interface.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SCNetworkInterfaceCopyMTU(_ interface: SCNetworkInterface, _ mtu_cur: UnsafeMutablePointer<Int32>?, _ mtu_min: UnsafeMutablePointer<Int32>?, _ mtu_max: UnsafeMutablePointer<Int32>?) -> Bool
```

```c
Boolean SCNetworkInterfaceCopyMTU(SCNetworkInterfaceRef interface, int *mtu_cur, int *mtu_min, int *mtu_max);
```

#### Return Value

`TRUE` if the requested information has been returned.

## Parameters

- `interface`: The network interface.
- `mtu_cur`: On output, the current MTU setting for the interface.
- `mtu_min`: On output, the minimum MTU setting for the interface. If negative, the minimum setting could not be determined.
- `mtu_max`: On output, the maximum MTU setting for the interface. If negative, the maximum setting could not be determined.

## See Also

### Configuring Network Interfaces
- [func SCNetworkInterfaceCopyAll() -> CFArray](./scnetworkinterfacecopyall%28%29.md)
  Returns all network-capable interfaces on the system.
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
- [func SCNetworkInterfaceGetInterfaceType(SCNetworkInterface) -> CFString?](./scnetworkinterfacegetinterfacetype%28_%29.md)
  Returns the network interface type of the specified interface.
- [func SCNetworkInterfaceGetLocalizedDisplayName(SCNetworkInterface) -> CFString?](./scnetworkinterfacegetlocalizeddisplayname%28_%29.md)
  Returns the localized display name, such as “Ethernet” or “FireWire”, for the specified interface.
- [func SCNetworkInterfaceGetSupportedInterfaceTypes(SCNetworkInterface) -> CFArray?](./scnetworkinterfacegetsupportedinterfacetypes%28_%29.md)
  Identifies all of the network interface types, such as PPP, that can be layered on top of the specified interface.
- [func SCNetworkInterfaceGetSupportedProtocolTypes(SCNetworkInterface) -> CFArray?](./scnetworkinterfacegetsupportedprotocoltypes%28_%29.md)
  Identifies all of the network protocol types, such as IPv4 and IPv6, that can be layered on top of the specified interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkinterfacecopymtu(_:_:_:_:))*