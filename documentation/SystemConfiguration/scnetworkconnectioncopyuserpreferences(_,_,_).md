# SCNetworkConnectionCopyUserPreferences(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Provides the default service ID and a dictionary of user options for the specified connection.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionCopyUserPreferences(_ selectionOptions: CFDictionary?, _ serviceID: UnsafeMutablePointer<Unmanaged<CFString>?>, _ userOptions: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> Bool
```

```c
Boolean SCNetworkConnectionCopyUserPreferences(CFDictionaryRef selectionOptions, CFStringRef*serviceID, CFDictionaryRef*userOptions);
```

## Return Value

`TRUE` if there is a valid service to dial; `FALSE` if the function was unable to retrieve a service to dial.

## Discussion

You can use the service ID and user options values returned by this function to open a connection on the fly.

## Parameters

- `selectionOptions`: Currently unimplemented. Pass `NULL`.
- `serviceID`: On output, a reference to the default service ID for starting connections.
- `userOptions`: On output, a reference to the default user options dictionary for starting connections.

## See Also

### Getting Connection-Status Information
- [func SCNetworkConnectionGetTypeID() -> CFTypeID](./scnetworkconnectiongettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkConnection` instances.
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

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncopyuserpreferences(_:_:_:))*