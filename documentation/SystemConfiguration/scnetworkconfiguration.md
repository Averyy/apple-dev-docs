# SCNetworkConfiguration

**Framework**: System Configuration

#### Overview

The `SCNetworkConfiguration` programming interface provides access to the stored network configuration. The functions include providing access to the network-capable devices on the system, the network sets, network services, and network protocols. Note that these functions follow Core Foundation function-name conventions. A function that has “Create” or “Copy” in its name returns a reference you must release with the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function.

Note that when using the functions in this programming interface, you must call the [`SCPreferencesCommitChanges(_:)`](scpreferencescommitchanges(_:).md) function to ensure that your changes are committed to permanent storage.

## Topics

### Configuring Ethernet Bond Interfaces
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
- [func SCBondStatusGetInterfaceStatus(SCBondStatus, SCNetworkInterface?) -> CFDictionary?](scbondstatusgetinterfacestatus(_:_:).md)
  Returns the status of the specified member interface of an Ethernet bond or the status of the bond as a whole.
- [func SCBondStatusGetMemberInterfaces(SCBondStatus) -> CFArray?](scbondstatusgetmemberinterfaces(_:).md)
  Returns the member interfaces that are represented with the Ethernet bond interface.
- [func SCBondStatusGetTypeID() -> CFTypeID](scbondstatusgettypeid().md)
  Returns the type identifier of all `SCBondStatusRef` instances.
### Configuring Network Interfaces
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
- [func SCNetworkInterfaceGetInterfaceType(SCNetworkInterface) -> CFString?](scnetworkinterfacegetinterfacetype(_:).md)
  Returns the network interface type of the specified interface.
- [func SCNetworkInterfaceGetLocalizedDisplayName(SCNetworkInterface) -> CFString?](scnetworkinterfacegetlocalizeddisplayname(_:).md)
  Returns the localized display name, such as “Ethernet” or “FireWire”, for the specified interface.
- [func SCNetworkInterfaceGetSupportedInterfaceTypes(SCNetworkInterface) -> CFArray?](scnetworkinterfacegetsupportedinterfacetypes(_:).md)
  Identifies all of the network interface types, such as PPP, that can be layered on top of the specified interface.
- [func SCNetworkInterfaceGetSupportedProtocolTypes(SCNetworkInterface) -> CFArray?](scnetworkinterfacegetsupportedprotocoltypes(_:).md)
  Identifies all of the network protocol types, such as IPv4 and IPv6, that can be layered on top of the specified interface.
- [func SCNetworkInterfaceGetTypeID() -> CFTypeID](scnetworkinterfacegettypeid().md)
  Returns the type identifier of all `SCNetworkInterface` instances.
- [func SCNetworkInterfaceSetConfiguration(SCNetworkInterface, CFDictionary?) -> Bool](scnetworkinterfacesetconfiguration(_:_:).md)
  Stores the configuration settings for the specified interface.
- [func SCNetworkInterfaceSetExtendedConfiguration(SCNetworkInterface, CFString, CFDictionary?) -> Bool](scnetworkinterfacesetextendedconfiguration(_:_:_:).md)
  Stores the extended configuration settings for the specified interface.
- [func SCNetworkInterfaceSetMTU(SCNetworkInterface, Int32) -> Bool](scnetworkinterfacesetmtu(_:_:).md)
  Sets the requested MTU setting for the specified network interface.
- [func SCNetworkInterfaceSetMediaOptions(SCNetworkInterface, CFString?, CFArray?) -> Bool](scnetworkinterfacesetmediaoptions(_:_:_:).md)
  Sets the requested media subtype and options for the specified network interface.
### Configuring Network Protocols
- [func SCNetworkProtocolGetConfiguration(SCNetworkProtocol) -> CFDictionary?](scnetworkprotocolgetconfiguration(_:).md)
  Returns the configuration settings associated with the specified protocol.
- [func SCNetworkProtocolGetEnabled(SCNetworkProtocol) -> Bool](scnetworkprotocolgetenabled(_:).md)
  Returns a Boolean value indicating whether the specified protocol is enabled.
- [func SCNetworkProtocolGetProtocolType(SCNetworkProtocol) -> CFString?](scnetworkprotocolgetprotocoltype(_:).md)
  Returns the type of the specified network protocol.
- [func SCNetworkProtocolGetTypeID() -> CFTypeID](scnetworkprotocolgettypeid().md)
  Returns the type identifier of all `SCNetworkProtocol` instances.
