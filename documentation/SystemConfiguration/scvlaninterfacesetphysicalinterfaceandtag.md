# SCVLANInterfaceSetPhysicalInterfaceAndTag(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Updates the specified virtual LAN (VLAN) interface with the specified information.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SCVLANInterfaceSetPhysicalInterfaceAndTag(_ vlan: SCVLANInterface, _ physical: SCNetworkInterface, _ tag: CFNumber) -> Bool
```

#### Return Value

`TRUE` if the configuration was stored; `FALSE` if an error occurred.

## Parameters

- `vlan`: The VLAN interface to update.
- `physical`: The physical interface to associate with the VLAN interface.
- `tag`: The tag to associate with the VLAN interface. This value must be between 1 and 4094.

## See Also

- [func SCVLANInterfaceCopyAll(SCPreferences) -> CFArray](scvlaninterfacecopyall(_:).md)
  Returns all virtual LAN (VLAN) interfaces on the system.
- [func SCVLANInterfaceCopyAvailablePhysicalInterfaces() -> CFArray](scvlaninterfacecopyavailablephysicalinterfaces().md)
  Returns the network capable devices on the system that can be associated with a virtual LAN (VLAN) interface.
- [func SCVLANInterfaceCreate(SCPreferences, SCNetworkInterface, CFNumber) -> SCVLANInterface?](scvlaninterfacecreate(_:_:_:).md)
  Creates a new virtual LAN (VLAN) interface.
- [func SCVLANInterfaceGetOptions(SCVLANInterface) -> CFDictionary?](scvlaninterfacegetoptions(_:).md)
  Returns the configuration settings associated with the virtual LAN (VLAN) interface.
- [func SCVLANInterfaceGetPhysicalInterface(SCVLANInterface) -> SCNetworkInterface?](scvlaninterfacegetphysicalinterface(_:).md)
  Returns the physical interface for the specified virtual LAN (VLAN) interface.
- [func SCVLANInterfaceGetTag(SCVLANInterface) -> CFNumber?](scvlaninterfacegettag(_:).md)
  Returns the tag for the specified virtual LAN (VLAN) interface.
- [func SCVLANInterfaceRemove(SCVLANInterface) -> Bool](scvlaninterfaceremove(_:).md)
  Removes the virtual LAN (VLAN) interface from the configuration.
- [func SCVLANInterfaceSetLocalizedDisplayName(SCVLANInterface, CFString) -> Bool](scvlaninterfacesetlocalizeddisplayname(_:_:).md)
  Sets the localized display name for the specified virtual LAN (VLAN) interface.
- [func SCVLANInterfaceSetOptions(SCVLANInterface, CFDictionary) -> Bool](scvlaninterfacesetoptions(_:_:).md)
  Sets the specified configuration settings for the specified virtual LAN (VLAN) interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scvlaninterfacesetphysicalinterfaceandtag(_:_:_:))*