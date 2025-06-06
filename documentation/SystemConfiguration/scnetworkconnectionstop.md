# SCNetworkConnectionStop(_:_:)

**Framework**: System Configuration  
**Kind**: func

Stops the connection process for the specified network connection.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionStop(_ connection: SCNetworkConnection, _ forceDisconnect: Bool) -> Bool
```

#### Return Value

`TRUE` if the disconnection request succeeded; `FALSE` (use the [`SCError()`](scerror().md) function to retrieve the specific error).

## Parameters

- `connection`: The network connection to stop.
- `forceDisconnect`: Pass   to stop the connection regardless of other applications that might have interest in it.

## See Also

- [func SCNetworkConnectionStart(SCNetworkConnection, CFDictionary?, Bool) -> Bool](scnetworkconnectionstart(_:_:_:).md)
  Starts the connection process for the specified network connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstop(_:_:))*