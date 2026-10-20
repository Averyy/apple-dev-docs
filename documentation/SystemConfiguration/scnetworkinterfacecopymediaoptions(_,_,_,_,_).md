# SCNetworkInterfaceCopyMediaOptions(_:_:_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns information media options for the specified network interface.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SCNetworkInterfaceCopyMediaOptions(_ interface: SCNetworkInterface, _ current: UnsafeMutablePointer<Unmanaged<CFDictionary>?>?, _ active: UnsafeMutablePointer<Unmanaged<CFDictionary>?>?, _ available: UnsafeMutablePointer<Unmanaged<CFArray>?>?, _ filter: Bool) -> Bool
```

```c
Boolean SCNetworkInterfaceCopyMediaOptions(SCNetworkInterfaceRef interface, CFDictionaryRef*current, CFDictionaryRef*active, CFArrayRef*available, Boolean filter);
```

#### Return Value

`TRUE` if requested information has been returned.

## Parameters

- `interface`: The network interface.
- `current`: On output, a dictionary representing the currently requested media options (subtype, options). If `NULL`, the current options are not returned.
- `active`: On output, a dictionary representing the active media options (subtype, options). If `NULL`, the active options are not returned.
- `available`: On output, an array representing the possible media options (subtype, options). If `NULL`, the current options are not returned.
- `filter`: A Boolean value indicating whether the available options should be filtered to exclude those options which would not normally be requested by a user/admin (for example, `hw-loopback`).

## See Also

### Configuring Network Interfaces
- [func SCNetworkInterfaceCopyAll() -> CFArray](./scnetworkinterfacecopyall%28%29.md)
  Returns all network-capable interfaces on the system.
- [func SCNetworkInterfaceCopyMTU(SCNetworkInterface, UnsafeMutablePointer<Int32>?, UnsafeMutablePointer<Int32>?, UnsafeMutablePointer<Int32>?) -> Bool](./scnetworkinterfacecopymtu%28_,_,_,_%29.md)
  Returns the current MTU setting and the range of allowable values for the specified network interface.
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

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkinterfacecopymediaoptions(_:_:_:_:_:))*