- [func SCNetworkProtocolSetConfiguration(SCNetworkProtocol, CFDictionary?) -> Bool](scnetworkprotocolsetconfiguration(_:_:).md)
  Stores the configuration settings for the specified network protocol.
- [func SCNetworkProtocolSetEnabled(SCNetworkProtocol, Bool) -> Bool](scnetworkprotocolsetenabled(_:_:).md)
  Enables or disables the specified protocol.
### Configuring Network Services
- [func SCNetworkServiceAddProtocolType(SCNetworkService, CFString) -> Bool](scnetworkserviceaddprotocoltype(_:_:).md)
  Adds the network protocol of the specified type to the specified service.
- [func SCNetworkServiceCopy(SCPreferences, CFString) -> SCNetworkService?](scnetworkservicecopy(_:_:).md)
  Returns the network service with the specified identifier.
- [func SCNetworkServiceCopyAll(SCPreferences) -> CFArray?](scnetworkservicecopyall(_:).md)
  Returns all available network services for the specified preferences.
- [func SCNetworkServiceCopyProtocol(SCNetworkService, CFString) -> SCNetworkProtocol?](scnetworkservicecopyprotocol(_:_:).md)
  Returns the network protocol of the specified type for the specified service.
- [func SCNetworkServiceCopyProtocols(SCNetworkService) -> CFArray?](scnetworkservicecopyprotocols(_:).md)
  Returns all network protocols associated with the specified service.
- [func SCNetworkServiceCreate(SCPreferences, SCNetworkInterface) -> SCNetworkService?](scnetworkservicecreate(_:_:).md)
  Creates a new network service for the specified interface in the configuration.
- [func SCNetworkServiceEstablishDefaultConfiguration(SCNetworkService) -> Bool](scnetworkserviceestablishdefaultconfiguration(_:).md)
  Establishes the default configuration for the specified network service.
- [func SCNetworkServiceGetEnabled(SCNetworkService) -> Bool](scnetworkservicegetenabled(_:).md)
  Returns a Boolean value indicating whether the specified service is enabled.
- [func SCNetworkServiceGetInterface(SCNetworkService) -> SCNetworkInterface?](scnetworkservicegetinterface(_:).md)
  Returns the network interface associated with the specified service.
- [func SCNetworkServiceGetName(SCNetworkService) -> CFString?](scnetworkservicegetname(_:).md)
  Returns the user-specified name associated with the specified service.
- [func SCNetworkServiceGetServiceID(SCNetworkService) -> CFString?](scnetworkservicegetserviceid(_:).md)
  Returns the identifier for the specified service.
- [func SCNetworkServiceGetTypeID() -> CFTypeID](scnetworkservicegettypeid().md)
  Returns the type identifier of all `SCNetworkService` instances.
- [func SCNetworkServiceRemove(SCNetworkService) -> Bool](scnetworkserviceremove(_:).md)
  Removes the specified network service from the configuration.
- [func SCNetworkServiceRemoveProtocolType(SCNetworkService, CFString) -> Bool](scnetworkserviceremoveprotocoltype(_:_:).md)
  Removes the network protocol of the specified type from the specified service.
- [func SCNetworkServiceSetEnabled(SCNetworkService, Bool) -> Bool](scnetworkservicesetenabled(_:_:).md)
  Enables or disables the specified service.
- [func SCNetworkServiceSetName(SCNetworkService, CFString?) -> Bool](scnetworkservicesetname(_:_:).md)
  Stores the user-specified name for the specified service.
### Configuring Network Sets
- [func SCNetworkSetAddService(SCNetworkSet, SCNetworkService) -> Bool](scnetworksetaddservice(_:_:).md)
  Adds the specified network service to the specified set.
- [func SCNetworkSetContainsInterface(SCNetworkSet, SCNetworkInterface) -> Bool](scnetworksetcontainsinterface(_:_:).md)
  Returns a Boolean value indicating whether the specified interface is represented by at least one network service in the specified set.
- [func SCNetworkSetCopy(SCPreferences, CFString) -> SCNetworkSet?](scnetworksetcopy(_:_:).md)
  Returns the set with the specified identifier.
- [func SCNetworkSetCopyAll(SCPreferences) -> CFArray?](scnetworksetcopyall(_:).md)
  Returns all available sets for the specified preferences session.
- [func SCNetworkSetCopyCurrent(SCPreferences) -> SCNetworkSet?](scnetworksetcopycurrent(_:).md)
  Returns the current set.
