# SCBondInterfaceSetMemberInterfaces(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Sets the member interfaces for the specified Ethernet bond interface.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SCBondInterfaceSetMemberInterfaces(_ bond: SCBondInterface, _ members: CFArray) -> Bool
```

```c
Boolean SCBondInterfaceSetMemberInterfaces(SCBondInterfaceRef bond, CFArrayRef members);
```

## Return Value

`TRUE` if the configuration was stored; `FALSE` if an error occurred.

## Parameters

- `bond`: The Ethernet bond interface
- `members`: The desired member interfaces.

## See Also

### Configuring Ethernet Bond Interfaces
- [func SCBondInterfaceCopyAll(SCPreferences) -> CFArray](./scbondinterfacecopyall%28_%29.md)
  Returns all Ethernet bond interfaces on the system.
- [func SCBondInterfaceCopyAvailableMemberInterfaces(SCPreferences) -> CFArray](./scbondinterfacecopyavailablememberinterfaces%28_%29.md)
  Returns all network capable devices on the system that can be added to an Ethernet bond interface.
- [func SCBondInterfaceCopyStatus(SCBondInterface) -> SCBondStatus?](./scbondinterfacecopystatus%28_%29.md)
  Returns the status of the specified Ethernet bond interface.
- [func SCBondInterfaceCreate(SCPreferences) -> SCBondInterface?](./scbondinterfacecreate%28_%29.md)
  Creates a new Ethernet bond interface.
- [func SCBondInterfaceGetMemberInterfaces(SCBondInterface) -> CFArray?](./scbondinterfacegetmemberinterfaces%28_%29.md)
  Returns the member interfaces for the specified Ethernet bond interface.
- [func SCBondInterfaceGetOptions(SCBondInterface) -> CFDictionary?](./scbondinterfacegetoptions%28_%29.md)
  Returns the configuration settings associated with the specified Ethernet bond interface.
- [func SCBondInterfaceRemove(SCBondInterface) -> Bool](./scbondinterfaceremove%28_%29.md)
  Removes the Ethernet bond interface from the configuration.
- [func SCBondInterfaceSetLocalizedDisplayName(SCBondInterface, CFString) -> Bool](./scbondinterfacesetlocalizeddisplayname%28_,_%29.md)
  Sets the localized display name for the specified Ethernet bond interface.
- [func SCBondInterfaceSetOptions(SCBondInterface, CFDictionary) -> Bool](./scbondinterfacesetoptions%28_,_%29.md)
  Sets the configuration settings for the specified Ethernet bond interface.
- [func SCBondStatusGetInterfaceStatus(SCBondStatus, SCNetworkInterface?) -> CFDictionary?](./scbondstatusgetinterfacestatus%28_,_%29.md)
  Returns the status of the specified member interface of an Ethernet bond or the status of the bond as a whole.
- [func SCBondStatusGetMemberInterfaces(SCBondStatus) -> CFArray?](./scbondstatusgetmemberinterfaces%28_%29.md)
  Returns the member interfaces that are represented with the Ethernet bond interface.
- [func SCBondStatusGetTypeID() -> CFTypeID](./scbondstatusgettypeid%28%29.md)
  Returns the type identifier of all `SCBondStatusRef` instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scbondinterfacesetmemberinterfaces(_:_:))*