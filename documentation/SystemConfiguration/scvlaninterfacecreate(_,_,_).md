# SCVLANInterfaceCreate(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Creates a new virtual LAN (VLAN) interface.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SCVLANInterfaceCreate(_ prefs: SCPreferences, _ physical: SCNetworkInterface, _ tag: CFNumber) -> SCVLANInterface?
```

```c
SCVLANInterfaceRefSCVLANInterfaceCreate(SCPreferencesRef prefs, SCNetworkInterfaceRef physical, CFNumberRef tag);
```

#### Return Value

The new VLAN interface. You must release the returned value.

## Parameters

- `prefs`: The preferences session.
- `physical`: The physical interface to associate with the VLAN.
- `tag`: The tag to associate with the VLAN. This value must be between 1 and 4094.

## See Also

### Configuring VLAN Interfaces
- [func SCVLANInterfaceCopyAll(SCPreferences) -> CFArray](./scvlaninterfacecopyall%28_%29.md)
  Returns all virtual LAN (VLAN) interfaces on the system.
- [func SCVLANInterfaceCopyAvailablePhysicalInterfaces() -> CFArray](./scvlaninterfacecopyavailablephysicalinterfaces%28%29.md)
  Returns the network capable devices on the system that can be associated with a virtual LAN (VLAN) interface.
- [func SCVLANInterfaceGetOptions(SCVLANInterface) -> CFDictionary?](./scvlaninterfacegetoptions%28_%29.md)
  Returns the configuration settings associated with the virtual LAN (VLAN) interface.
- [func SCVLANInterfaceGetPhysicalInterface(SCVLANInterface) -> SCNetworkInterface?](./scvlaninterfacegetphysicalinterface%28_%29.md)
  Returns the physical interface for the specified virtual LAN (VLAN) interface.
- [func SCVLANInterfaceGetTag(SCVLANInterface) -> CFNumber?](./scvlaninterfacegettag%28_%29.md)
  Returns the tag for the specified virtual LAN (VLAN) interface.
- [func SCVLANInterfaceRemove(SCVLANInterface) -> Bool](./scvlaninterfaceremove%28_%29.md)
  Removes the virtual LAN (VLAN) interface from the configuration.
- [func SCVLANInterfaceSetLocalizedDisplayName(SCVLANInterface, CFString) -> Bool](./scvlaninterfacesetlocalizeddisplayname%28_,_%29.md)
  Sets the localized display name for the specified virtual LAN (VLAN) interface.
- [func SCVLANInterfaceSetOptions(SCVLANInterface, CFDictionary) -> Bool](./scvlaninterfacesetoptions%28_,_%29.md)
  Sets the specified configuration settings for the specified virtual LAN (VLAN) interface.
- [func SCVLANInterfaceSetPhysicalInterfaceAndTag(SCVLANInterface, SCNetworkInterface, CFNumber) -> Bool](./scvlaninterfacesetphysicalinterfaceandtag%28_,_,_%29.md)
  Updates the specified virtual LAN (VLAN) interface with the specified information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scvlaninterfacecreate(_:_:_:))*