- [func SCNetworkSetCopyServices(SCNetworkSet) -> CFArray?](scnetworksetcopyservices(_:).md)
  Returns all network services associated with the specified set.
- [func SCNetworkSetCreate(SCPreferences) -> SCNetworkSet?](scnetworksetcreate(_:).md)
  Creates a new set in the configuration.
- [func SCNetworkSetGetName(SCNetworkSet) -> CFString?](scnetworksetgetname(_:).md)
  Returns the user-specified name associated with the specified set.
- [func SCNetworkSetGetServiceOrder(SCNetworkSet) -> CFArray?](scnetworksetgetserviceorder(_:).md)
  Returns the user-specified ordering of network services within the specified set.
- [func SCNetworkSetGetSetID(SCNetworkSet) -> CFString?](scnetworksetgetsetid(_:).md)
  Returns the identifier for the specified set.
- [func SCNetworkSetGetTypeID() -> CFTypeID](scnetworksetgettypeid().md)
  Returns the type identifier of all `SCNetworkSet` instances.
- [func SCNetworkSetRemove(SCNetworkSet) -> Bool](scnetworksetremove(_:).md)
  Removes the specified set from the configuration.
- [func SCNetworkSetRemoveService(SCNetworkSet, SCNetworkService) -> Bool](scnetworksetremoveservice(_:_:).md)
  Removes the specified network service from the specified set.
- [func SCNetworkSetSetCurrent(SCNetworkSet) -> Bool](scnetworksetsetcurrent(_:).md)
  Specifies the set that should be the current set.
- [func SCNetworkSetSetName(SCNetworkSet, CFString?) -> Bool](scnetworksetsetname(_:_:).md)
  Stores the user-specified name for the specified set.
- [func SCNetworkSetSetServiceOrder(SCNetworkSet, CFArray) -> Bool](scnetworksetsetserviceorder(_:_:).md)
  Stores the user-specified ordering of network services for the specified set.
### Configuring VLAN Interfaces
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
- [func SCVLANInterfaceSetPhysicalInterfaceAndTag(SCVLANInterface, SCNetworkInterface, CFNumber) -> Bool](scvlaninterfacesetphysicalinterfaceandtag(_:_:_:).md)
  Updates the specified virtual LAN (VLAN) interface with the specified information.
### Data Types
- [class SCNetworkInterface](scnetworkinterface.md)
  The reference to an object that represents a network interface.
- [typealias SCBondInterface](scbondinterface.md)
  The reference to an object that represents an Ethernet bond interface.
- [class SCBondStatus](scbondstatus.md)
  The reference to an object that represents the status of an Ethernet bond interface.
- [typealias SCVLANInterface](scvlaninterface.md)
  The reference to an object that represents a virtual LAN (VLAN) interface.
- [class SCNetworkProtocol](scnetworkprotocol.md)
  The reference to an object that represents a network protocol.
- [class SCNetworkService](scnetworkservice.md)
  The reference to an object that represents a network service.
- [class SCNetworkSet](scnetworkset.md)
  The reference to an object that represents a network set.
### Constants
- [Ethernet Bond Aggregation Status](1546981-ethernet-bond-aggregation-status.md)
  Ethernet bond aggregation status codes.
- [Ethernet Bond Status Constants](ethernet-bond-status-constants.md)
  Ethernet bond status codes.
- [Network Interface Types](network-interface-types.md)
  Keys that identify network interface types.
- [Network Protocol Types](network-protocol-types.md)
  Keys that identify network protocol types.

## See Also

- [SCDynamicStore](scdynamicstore-gb2.md)
- [SCDynamicStoreCopySpecific](scdynamicstorecopyspecific.md)
- [SCDynamicStoreKey](scdynamicstorekey.md)
- [SCNetwork](scnetwork.md)
- [SCNetworkConnection](scnetworkconnection-g7e.md)
- [SCNetworkReachability](scnetworkreachability-g7d.md)
- [SCPreferences](scpreferences-ft8.md)
- [SCPreferencesPath](scpreferencespath.md)
- [SCPreferencesSetSpecific](scpreferencessetspecific.md)
- [SCSchemaDefinitions](scschemadefinitions.md)
- [System Configuration](system-configuration.md)
- [SystemConfiguration Enumerations](systemconfiguration-enumerations.md)
- [SystemConfiguration Constants](systemconfiguration-constants.md)
- [SystemConfiguration Functions](systemconfiguration-functions.md)
- [SystemConfiguration Data Types](systemconfiguration-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconfiguration)*