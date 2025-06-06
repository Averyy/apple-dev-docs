# SCNetworkConnection

**Framework**: Systemconfiguration

#### Overview

The `SCNetworkConnection` programming interface contains functions that allow an application to control connection-oriented services defined in the system and get connection-status information. Note that these functions allow you to control and get information about existing services only. If you need to create, change, or remove services, you should use the `SCNetworkConfiguration` programming interface instead.

> **Note**:  Currently, only PPP services can be controlled.

## Topics

### Getting Connection-Status Information
- [func SCNetworkConnectionGetTypeID() -> CFTypeID](scnetworkconnectiongettypeid().md)
  Returns the type identifier of all `SCNetworkConnection` instances.
- [func SCNetworkConnectionCopyUserPreferences(CFDictionary?, UnsafeMutablePointer<Unmanaged<CFString>?>, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> Bool](scnetworkconnectioncopyuserpreferences(_:_:_:).md)
  Provides the default service ID and a dictionary of user options for the specified connection.
- [func SCNetworkConnectionCopyServiceID(SCNetworkConnection) -> CFString?](scnetworkconnectioncopyserviceid(_:).md)
  Returns the service ID associated with the specified network connection.
- [func SCNetworkConnectionGetStatus(SCNetworkConnection) -> SCNetworkConnectionStatus](scnetworkconnectiongetstatus(_:).md)
  Returns the status of the specified network connection.
- [func SCNetworkConnectionCopyExtendedStatus(SCNetworkConnection) -> CFDictionary?](scnetworkconnectioncopyextendedstatus(_:).md)
  Returns the extended status of the connection.
- [func SCNetworkConnectionCopyStatistics(SCNetworkConnection) -> CFDictionary?](scnetworkconnectioncopystatistics(_:).md)
  Returns the statistics of the specified connection.
- [func SCNetworkConnectionCopyUserOptions(SCNetworkConnection) -> CFDictionary?](scnetworkconnectioncopyuseroptions(_:).md)
  Gets the user options used to start the specified connection.
### Starting and Stopping a Connection
- [func SCNetworkConnectionStart(SCNetworkConnection, CFDictionary?, Bool) -> Bool](scnetworkconnectionstart(_:_:_:).md)
  Starts the connection process for the specified network connection.
- [func SCNetworkConnectionStop(SCNetworkConnection, Bool) -> Bool](scnetworkconnectionstop(_:_:).md)
  Stops the connection process for the specified network connection.
### Scheduling a Connection Reference on a Run Loop
- [func SCNetworkConnectionScheduleWithRunLoop(SCNetworkConnection, CFRunLoop, CFString) -> Bool](scnetworkconnectionschedulewithrunloop(_:_:_:).md)
  Schedules the specified connection with the specified run loop.
- [func SCNetworkConnectionUnscheduleFromRunLoop(SCNetworkConnection, CFRunLoop, CFString) -> Bool](scnetworkconnectionunschedulefromrunloop(_:_:_:).md)
  Unschedules the specified connection from the specified run loop.
### Creating a Connection Reference
- [func SCNetworkConnectionCreateWithServiceID(CFAllocator?, CFString, SCNetworkConnectionCallBack?, UnsafeMutablePointer<SCNetworkConnectionContext>?) -> SCNetworkConnection?](scnetworkconnectioncreatewithserviceid(_:_:_:_:).md)
  Creates a new connection reference to use for getting the status or for connecting or disconnecting the associated service.
### Specifying a Dispatch Queue and Enabling Notifications
- [func SCNetworkConnectionSetDispatchQueue(SCNetworkConnection, dispatch_queue_t?) -> Bool](scnetworkconnectionsetdispatchqueue(_:_:).md)
  Specifies a dispatch queue to use for the connection’s callback function and enables notifications.
### Data Types
- [class SCNetworkConnection](scnetworkconnection.md)
  The handle to manage a connection-oriented service.
- [typealias SCNetworkConnectionCallBack](scnetworkconnectioncallback.md)
  The type of callback function used when a status event is delivered.
- [struct SCNetworkConnectionContext](scnetworkconnectioncontext.md)
  A structure containing user-specified data and callbacks for a network connection.
### Constants
- [enum SCNetworkConnectionStatus](scnetworkconnectionstatus.md)
  The current status of the network connection.
- [enum SCNetworkConnectionPPPStatus](scnetworkconnectionpppstatus.md)
  The PPP-specific status of the network connection.
- [Statistics Dictionary Keys](statistics-dictionary-keys.md)
  Keys associated with values in the statistics dictionary.
- [Selection Options Dictionary Keys](selection-options-dictionary-keys.md)
  Keys used with the [`SCNetworkConnectionCopyUserPreferences(_:_:_:)`](scnetworkconnectioncopyuserpreferences(_:_:_:).md) selection options dictionary.

## See Also

- [SCDynamicStore](scdynamicstore-gb2.md)
- [SCDynamicStoreCopySpecific](scdynamicstorecopyspecific.md)
- [SCDynamicStoreKey](scdynamicstorekey.md)
- [SCNetwork](scnetwork.md)
- [SCNetworkConfiguration](scnetworkconfiguration.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/SystemConfiguration/scnetworkconnection-g7e)*