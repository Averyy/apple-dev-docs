# SCNetwork

**Framework**: System Configuration

#### Overview

The `SCNetwork` programming interface contains functions an application can use to determine whether that application can reach a remote host and to notify the system of configuration changes.

A remote host is considered reachable when a data packet, sent by an application into the network stack, can leave the local computer. Note that reachability does not guarantee that the data packet will actually be received by the host.

## Topics

### Constants
- [typealias SCNetworkConnectionFlags](scnetworkconnectionflags.md)
  Flags that indicate whether the specified network node name or address is reachable, whether a connection is required, and whether some user intervention may be required when establishing a connection.

## See Also

- [SCDynamicStore](scdynamicstore-gb2.md)
- [SCDynamicStoreCopySpecific](scdynamicstorecopyspecific.md)
- [SCDynamicStoreKey](scdynamicstorekey.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetwork)*