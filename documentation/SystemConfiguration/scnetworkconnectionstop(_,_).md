# SCNetworkConnectionStop(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Stops the connection process for the specified network connection.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionStop(_ connection: SCNetworkConnection, _ forceDisconnect: Bool) -> Bool
```

```c
Boolean SCNetworkConnectionStop(SCNetworkConnectionRef connection, Boolean forceDisconnect);
```

## Return Value

`TRUE` if the disconnection request succeeded; `FALSE` (use the [`SCError()`](./scerror%28%29.md) function to retrieve the specific error).

## Parameters

- `connection`: The network connection to stop.
- `forceDisconnect`: Pass `TRUE` to stop the connection regardless of other applications that might have interest in it.

## See Also

### Starting and Stopping a Connection
- [func SCNetworkConnectionStart(SCNetworkConnection, CFDictionary?, Bool) -> Bool](./scnetworkconnectionstart%28_,_,_%29.md)
  Starts the connection process for the specified network connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstop(_:_:))*