# SCNetworkConnectionGetTypeID()

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the type identifier of all `SCNetworkConnection` instances.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionGetTypeID() -> CFTypeID
```

```c
CFTypeID SCNetworkConnectionGetTypeID();
```

## Return Value

The type identifier of all `SCNetworkConnection` instances.

## See Also

### Getting Connection-Status Information
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectiongettypeid())*