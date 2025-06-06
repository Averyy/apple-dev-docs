# SCNetworkReachabilitySetDispatchQueue(_:_:)

**Framework**: System Configuration  
**Kind**: func

Schedules callbacks for the specified target on the specified dispatch queue.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func SCNetworkReachabilitySetDispatchQueue(_ target: SCNetworkReachability, _ queue: dispatch_queue_t?) -> Bool
```

#### Return Value

`TRUE` if the target is scheduled successfully; otherwise, `FALSE`.

## Parameters

- `target`: The address or name that is set up for asynchronous notifications. Must not be  .
- `queue`: The libdispatch queue on which the target should run. Pass   to disable notifications and release the queue.

## See Also

- [func SCNetworkReachabilityGetTypeID() -> CFTypeID](scnetworkreachabilitygettypeid().md)
  Returns the type identifier of all `SCNetworkReachability` instances.
- [func SCNetworkReachabilitySetCallback(SCNetworkReachability, SCNetworkReachabilityCallBack?, UnsafeMutablePointer<SCNetworkReachabilityContext>?) -> Bool](scnetworkreachabilitysetcallback(_:_:_:).md)
  Assigns a client to the specified target, which receives callbacks when the reachability of the target changes.
- [func SCNetworkReachabilityScheduleWithRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](scnetworkreachabilityschedulewithrunloop(_:_:_:).md)
  Schedules the specified network target with the specified run loop and mode.
- [func SCNetworkReachabilityUnscheduleFromRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](scnetworkreachabilityunschedulefromrunloop(_:_:_:).md)
  Unschedules the specified target from the specified run loop and mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitysetdispatchqueue(_:_:))*