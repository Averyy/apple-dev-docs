# SCNetworkConnectionCopyUserOptions(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Gets the user options used to start the specified connection.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionCopyUserOptions(_ connection: SCNetworkConnection) -> CFDictionary?
```

```c
CFDictionaryRefSCNetworkConnectionCopyUserOptions(SCNetworkConnectionRef connection);
```

#### Return Value

The service dictionary containing the connection options (the dictionary can be empty if no user options were used), or `NULL` if an error occurred (use the [`SCError()`](./scerror%28%29.md) function to retrieve the specific error).

#### Discussion

A client can call this function to retrieve the user options previously passed to the [`SCNetworkConnectionStart(_:_:_:)`](./scnetworkconnectionstart%28_,_,_%29.md) function.

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
- [func SCNetworkConnectionGetStatus(SCNetworkConnection) -> SCNetworkConnectionStatus](./scnetworkconnectiongetstatus%28_%29.md)
  Returns the status of the specified network connection.
- [func SCNetworkConnectionCopyExtendedStatus(SCNetworkConnection) -> CFDictionary?](./scnetworkconnectioncopyextendedstatus%28_%29.md)
  Returns the extended status of the connection.
- [func SCNetworkConnectionCopyStatistics(SCNetworkConnection) -> CFDictionary?](./scnetworkconnectioncopystatistics%28_%29.md)
  Returns the statistics of the specified connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncopyuseroptions(_:))*