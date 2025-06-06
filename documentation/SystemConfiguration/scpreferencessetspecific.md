# SCPreferencesSetSpecific

**Framework**: System Configuration

#### Overview

The functions in the `SCPreferencesSetSpecific` programming interface allow an application to set specific configuration information about the current system (for example, the computer or sharing name). Note that to access configuration preferences, you must first establish a preferences session using the [`SCPreferencesCreate(_:_:_:)`](scpreferencescreate(_:_:_:).md) function.

## Topics

### Setting Configuration Information
- [func SCPreferencesSetComputerName(SCPreferences, CFString?, CFStringEncoding) -> Bool](scpreferencessetcomputername(_:_:_:).md)
  Sets the computer name preference to the specified name.
- [func SCPreferencesSetLocalHostName(SCPreferences, CFString?) -> Bool](scpreferencessetlocalhostname(_:_:).md)
  Sets the local host name to the specified name.

## See Also

- [SCDynamicStore](scdynamicstore-gb2.md)
- [SCDynamicStoreCopySpecific](scdynamicstorecopyspecific.md)
- [SCDynamicStoreKey](scdynamicstorekey.md)
- [SCNetwork](scnetwork.md)
- [SCNetworkConfiguration](scnetworkconfiguration.md)
- [SCNetworkConnection](scnetworkconnection-g7e.md)
- [SCNetworkReachability](scnetworkreachability-g7d.md)
- [SCPreferences](scpreferences-ft8.md)
- [SCPreferencesPath](scpreferencespath.md)
- [SCSchemaDefinitions](scschemadefinitions.md)
- [System Configuration](system-configuration.md)
- [SystemConfiguration Enumerations](systemconfiguration-enumerations.md)
- [SystemConfiguration Constants](systemconfiguration-constants.md)
- [SystemConfiguration Functions](systemconfiguration-functions.md)
- [SystemConfiguration Data Types](systemconfiguration-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencessetspecific)*