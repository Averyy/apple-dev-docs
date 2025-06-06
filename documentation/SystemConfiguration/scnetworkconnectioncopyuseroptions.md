# SCNetworkConnectionCopyUserOptions(_:)

**Framework**: System Configuration  
**Kind**: func

Gets the user options used to start the specified connection.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionCopyUserOptions(_ connection: SCNetworkConnection) -> CFDictionary?
```

#### Return Value

The service dictionary containing the connection options (the dictionary can be empty if no user options were used), or `NULL` if an error occurred (use the [`SCError()`](scerror().md) function to retrieve the specific error).

#### Discussion

A client can call this function to retrieve the user options previously passed to the [`SCNetworkConnectionStart(_:_:_:)`](scnetworkconnectionstart(_:_:_:).md) function.

## Parameters

- `connection`: The network connection.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncopyuseroptions(_:))*