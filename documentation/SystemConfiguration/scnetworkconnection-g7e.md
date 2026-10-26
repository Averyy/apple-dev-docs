# SCNetworkConnection

**Framework**: System Configuration  
**Role**: API Collection

#### Overview

The `SCNetworkConnection` programming interface contains functions that allow an application to control connection-oriented services defined in the system and get connection-status information. Note that these functions allow you to control and get information about existing services only. If you need to create, change, or remove services, you should use the `SCNetworkConfiguration` programming interface instead.

> **Note**:  Currently, only PPP services can be controlled.

## Topics

### Getting Connection-Status Information
- [func SCNetworkConnectionGetTypeID() -> CFTypeID](./scnetworkconnectiongettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkConnection` instances.
- [func SCNetworkConnectionCopyUserPreferences(CFDictionary?, UnsafeMutablePointer<Unmanaged<CFString>?>, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> Bool](./scnetworkconnectioncopyuserpreferences%28_,_,_%29.md)
  Provides the default service ID and a dictionary of user options for the specified connection.
- [func SCNetworkConnectionCopyServiceID(SCNetworkConnection) -> CFString?](./scnetworkconnectioncopyserviceid%28_%29.md)
  Returns the service ID associated with the specified network connection.
- [func SCNetworkConnectionGetStatus(SCNetworkConnection) -> SCNetworkConnectionStatus](./scnetworkconnectiongetstatus%28_%29.md)
  Returns the status of the specified network connection.
- [func SCNetworkConnectionCopyExtendedStatus(SCNetworkConnection) -> CFDictionary?](./scnetworkconnectioncopyextendedstatus%28_%29.md)
  Returns the extended status of the connection.
- [func SCNetworkConnectionCopyStatistics(SCNetworkConnection) -> CFDictionary?](./scnetworkconnectioncopystatistics%28_%29.md)
  Returns the statistics of the specified connection.
- [func SCNetworkConnectionCopyUserOptions(SCNetworkConnection) -> CFDictionary?](./scnetworkconnectioncopyuseroptions%28_%29.md)
  Gets the user options used to start the specified connection.
### Starting and Stopping a Connection
- [func SCNetworkConnectionStart(SCNetworkConnection, CFDictionary?, Bool) -> Bool](./scnetworkconnectionstart%28_,_,_%29.md)
  Starts the connection process for the specified network connection.
- [func SCNetworkConnectionStop(SCNetworkConnection, Bool) -> Bool](./scnetworkconnectionstop%28_,_%29.md)
  Stops the connection process for the specified network connection.
### Scheduling a Connection Reference on a Run Loop
- [func SCNetworkConnectionScheduleWithRunLoop(SCNetworkConnection, CFRunLoop, CFString) -> Bool](./scnetworkconnectionschedulewithrunloop%28_,_,_%29.md)
  Schedules the specified connection with the specified run loop.
- [func SCNetworkConnectionUnscheduleFromRunLoop(SCNetworkConnection, CFRunLoop, CFString) -> Bool](./scnetworkconnectionunschedulefromrunloop%28_,_,_%29.md)
  Unschedules the specified connection from the specified run loop.
### Creating a Connection Reference
- [func SCNetworkConnectionCreateWithServiceID(CFAllocator?, CFString, SCNetworkConnectionCallBack?, UnsafeMutablePointer<SCNetworkConnectionContext>?) -> SCNetworkConnection?](./scnetworkconnectioncreatewithserviceid%28_,_,_,_%29.md)
  Creates a new connection reference to use for getting the status or for connecting or disconnecting the associated service.
### Specifying a Dispatch Queue and Enabling Notifications
- [func SCNetworkConnectionSetDispatchQueue(SCNetworkConnection, dispatch_queue_t?) -> Bool](./scnetworkconnectionsetdispatchqueue%28_,_%29.md)
  Specifies a dispatch queue to use for the connection’s callback function and enables notifications.
### Data Types
- [class SCNetworkConnection](./scnetworkconnection.md)
  The handle to manage a connection-oriented service.
- [typealias SCNetworkConnectionCallBack](./scnetworkconnectioncallback.md)
  The type of callback function used when a status event is delivered.
- [struct SCNetworkConnectionContext](./scnetworkconnectioncontext.md)
  A structure containing user-specified data and callbacks for a network connection.
### Constants
- [enum SCNetworkConnectionStatus](./scnetworkconnectionstatus.md)
  The current status of the network connection.
- [enum SCNetworkConnectionPPPStatus](./scnetworkconnectionpppstatus.md)
  The PPP-specific status of the network connection.
- [Statistics Dictionary Keys](./statistics-dictionary-keys.md)
  Keys associated with values in the statistics dictionary.
- [Selection Options Dictionary Keys](./selection-options-dictionary-keys.md)
  Keys used with the [`SCNetworkConnectionCopyUserPreferences(_:_:_:)`](./scnetworkconnectioncopyuserpreferences%28_,_,_%29.md) selection options dictionary.

## See Also

### Reference
- [SCDynamicStore](./scdynamicstore-gb2.md)
- [SCDynamicStoreCopySpecific](./scdynamicstorecopyspecific.md)
- [SCDynamicStoreKey](./scdynamicstorekey.md)
- [SCNetwork](./scnetwork.md)
- [SCNetworkConfiguration](./scnetworkconfiguration.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnection-g7e)*