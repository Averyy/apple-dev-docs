# SCNetworkConnectionScheduleWithRunLoop(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Schedules the specified connection with the specified run loop.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionScheduleWithRunLoop(_ connection: SCNetworkConnection, _ runLoop: CFRunLoop, _ runLoopMode: CFString) -> Bool
```

#### Return Value

`TRUE` if the connection is scheduled successfully; `FALSE` (use the [`SCError()`](scerror().md) function to retrieve the specific error).

## Parameters

- `connection`: The network connection to schedule.
- `runLoop`: The run loop with which to schedule the network connection.
- `runLoopMode`: The run loop mode.

## See Also

- [func SCNetworkConnectionUnscheduleFromRunLoop(SCNetworkConnection, CFRunLoop, CFString) -> Bool](scnetworkconnectionunschedulefromrunloop(_:_:_:).md)
  Unschedules the specified connection from the specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionschedulewithrunloop(_:_:_:))*