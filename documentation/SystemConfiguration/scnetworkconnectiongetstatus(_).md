# SCNetworkConnectionGetStatus(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the status of the specified network connection.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionGetStatus(_ connection: SCNetworkConnection) -> SCNetworkConnectionStatus
```

```c
SCNetworkConnectionStatus SCNetworkConnectionGetStatus(SCNetworkConnectionRef connection);
```

## Return Value

The status of the network connection. See [`SCNetworkConnectionStatus`](./scnetworkconnectionstatus.md) for a list of possible values.

## Parameters

- `connection`: The network connection.

## See Also

### Getting Connection-Status Information
- [func SCNetworkConnectionGetTypeID() -> CFTypeID](./scnetworkconnectiongettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkConnection` instances.
- [func SCNetworkConnectionCopyUserPreferences(CFDictionary?, UnsafeMutablePointer<Unmanaged<CFString>?>, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> Bool](./scnetworkconnectioncopyuserpreferences%28_,_,_%29.md)
  Provides the default service ID and a dictionary of user options for the specified connection.
- [func SCNetworkConnectionCopyServiceID(SCNetworkConnection) -> CFString?](./scnetworkconnectioncopyserviceid%28_%29.md)
  Returns the service ID associated with the specified network connection.
- [func SCNetworkConnectionCopyExtendedStatus(SCNetworkConnection) -> CFDictionary?](./scnetworkconnectioncopyextendedstatus%28_%29.md)
  Returns the extended status of the connection.
- [func SCNetworkConnectionCopyStatistics(SCNetworkConnection) -> CFDictionary?](./scnetworkconnectioncopystatistics%28_%29.md)
  Returns the statistics of the specified connection.
- [func SCNetworkConnectionCopyUserOptions(SCNetworkConnection) -> CFDictionary?](./scnetworkconnectioncopyuseroptions%28_%29.md)
  Gets the user options used to start the specified connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectiongetstatus(_:))*