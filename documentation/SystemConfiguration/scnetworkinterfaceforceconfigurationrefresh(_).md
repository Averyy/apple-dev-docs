# SCNetworkInterfaceForceConfigurationRefresh(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Sends a notification to interested network configuration agents to immediately retry their configuration.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SCNetworkInterfaceForceConfigurationRefresh(_ interface: SCNetworkInterface) -> Bool
```

```c
Boolean SCNetworkInterfaceForceConfigurationRefresh(SCNetworkInterfaceRef interface);
```

## Return Value

`TRUE` if the notification was sent; otherwise, `FALSE`.

## Discussion

Calling this function causes the DHCP client to contact the DHCP server immediately rather than waiting until its timeout has expired. The caller uses this function to inform the system that the network infrastructure or configuration has changed.

Note that this function requires root privilege; alternatively, you can pass in an interface that is derived from a sequence of calls to:

- [`SCPreferencesCreateWithAuthorization(_:_:_:_:)`](./scpreferencescreatewithauthorization%28_,_,_,_%29.md)
- The appropriate `SCNetworkSetCopy...` function, such as [`SCNetworkSetCopyServices(_:)`](./scnetworksetcopyservices%28_%29.md)
- [`SCNetworkServiceGetInterface(_:)`](./scnetworkservicegetinterface%28_%29.md)

## Parameters

- `interface`: The desired network interface.

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

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkinterfaceforceconfigurationrefresh(_:))*