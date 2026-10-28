# SCNetworkReachabilitySetDispatchQueue(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Schedules callbacks for the specified target on the specified dispatch queue.

**Availability**:
- iOS 4.0+ - Deprecated in 17.4
- iPadOS 4.0+ - Deprecated in 17.4
- Mac Catalyst 13.1+ - Deprecated in 17.4
- macOS 10.6+ - Deprecated in 14.4
- tvOS - Deprecated in 17.4
- visionOS 1.0+ - Deprecated in 1.1

## Declaration

```swift
func SCNetworkReachabilitySetDispatchQueue(_ target: SCNetworkReachability, _ queue: dispatch_queue_t?) -> Bool
```

```c
Boolean SCNetworkReachabilitySetDispatchQueue(SCNetworkReachabilityRef target, dispatch_queue_t queue);
```

## Return Value

`TRUE` if the target is scheduled successfully; otherwise, `FALSE`.

## Parameters

- `target`: The address or name that is set up for asynchronous notifications. Must not be `NULL`.
- `queue`: The libdispatch queue on which the target should run. Pass `NULL` to disable notifications and release the queue.

## See Also

### Preparing to Determine Reachability
- [func SCNetworkReachabilityGetTypeID() -> CFTypeID](./scnetworkreachabilitygettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkReachability` instances.
- [func SCNetworkReachabilitySetCallback(SCNetworkReachability, SCNetworkReachabilityCallBack?, UnsafeMutablePointer<SCNetworkReachabilityContext>?) -> Bool](./scnetworkreachabilitysetcallback%28_,_,_%29.md)
  Assigns a client to the specified target, which receives callbacks when the reachability of the target changes.
- [func SCNetworkReachabilityScheduleWithRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](./scnetworkreachabilityschedulewithrunloop%28_,_,_%29.md)
  Schedules the specified network target with the specified run loop and mode.
- [func SCNetworkReachabilityUnscheduleFromRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](./scnetworkreachabilityunschedulefromrunloop%28_,_,_%29.md)
  Unschedules the specified target from the specified run loop and mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitysetdispatchqueue(_:_:))*