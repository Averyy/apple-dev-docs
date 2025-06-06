# SCBondInterfaceCreate(_:)

**Framework**: System Configuration  
**Kind**: func

Creates a new Ethernet bond interface.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SCBondInterfaceCreate(_ prefs: SCPreferences) -> SCBondInterface?
```

#### Return Value

The new Ethernet bond interface, represented by an [`SCBondInterface`](scbondinterface.md) object. You must release the returned value.

## Parameters

- `prefs`: The preferences session.

## See Also

- [func SCBondInterfaceCopyAll(SCPreferences) -> CFArray](scbondinterfacecopyall(_:).md)
  Returns all Ethernet bond interfaces on the system.
- [func SCBondInterfaceCopyAvailableMemberInterfaces(SCPreferences) -> CFArray](scbondinterfacecopyavailablememberinterfaces(_:).md)
  Returns all network capable devices on the system that can be added to an Ethernet bond interface.
- [func SCBondInterfaceCopyStatus(SCBondInterface) -> SCBondStatus?](scbondinterfacecopystatus(_:).md)
  Returns the status of the specified Ethernet bond interface.
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
- [func SCBondStatusGetInterfaceStatus(SCBondStatus, SCNetworkInterface?) -> CFDictionary?](scbondstatusgetinterfacestatus(_:_:).md)
  Returns the status of the specified member interface of an Ethernet bond or the status of the bond as a whole.
- [func SCBondStatusGetMemberInterfaces(SCBondStatus) -> CFArray?](scbondstatusgetmemberinterfaces(_:).md)
  Returns the member interfaces that are represented with the Ethernet bond interface.
- [func SCBondStatusGetTypeID() -> CFTypeID](scbondstatusgettypeid().md)
  Returns the type identifier of all `SCBondStatusRef` instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scbondinterfacecreate(_:))*