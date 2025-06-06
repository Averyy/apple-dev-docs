# SCBondStatusGetInterfaceStatus(_:_:)

**Framework**: System Configuration  
**Kind**: func

Returns the status of the specified member interface of an Ethernet bond or the status of the bond as a whole.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SCBondStatusGetInterfaceStatus(_ bondStatus: SCBondStatus, _ interface: SCNetworkInterface?) -> CFDictionary?
```

#### Return Value

The interface status.

## Parameters

- `bondStatus`: The Ethernet bond status.
- `interface`: The member interface whose status is needed. Pass   to get the status of the Ethernet bond.

## See Also

- [func SCBondInterfaceCopyAll(SCPreferences) -> CFArray](scbondinterfacecopyall(_:).md)
  Returns all Ethernet bond interfaces on the system.
- [func SCBondInterfaceCopyAvailableMemberInterfaces(SCPreferences) -> CFArray](scbondinterfacecopyavailablememberinterfaces(_:).md)
  Returns all network capable devices on the system that can be added to an Ethernet bond interface.
- [func SCBondInterfaceCopyStatus(SCBondInterface) -> SCBondStatus?](scbondinterfacecopystatus(_:).md)
  Returns the status of the specified Ethernet bond interface.
- [func SCBondInterfaceCreate(SCPreferences) -> SCBondInterface?](scbondinterfacecreate(_:).md)
  Creates a new Ethernet bond interface.
- [func SCBondInterfaceGetMemberInterfaces(SCBondInterface) -> CFArray?](scbondinterfacegetmemberinterfaces(_:).md)
  Returns the member interfaces for the specified Ethernet bond interface.
- [func SCBondInterfaceGetOptions(SCBondInterface) -> CFDictionary?](scbondinterfacegetoptions(_:).md)
  Returns the configuration settings associated with the specified Ethernet bond interface.
- [func SCBondInterfaceRemove(SCBondInterface) -> Bool](scbondinterfaceremove(_:).md)
  Removes the Ethernet bond interface from the configuration.
- [func SCBondInterfaceSetLocalizedDisplayName(SCBondInterface, CFString) -> Bool](scbondinterfacesetlocalizeddisplayname(_:_:).md)
  Sets the localized display name for the specified Ethernet bond interface.
- [func SCBondInterfaceSetMemberInterfaces(SCBondInterface, CFArray) -> Bool](scbondinterfacesetmemberinterfaces(_:_:).md)
  Sets the member interfaces for the specified Ethernet bond interface.
- [func SCBondInterfaceSetOptions(SCBondInterface, CFDictionary) -> Bool](scbondinterfacesetoptions(_:_:).md)
  Sets the configuration settings for the specified Ethernet bond interface.
- [func SCBondStatusGetMemberInterfaces(SCBondStatus) -> CFArray?](scbondstatusgetmemberinterfaces(_:).md)
  Returns the member interfaces that are represented with the Ethernet bond interface.
- [func SCBondStatusGetTypeID() -> CFTypeID](scbondstatusgettypeid().md)
  Returns the type identifier of all `SCBondStatusRef` instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scbondstatusgetinterfacestatus(_:_:))*