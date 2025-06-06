# SCNetworkConnectionSetDispatchQueue(_:_:)

**Framework**: System Configuration  
**Kind**: func

Specifies a dispatch queue to use for the connection’s callback function and enables notifications.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func SCNetworkConnectionSetDispatchQueue(_ connection: SCNetworkConnection, _ queue: dispatch_queue_t?) -> Bool
```

#### Return Value

`TRUE` if successful; otherwise, `FALSE` (use the [`SCError()`](scerror().md) function to retrieve the specific error).

## Parameters

- `connection`: The network connection to notify.
- `queue`: The queue on which to run the connection’s callback function. Pass   to disable notifications and release the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionsetdispatchqueue(_:_:))*