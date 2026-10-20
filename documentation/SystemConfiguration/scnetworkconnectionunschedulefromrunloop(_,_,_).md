# SCNetworkConnectionUnscheduleFromRunLoop(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Unschedules the specified connection from the specified run loop.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SCNetworkConnectionUnscheduleFromRunLoop(_ connection: SCNetworkConnection, _ runLoop: CFRunLoop, _ runLoopMode: CFString) -> Bool
```

```c
Boolean SCNetworkConnectionUnscheduleFromRunLoop(SCNetworkConnectionRef connection, CFRunLoopRef runLoop, CFStringRef runLoopMode);
```

#### Return Value

`TRUE` if the connection is unscheduled successfully; `FALSE` (use the [`SCError()`](./scerror%28%29.md) function to retrieve the specific error).

## Parameters

- `connection`: The network connection to unschedule.
- `runLoop`: The run loop from which to unschedule the network connection.
- `runLoopMode`: The run loop mode.

## See Also

### Scheduling a Connection Reference on a Run Loop
- [func SCNetworkConnectionScheduleWithRunLoop(SCNetworkConnection, CFRunLoop, CFString) -> Bool](./scnetworkconnectionschedulewithrunloop%28_,_,_%29.md)
  Schedules the specified connection with the specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionunschedulefromrunloop(_:_:_:))*