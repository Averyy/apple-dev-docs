# SCNetworkInterfaceGetInterfaceType(_:)

**Framework**: System Configuration  
**Kind**: func

Returns the network interface type of the specified interface.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkInterfaceGetInterfaceType(_ interface: SCNetworkInterface) -> CFString?
```

#### Return Value

The interface type.

## Parameters

- `interface`: The network interface.

## See Also

- [func SCNetworkInterfaceCopyAll() -> CFArray](scnetworkinterfacecopyall().md)
  Returns all network-capable interfaces on the system.
- [func SCNetworkInterfaceCopyMTU(SCNetworkInterface, UnsafeMutablePointer<Int32>?, UnsafeMutablePointer<Int32>?, UnsafeMutablePointer<Int32>?) -> Bool](scnetworkinterfacecopymtu(_:_:_:_:).md)
  Returns the current MTU setting and the range of allowable values for the specified network interface.
- [func SCNetworkInterfaceCopyMediaOptions(SCNetworkInterface, UnsafeMutablePointer<Unmanaged<CFDictionary>?>?, UnsafeMutablePointer<Unmanaged<CFDictionary>?>?, UnsafeMutablePointer<Unmanaged<CFArray>?>?, Bool) -> Bool](scnetworkinterfacecopymediaoptions(_:_:_:_:_:).md)
  Returns information media options for the specified network interface.
- [func SCNetworkInterfaceCopyMediaSubTypeOptions(CFArray, CFString) -> CFArray?](scnetworkinterfacecopymediasubtypeoptions(_:_:).md)
  Returns a list of available media options for the specified interface configuration options and subtype.
- [func SCNetworkInterfaceCopyMediaSubTypes(CFArray) -> CFArray?](scnetworkinterfacecopymediasubtypes(_:).md)
  Returns a list of available media subtypes for the specified interface configuration options.
- [func SCNetworkInterfaceCreateWithInterface(SCNetworkInterface, CFString) -> SCNetworkInterface?](scnetworkinterfacecreatewithinterface(_:_:).md)
  Creates a new network interface layered on top of the specified interface.
- [func SCNetworkInterfaceForceConfigurationRefresh(SCNetworkInterface) -> Bool](scnetworkinterfaceforceconfigurationrefresh(_:).md)
  Sends a notification to interested network configuration agents to immediately retry their configuration.
- [func SCNetworkInterfaceGetBSDName(SCNetworkInterface) -> CFString?](scnetworkinterfacegetbsdname(_:).md)
  Returns the BSD interface or device name for the specified interface.
- [func SCNetworkInterfaceGetConfiguration(SCNetworkInterface) -> CFDictionary?](scnetworkinterfacegetconfiguration(_:).md)
  Returns the configuration settings associated with the specified interface.
- [func SCNetworkInterfaceGetExtendedConfiguration(SCNetworkInterface, CFString) -> CFDictionary?](scnetworkinterfacegetextendedconfiguration(_:_:).md)
  Returns the extended configuration settings associated with the specified interface.
- [func SCNetworkInterfaceGetHardwareAddressString(SCNetworkInterface) -> CFString?](scnetworkinterfacegethardwareaddressstring(_:).md)
  Returns a displayable link layer address for the specified interface.
- [func SCNetworkInterfaceGetInterface(SCNetworkInterface) -> SCNetworkInterface?](scnetworkinterfacegetinterface(_:).md)
  Returns the underlying interface, for layered network interfaces.
- [func SCNetworkInterfaceGetLocalizedDisplayName(SCNetworkInterface) -> CFString?](scnetworkinterfacegetlocalizeddisplayname(_:).md)
  Returns the localized display name, such as “Ethernet” or “FireWire”, for the specified interface.
- [func SCNetworkInterfaceGetSupportedInterfaceTypes(SCNetworkInterface) -> CFArray?](scnetworkinterfacegetsupportedinterfacetypes(_:).md)
  Identifies all of the network interface types, such as PPP, that can be layered on top of the specified interface.
- [func SCNetworkInterfaceGetSupportedProtocolTypes(SCNetworkInterface) -> CFArray?](scnetworkinterfacegetsupportedprotocoltypes(_:).md)
  Identifies all of the network protocol types, such as IPv4 and IPv6, that can be layered on top of the specified interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkinterfacegetinterfacetype(_:))*