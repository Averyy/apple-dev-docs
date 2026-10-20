# SCNetworkConnectionCopyExtendedStatus(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the extended status of the connection.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionCopyExtendedStatus(_ connection: SCNetworkConnection) -> CFDictionary?
```

```c
CFDictionaryRefSCNetworkConnectionCopyExtendedStatus(SCNetworkConnectionRef connection);
```

#### Return Value

The status dictionary, or `NULL` if an error occurred (use the [`SCError()`](./scerror%28%29.md) function to retrieve the specific error).

#### Discussion

An extended status dictionary contains specific dictionaries describing the status for each subcomponent of the service. For example, a status dictionary contains the following sub-dictionaries, keys, and values:

| Sub-dictionary | Key | Value |
| --- | --- | --- |
| IPv4 | `Addresses` | The assigned IP address |
| PPP | `Status` | The PPP-specific status (see [`SCNetworkConnectionPPPStatus`](./scnetworkconnectionpppstatus.md) for possible values) |
|  | `LastCause` | Available when the status is “Disconnected” and contains the last error associated with connecting or disconnecting. |
|  | `ConnectTime` | The time when the connection was established. |
| Modem | `ConnectSpeed` | The speed of the modem connection in bits per second. |

Other dictionaries can be present for PPoE, PPTP, and L2TP.

The status dictionary may be extended in the future to contain additional information.

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
- [func SCNetworkConnectionCopyStatistics(SCNetworkConnection) -> CFDictionary?](./scnetworkconnectioncopystatistics%28_%29.md)
  Returns the statistics of the specified connection.
- [func SCNetworkConnectionCopyUserOptions(SCNetworkConnection) -> CFDictionary?](./scnetworkconnectioncopyuseroptions%28_%29.md)
  Gets the user options used to start the specified connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncopyextendedstatus(_:))*