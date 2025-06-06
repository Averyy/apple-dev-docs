# SCDynamicStoreCopySpecific

**Framework**: System Configuration

#### Overview

The functions of the `SCDynamicStoreCopySpecific` programming interface allow an application to determine specific configuration information about the current system (for example, the computer or sharing name or the currently logged-in user). Note that these functions follow Core Foundation function-name conventions. A function that has “Create” or “Copy” in its name returns a reference you must release with the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function.

## Topics

### Group
- [func SCDynamicStoreCopyComputerName(SCDynamicStore?, UnsafeMutablePointer<CFStringEncoding>?) -> CFString?](scdynamicstorecopycomputername(_:_:).md)
  Returns the current computer name.
- [func SCDynamicStoreCopyConsoleUser(SCDynamicStore?, UnsafeMutablePointer<uid_t>?, UnsafeMutablePointer<gid_t>?) -> CFString?](scdynamicstorecopyconsoleuser(_:_:_:).md)
  Returns information about the user currently logged into the system.
- [func SCDynamicStoreCopyLocalHostName(SCDynamicStore?) -> CFString?](scdynamicstorecopylocalhostname(_:).md)
  Returns the current local host name.
- [func SCDynamicStoreCopyLocation(SCDynamicStore?) -> CFString?](scdynamicstorecopylocation(_:).md)
  Returns the current location identifier.
- [func SCDynamicStoreCopyProxies(SCDynamicStore?) -> CFDictionary?](scdynamicstorecopyproxies(_:).md)
  Returns the key-value pairs that represent the current internet proxy settings.

## See Also

- [SCDynamicStore](scdynamicstore-gb2.md)
- [SCDynamicStoreKey](scdynamicstorekey.md)
- [SCNetwork](scnetwork.md)
- [SCNetworkConfiguration](scnetworkconfiguration.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecopyspecific)*