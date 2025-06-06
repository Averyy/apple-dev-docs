# SCNetworkReachabilityScheduleWithRunLoop(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Schedules the specified network target with the specified run loop and mode.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func SCNetworkReachabilityScheduleWithRunLoop(_ target: SCNetworkReachability, _ runLoop: CFRunLoop, _ runLoopMode: CFString) -> Bool
```

#### Return Value

`TRUE` if the target is scheduled successfully; otherwise,  `FALSE`.

## Parameters

- `target`: The address or name that is set up for asynchronous notifications. Must not be  .
- `runLoop`: The run loop on which the target should be scheduled. Must not be  .
- `runLoopMode`: The mode in which to schedule the target. Must not be  .

## See Also

- [func SCNetworkReachabilityGetTypeID() -> CFTypeID](scnetworkreachabilitygettypeid().md)
  Returns the type identifier of all `SCNetworkReachability` instances.
- [func SCNetworkReachabilitySetCallback(SCNetworkReachability, SCNetworkReachabilityCallBack?, UnsafeMutablePointer<SCNetworkReachabilityContext>?) -> Bool](scnetworkreachabilitysetcallback(_:_:_:).md)
  Assigns a client to the specified target, which receives callbacks when the reachability of the target changes.
- [func SCNetworkReachabilityUnscheduleFromRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](scnetworkreachabilityunschedulefromrunloop(_:_:_:).md)
  Unschedules the specified target from the specified run loop and mode.
- [func SCNetworkReachabilitySetDispatchQueue(SCNetworkReachability, dispatch_queue_t?) -> Bool](scnetworkreachabilitysetdispatchqueue(_:_:).md)
  Schedules callbacks for the specified target on the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityschedulewithrunloop(_:_:_:))*