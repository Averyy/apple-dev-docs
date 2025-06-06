# SCNetworkConnectionGetStatus(_:)

**Framework**: System Configuration  
**Kind**: func

Returns the status of the specified network connection.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionGetStatus(_ connection: SCNetworkConnection) -> SCNetworkConnectionStatus
```

#### Return Value

The status of the network connection. See [`SCNetworkConnectionStatus`](scnetworkconnectionstatus.md) for a list of possible values.

## Parameters

- `connection`: The network connection.

## See Also

- [func SCNetworkConnectionGetTypeID() -> CFTypeID](scnetworkconnectiongettypeid().md)
  Returns the type identifier of all `SCNetworkConnection` instances.
- [func SCNetworkConnectionCopyUserPreferences(CFDictionary?, UnsafeMutablePointer<Unmanaged<CFString>?>, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> Bool](scnetworkconnectioncopyuserpreferences(_:_:_:).md)
  Provides the default service ID and a dictionary of user options for the specified connection.
- [func SCNetworkConnectionCopyServiceID(SCNetworkConnection) -> CFString?](scnetworkconnectioncopyserviceid(_:).md)
  Returns the service ID associated with the specified network connection.
- [func SCNetworkConnectionCopyExtendedStatus(SCNetworkConnection) -> CFDictionary?](scnetworkconnectioncopyextendedstatus(_:).md)
  Returns the extended status of the connection.
- [func SCNetworkConnectionCopyStatistics(SCNetworkConnection) -> CFDictionary?](scnetworkconnectioncopystatistics(_:).md)
  Returns the statistics of the specified connection.
- [func SCNetworkConnectionCopyUserOptions(SCNetworkConnection) -> CFDictionary?](scnetworkconnectioncopyuseroptions(_:).md)
  Gets the user options used to start the specified connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectiongetstatus(_:))*