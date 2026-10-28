# SCNetworkConfiguration

**Framework**: System Configuration  
**Role**: API Collection

## Overview

The `SCNetworkConfiguration` programming interface provides access to the stored network configuration. The functions include providing access to the network-capable devices on the system, the network sets, network services, and network protocols. Note that these functions follow Core Foundation function-name conventions. A function that has “Create” or “Copy” in its name returns a reference you must release with the [`CFRelease`](../CoreFoundation/cfrelease.md) function.

Note that when using the functions in this programming interface, you must call the [`SCPreferencesCommitChanges(_:)`](./scpreferencescommitchanges%28_%29.md) function to ensure that your changes are committed to permanent storage.

## Topics

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
- [func SCBondInterfaceSetMemberInterfaces(SCBondInterface, CFArray) -> Bool](./scbondinterfacesetmemberinterfaces%28_,_%29.md)
  Sets the member interfaces for the specified Ethernet bond interface.
- [func SCBondInterfaceSetOptions(SCBondInterface, CFDictionary) -> Bool](./scbondinterfacesetoptions%28_,_%29.md)
  Sets the configuration settings for the specified Ethernet bond interface.
- [func SCBondStatusGetInterfaceStatus(SCBondStatus, SCNetworkInterface?) -> CFDictionary?](./scbondstatusgetinterfacestatus%28_,_%29.md)
  Returns the status of the specified member interface of an Ethernet bond or the status of the bond as a whole.
- [func SCBondStatusGetMemberInterfaces(SCBondStatus) -> CFArray?](./scbondstatusgetmemberinterfaces%28_%29.md)
  Returns the member interfaces that are represented with the Ethernet bond interface.
