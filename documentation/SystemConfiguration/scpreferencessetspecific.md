# SCPreferencesSetSpecific

**Framework**: System Configuration  
**Role**: API Collection

## Overview

The functions in the `SCPreferencesSetSpecific` programming interface allow an application to set specific configuration information about the current system (for example, the computer or sharing name). Note that to access configuration preferences, you must first establish a preferences session using the [`SCPreferencesCreate(_:_:_:)`](./scpreferencescreate%28_,_,_%29.md) function.

## Topics

### Setting Configuration Information
- [func SCPreferencesSetComputerName(SCPreferences, CFString?, CFStringEncoding) -> Bool](./scpreferencessetcomputername%28_,_,_%29.md)
  Sets the computer name preference to the specified name.
- [func SCPreferencesSetLocalHostName(SCPreferences, CFString?) -> Bool](./scpreferencessetlocalhostname%28_,_%29.md)
  Sets the local host name to the specified name.

## See Also

### Reference
- [SCDynamicStore](./scdynamicstore-gb2.md)
- [SCDynamicStoreCopySpecific](./scdynamicstorecopyspecific.md)
- [SCDynamicStoreKey](./scdynamicstorekey.md)
- [SCNetwork](./scnetwork.md)
- [SCNetworkConfiguration](./scnetworkconfiguration.md)
- [SCNetworkConnection](./scnetworkconnection-g7e.md)
- [SCNetworkReachability](./scnetworkreachability-g7d.md)
- [SCPreferences](./scpreferences-ft8.md)
- [SCPreferencesPath](./scpreferencespath.md)
- [SCSchemaDefinitions](./scschemadefinitions.md)
- [System Configuration](./system-configuration.md)
- [SystemConfiguration Enumerations](./systemconfiguration-enumerations.md)
- [SystemConfiguration Constants](./systemconfiguration-constants.md)
- [SystemConfiguration Functions](./systemconfiguration-functions.md)
- [SystemConfiguration Data Types](./systemconfiguration-data-types.md)
- [DHCPClientPreferences](./dhcpclientpreferences.md)
- [SCDynamicStoreCopyDHCPInfo](./scdynamicstorecopydhcpinfo-apicollection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencessetspecific)*