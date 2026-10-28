# SCNetworkConnectionCopyStatistics(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the statistics of the specified connection.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionCopyStatistics(_ connection: SCNetworkConnection) -> CFDictionary?
```

```c
CFDictionaryRefSCNetworkConnectionCopyStatistics(SCNetworkConnectionRef connection);
```

## Return Value

The statistics dictionary, or `NULL` if an error occurred (use the [`SCError()`](./scerror%28%29.md) function to retrieve the specific error).

## Discussion

A statistics dictionary contains specific dictionaries with statistics for each subcomponent of the service. For example, a statistics dictionary for PPP contains the following sub-dictionaries, keys, and values:

| Sub-dictionary | Key | Value |
| --- | --- | --- |
| PPP | `BytesIn` | The number of bytes going up into the network stack for any networking protocol without the PPP headers and trailers. |
| PPP | `BytesOut` | The number of bytes coming out of the network stack for any networking protocol without the PPP headers and trailers. |
| PPP | `PacketsIn` | The number of packets going up into the network stack for any networking protocol without the PPP headers and trailers. |
| PPP | `PacketsOut` | The number of packets coming out of the network stack for any networking protocol without the PPP headers and trailers. |
| PPP | `ErrorsIn` | The number of errors going up into the network stack for any networking protocol without the PPP headers and trailers. |
| PPP | `ErrorsOut` | The number of errors coming out of the network stack for any networking protocol without the PPP headers and trailers. |

See [Statistics Dictionary Keys](./statistics-dictionary-keys.md) for the keys to use in the statistics dictionary.

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
- [func SCNetworkConnectionCopyUserOptions(SCNetworkConnection) -> CFDictionary?](./scnetworkconnectioncopyuseroptions%28_%29.md)
  Gets the user options used to start the specified connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncopystatistics(_:))*