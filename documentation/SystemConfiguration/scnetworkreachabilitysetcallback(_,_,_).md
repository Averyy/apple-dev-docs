# SCNetworkReachabilitySetCallback(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Assigns a client to the specified target, which receives callbacks when the reachability of the target changes.

**Availability**:
- iOS 2.0+ - Deprecated in 17.4
- iPadOS 2.0+ - Deprecated in 17.4
- Mac Catalyst 13.1+ - Deprecated in 17.4
- macOS 10.3+ - Deprecated in 14.4
- tvOS - Deprecated in 17.4
- visionOS 1.0+ - Deprecated in 1.1

## Declaration

```swift
func SCNetworkReachabilitySetCallback(_ target: SCNetworkReachability, _ callout: SCNetworkReachabilityCallBack?, _ context: UnsafeMutablePointer<SCNetworkReachabilityContext>?) -> Bool
```

```c
Boolean SCNetworkReachabilitySetCallback(SCNetworkReachabilityRef target, SCNetworkReachabilityCallBack callout, SCNetworkReachabilityContext *context);
```

## Return Value

`TRUE` if the notification client was successfully set; otherwise, `FALSE`.

## Parameters

- `target`: The network reference associated with the address or name to be checked for reachability.
- `callout`: The function to be called when the reachability of the target changes. If `NULL`, the current client for the target is removed.
- `context`: The reachability context associated with the callout. This value may be `NULL`.

## See Also

### Preparing to Determine Reachability
- [func SCNetworkReachabilityGetTypeID() -> CFTypeID](./scnetworkreachabilitygettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkReachability` instances.
- [func SCNetworkReachabilityScheduleWithRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](./scnetworkreachabilityschedulewithrunloop%28_,_,_%29.md)
  Schedules the specified network target with the specified run loop and mode.
- [func SCNetworkReachabilityUnscheduleFromRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](./scnetworkreachabilityunschedulefromrunloop%28_,_,_%29.md)
  Unschedules the specified target from the specified run loop and mode.
- [func SCNetworkReachabilitySetDispatchQueue(SCNetworkReachability, dispatch_queue_t?) -> Bool](./scnetworkreachabilitysetdispatchqueue%28_,_%29.md)
  Schedules callbacks for the specified target on the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitysetcallback(_:_:_:))*