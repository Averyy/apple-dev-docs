# SCNetworkReachabilityScheduleWithRunLoop(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Schedules the specified network target with the specified run loop and mode.

**Availability**:
- iOS 2.0+ - Deprecated in 17.4
- iPadOS 2.0+ - Deprecated in 17.4
- Mac Catalyst 13.1+ - Deprecated in 17.4
- macOS 10.3+ - Deprecated in 14.4
- tvOS - Deprecated in 17.4
- visionOS 1.0+ - Deprecated in 1.1

## Declaration

```swift
func SCNetworkReachabilityScheduleWithRunLoop(_ target: SCNetworkReachability, _ runLoop: CFRunLoop, _ runLoopMode: CFString) -> Bool
```

```c
Boolean SCNetworkReachabilityScheduleWithRunLoop(SCNetworkReachabilityRef target, CFRunLoopRef runLoop, CFStringRef runLoopMode);
```

#### Return Value

`TRUE` if the target is scheduled successfully; otherwise,  `FALSE`.

## Parameters

- `target`: The address or name that is set up for asynchronous notifications. Must not be `NULL`.
- `runLoop`: The run loop on which the target should be scheduled. Must not be `NULL`.
- `runLoopMode`: The mode in which to schedule the target. Must not be `NULL`.

## See Also

### Preparing to Determine Reachability
- [func SCNetworkReachabilityGetTypeID() -> CFTypeID](./scnetworkreachabilitygettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkReachability` instances.
- [func SCNetworkReachabilitySetCallback(SCNetworkReachability, SCNetworkReachabilityCallBack?, UnsafeMutablePointer<SCNetworkReachabilityContext>?) -> Bool](./scnetworkreachabilitysetcallback%28_,_,_%29.md)
  Assigns a client to the specified target, which receives callbacks when the reachability of the target changes.
- [func SCNetworkReachabilityUnscheduleFromRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](./scnetworkreachabilityunschedulefromrunloop%28_,_,_%29.md)
  Unschedules the specified target from the specified run loop and mode.
- [func SCNetworkReachabilitySetDispatchQueue(SCNetworkReachability, dispatch_queue_t?) -> Bool](./scnetworkreachabilitysetdispatchqueue%28_,_%29.md)
  Schedules callbacks for the specified target on the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityschedulewithrunloop(_:_:_:))*