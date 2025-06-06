# SCDynamicStoreKey

**Framework**: System Configuration

#### Overview

The `SCDynamicStoreKey` programming interface provides convenience functions that an application can use to create a correctly formatted dynamic store key for accessing specific items in the dynamic store. An application can then use the resulting string in any function that requires a dynamic store key.

## Topics

### Group
- [func SCDynamicStoreKeyCreateNetworkGlobalEntity(CFAllocator?, CFString, CFString) -> CFString](scdynamicstorekeycreatenetworkglobalentity(_:_:_:).md)
  Creates a dynamic store key that can be used to access a specific global (as opposed to a per-service or per-interface) network configuration entity.
- [func SCDynamicStoreKeyCreateNetworkInterface(CFAllocator?, CFString) -> CFString](scdynamicstorekeycreatenetworkinterface(_:_:).md)
  Creates a dynamic store key that can be used to access the network interface configuration information in the dynamic store.
- [func SCDynamicStoreKeyCreateNetworkInterfaceEntity(CFAllocator?, CFString, CFString, CFString?) -> CFString](scdynamicstorekeycreatenetworkinterfaceentity(_:_:_:_:).md)
  Creates a dynamic store key that can be used to access the per-interface network configuration information in the dynamic store.
- [func SCDynamicStoreKeyCreateNetworkServiceEntity(CFAllocator?, CFString, CFString, CFString?) -> CFString](scdynamicstorekeycreatenetworkserviceentity(_:_:_:_:).md)
  Creates a dynamic store key that can be used to access the per-service network configuration information.
- [func SCDynamicStoreKeyCreateComputerName(CFAllocator?) -> CFString](scdynamicstorekeycreatecomputername(_:).md)
  Creates a key that can be used to receive notifications when the current computer name changes.
- [func SCDynamicStoreKeyCreateConsoleUser(CFAllocator?) -> CFString](scdynamicstorekeycreateconsoleuser(_:).md)
  Creates a key that can be used to receive notifications when the current console user changes.
- [func SCDynamicStoreKeyCreateHostNames(CFAllocator?) -> CFString](scdynamicstorekeycreatehostnames(_:).md)
  Creates a key that can be used to receive notifications when the `HostNames` entity changes.
- [func SCDynamicStoreKeyCreateLocation(CFAllocator?) -> CFString](scdynamicstorekeycreatelocation(_:).md)
  Creates a key that can be used to receive notifications when the location identifier changes.
- [func SCDynamicStoreKeyCreateProxies(CFAllocator?) -> CFString](scdynamicstorekeycreateproxies(_:).md)
  Creates a key that can be used to receive notifications when the current network proxy settings are changed.

## See Also

- [SCDynamicStore](scdynamicstore-gb2.md)
- [SCDynamicStoreCopySpecific](scdynamicstorecopyspecific.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorekey)*