- [func SCBondStatusGetTypeID() -> CFTypeID](./scbondstatusgettypeid%28%29.md)
  Returns the type identifier of all `SCBondStatusRef` instances.
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
- [func SCNetworkInterfaceGetTypeID() -> CFTypeID](./scnetworkinterfacegettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkInterface` instances.
- [func SCNetworkInterfaceSetConfiguration(SCNetworkInterface, CFDictionary?) -> Bool](./scnetworkinterfacesetconfiguration%28_,_%29.md)
  Stores the configuration settings for the specified interface.
- [func SCNetworkInterfaceSetExtendedConfiguration(SCNetworkInterface, CFString, CFDictionary?) -> Bool](./scnetworkinterfacesetextendedconfiguration%28_,_,_%29.md)
  Stores the extended configuration settings for the specified interface.
- [func SCNetworkInterfaceSetMTU(SCNetworkInterface, Int32) -> Bool](./scnetworkinterfacesetmtu%28_,_%29.md)
  Sets the requested MTU setting for the specified network interface.
- [func SCNetworkInterfaceSetMediaOptions(SCNetworkInterface, CFString?, CFArray?) -> Bool](./scnetworkinterfacesetmediaoptions%28_,_,_%29.md)
  Sets the requested media subtype and options for the specified network interface.
### Configuring Network Protocols
- [func SCNetworkProtocolGetConfiguration(SCNetworkProtocol) -> CFDictionary?](./scnetworkprotocolgetconfiguration%28_%29.md)
  Returns the configuration settings associated with the specified protocol.
- [func SCNetworkProtocolGetEnabled(SCNetworkProtocol) -> Bool](./scnetworkprotocolgetenabled%28_%29.md)
  Returns a Boolean value indicating whether the specified protocol is enabled.
- [func SCNetworkProtocolGetProtocolType(SCNetworkProtocol) -> CFString?](./scnetworkprotocolgetprotocoltype%28_%29.md)
  Returns the type of the specified network protocol.
- [func SCNetworkProtocolGetTypeID() -> CFTypeID](./scnetworkprotocolgettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkProtocol` instances.
- [func SCNetworkProtocolSetConfiguration(SCNetworkProtocol, CFDictionary?) -> Bool](./scnetworkprotocolsetconfiguration%28_,_%29.md)
  Stores the configuration settings for the specified network protocol.
- [func SCNetworkProtocolSetEnabled(SCNetworkProtocol, Bool) -> Bool](./scnetworkprotocolsetenabled%28_,_%29.md)
  Enables or disables the specified protocol.
### Configuring Network Services
- [func SCNetworkServiceAddProtocolType(SCNetworkService, CFString) -> Bool](./scnetworkserviceaddprotocoltype%28_,_%29.md)
  Adds the network protocol of the specified type to the specified service.
- [func SCNetworkServiceCopy(SCPreferences, CFString) -> SCNetworkService?](./scnetworkservicecopy%28_,_%29.md)
  Returns the network service with the specified identifier.
- [func SCNetworkServiceCopyAll(SCPreferences) -> CFArray?](./scnetworkservicecopyall%28_%29.md)
  Returns all available network services for the specified preferences.
- [func SCNetworkServiceCopyProtocol(SCNetworkService, CFString) -> SCNetworkProtocol?](./scnetworkservicecopyprotocol%28_,_%29.md)
  Returns the network protocol of the specified type for the specified service.
- [func SCNetworkServiceCopyProtocols(SCNetworkService) -> CFArray?](./scnetworkservicecopyprotocols%28_%29.md)
  Returns all network protocols associated with the specified service.
- [func SCNetworkServiceCreate(SCPreferences, SCNetworkInterface) -> SCNetworkService?](./scnetworkservicecreate%28_,_%29.md)
  Creates a new network service for the specified interface in the configuration.
- [func SCNetworkServiceEstablishDefaultConfiguration(SCNetworkService) -> Bool](./scnetworkserviceestablishdefaultconfiguration%28_%29.md)
  Establishes the default configuration for the specified network service.
- [func SCNetworkServiceGetEnabled(SCNetworkService) -> Bool](./scnetworkservicegetenabled%28_%29.md)
  Returns a Boolean value indicating whether the specified service is enabled.
- [func SCNetworkServiceGetInterface(SCNetworkService) -> SCNetworkInterface?](./scnetworkservicegetinterface%28_%29.md)
  Returns the network interface associated with the specified service.
- [func SCNetworkServiceGetName(SCNetworkService) -> CFString?](./scnetworkservicegetname%28_%29.md)
  Returns the user-specified name associated with the specified service.
- [func SCNetworkServiceGetServiceID(SCNetworkService) -> CFString?](./scnetworkservicegetserviceid%28_%29.md)
  Returns the identifier for the specified service.
- [func SCNetworkServiceGetTypeID() -> CFTypeID](./scnetworkservicegettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkService` instances.
- [func SCNetworkServiceRemove(SCNetworkService) -> Bool](./scnetworkserviceremove%28_%29.md)
  Removes the specified network service from the configuration.
- [func SCNetworkServiceRemoveProtocolType(SCNetworkService, CFString) -> Bool](./scnetworkserviceremoveprotocoltype%28_,_%29.md)
  Removes the network protocol of the specified type from the specified service.
- [func SCNetworkServiceSetEnabled(SCNetworkService, Bool) -> Bool](./scnetworkservicesetenabled%28_,_%29.md)
  Enables or disables the specified service.
- [func SCNetworkServiceSetName(SCNetworkService, CFString?) -> Bool](./scnetworkservicesetname%28_,_%29.md)
  Stores the user-specified name for the specified service.
### Configuring Network Sets
- [func SCNetworkSetAddService(SCNetworkSet, SCNetworkService) -> Bool](./scnetworksetaddservice%28_,_%29.md)
  Adds the specified network service to the specified set.
- [func SCNetworkSetContainsInterface(SCNetworkSet, SCNetworkInterface) -> Bool](./scnetworksetcontainsinterface%28_,_%29.md)
  Returns a Boolean value indicating whether the specified interface is represented by at least one network service in the specified set.
- [func SCNetworkSetCopy(SCPreferences, CFString) -> SCNetworkSet?](./scnetworksetcopy%28_,_%29.md)
  Returns the set with the specified identifier.
- [func SCNetworkSetCopyAll(SCPreferences) -> CFArray?](./scnetworksetcopyall%28_%29.md)
  Returns all available sets for the specified preferences session.
- [func SCNetworkSetCopyCurrent(SCPreferences) -> SCNetworkSet?](./scnetworksetcopycurrent%28_%29.md)
  Returns the current set.
- [func SCNetworkSetCopyServices(SCNetworkSet) -> CFArray?](./scnetworksetcopyservices%28_%29.md)
  Returns all network services associated with the specified set.
- [func SCNetworkSetCreate(SCPreferences) -> SCNetworkSet?](./scnetworksetcreate%28_%29.md)
  Creates a new set in the configuration.
- [func SCNetworkSetGetName(SCNetworkSet) -> CFString?](./scnetworksetgetname%28_%29.md)
  Returns the user-specified name associated with the specified set.
- [func SCNetworkSetGetServiceOrder(SCNetworkSet) -> CFArray?](./scnetworksetgetserviceorder%28_%29.md)
  Returns the user-specified ordering of network services within the specified set.
- [func SCNetworkSetGetSetID(SCNetworkSet) -> CFString?](./scnetworksetgetsetid%28_%29.md)
  Returns the identifier for the specified set.
- [func SCNetworkSetGetTypeID() -> CFTypeID](./scnetworksetgettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkSet` instances.
- [func SCNetworkSetRemove(SCNetworkSet) -> Bool](./scnetworksetremove%28_%29.md)
  Removes the specified set from the configuration.
- [func SCNetworkSetRemoveService(SCNetworkSet, SCNetworkService) -> Bool](./scnetworksetremoveservice%28_,_%29.md)
  Removes the specified network service from the specified set.
- [func SCNetworkSetSetCurrent(SCNetworkSet) -> Bool](./scnetworksetsetcurrent%28_%29.md)
  Specifies the set that should be the current set.
- [func SCNetworkSetSetName(SCNetworkSet, CFString?) -> Bool](./scnetworksetsetname%28_,_%29.md)
  Stores the user-specified name for the specified set.
- [func SCNetworkSetSetServiceOrder(SCNetworkSet, CFArray) -> Bool](./scnetworksetsetserviceorder%28_,_%29.md)
  Stores the user-specified ordering of network services for the specified set.
### Configuring VLAN Interfaces
- [func SCVLANInterfaceCopyAll(SCPreferences) -> CFArray](./scvlaninterfacecopyall%28_%29.md)
  Returns all virtual LAN (VLAN) interfaces on the system.
- [func SCVLANInterfaceCopyAvailablePhysicalInterfaces() -> CFArray](./scvlaninterfacecopyavailablephysicalinterfaces%28%29.md)
  Returns the network capable devices on the system that can be associated with a virtual LAN (VLAN) interface.
- [func SCVLANInterfaceCreate(SCPreferences, SCNetworkInterface, CFNumber) -> SCVLANInterface?](./scvlaninterfacecreate%28_,_,_%29.md)
  Creates a new virtual LAN (VLAN) interface.
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
### Data Types
- [class SCNetworkInterface](./scnetworkinterface.md)
  The reference to an object that represents a network interface.
- [typealias SCBondInterface](./scbondinterface.md)
  The reference to an object that represents an Ethernet bond interface.
- [class SCBondStatus](./scbondstatus.md)
  The reference to an object that represents the status of an Ethernet bond interface.
- [typealias SCVLANInterface](./scvlaninterface.md)
  The reference to an object that represents a virtual LAN (VLAN) interface.
- [class SCNetworkProtocol](./scnetworkprotocol.md)
  The reference to an object that represents a network protocol.
- [class SCNetworkService](./scnetworkservice.md)
  The reference to an object that represents a network service.
- [class SCNetworkSet](./scnetworkset.md)
  The reference to an object that represents a network set.
### Constants
- [Ethernet Bond Aggregation Status](./api-1546981-ethernet-bond-aggregation-status.md)
  Ethernet bond aggregation status codes.
- [Ethernet Bond Status Constants](./ethernet-bond-status-constants.md)
  Ethernet bond status codes.
- [Network Interface Types](./network-interface-types.md)
  Keys that identify network interface types.
- [Network Protocol Types](./network-protocol-types.md)
  Keys that identify network protocol types.

## See Also

### Reference
- [SCDynamicStore](./scdynamicstore-gb2.md)
- [SCDynamicStoreCopySpecific](./scdynamicstorecopyspecific.md)
- [SCDynamicStoreKey](./scdynamicstorekey.md)
- [SCNetwork](./scnetwork.md)
- [SCNetworkConnection](./scnetworkconnection-g7e.md)
- [SCNetworkReachability](./scnetworkreachability-g7d.md)
- [SCPreferences](./scpreferences-ft8.md)
- [SCPreferencesPath](./scpreferencespath.md)
- [SCPreferencesSetSpecific](./scpreferencessetspecific.md)
- [SCSchemaDefinitions](./scschemadefinitions.md)
- [System Configuration](./system-configuration.md)
- [SystemConfiguration Enumerations](./systemconfiguration-enumerations.md)
- [SystemConfiguration Constants](./systemconfiguration-constants.md)
- [SystemConfiguration Functions](./systemconfiguration-functions.md)
- [SystemConfiguration Data Types](./systemconfiguration-data-types.md)
- [DHCPClientPreferences](./dhcpclientpreferences.md)
- [SCDynamicStoreCopyDHCPInfo](./scdynamicstorecopydhcpinfo-apicollection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconfiguration)*