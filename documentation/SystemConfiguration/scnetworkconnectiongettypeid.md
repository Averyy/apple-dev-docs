# SCNetworkConnectionGetTypeID()

**Framework**: System Configuration  
**Kind**: func

Returns the type identifier of all `SCNetworkConnection` instances.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionGetTypeID() -> CFTypeID
```

#### Return Value

The type identifier of all `SCNetworkConnection` instances.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectiongettypeid())*