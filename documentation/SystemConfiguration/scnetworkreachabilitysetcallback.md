# SCNetworkReachabilitySetCallback(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Assigns a client to the specified target, which receives callbacks when the reachability of the target changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func SCNetworkReachabilitySetCallback(_ target: SCNetworkReachability, _ callout: SCNetworkReachabilityCallBack?, _ context: UnsafeMutablePointer<SCNetworkReachabilityContext>?) -> Bool
```

#### Return Value

`TRUE` if the notification client was successfully set; otherwise, `FALSE`.

## Parameters

- `target`: The network reference associated with the address or name to be checked for reachability.
- `callout`: The function to be called when the reachability of the target changes. If  , the current client for the target is removed.
- `context`: The reachability context associated with the callout. This value may be  .

## See Also

- [func SCNetworkReachabilityGetTypeID() -> CFTypeID](scnetworkreachabilitygettypeid().md)
  Returns the type identifier of all `SCNetworkReachability` instances.
- [func SCNetworkReachabilityScheduleWithRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](scnetworkreachabilityschedulewithrunloop(_:_:_:).md)
  Schedules the specified network target with the specified run loop and mode.
- [func SCNetworkReachabilityUnscheduleFromRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](scnetworkreachabilityunschedulefromrunloop(_:_:_:).md)
  Unschedules the specified target from the specified run loop and mode.
- [func SCNetworkReachabilitySetDispatchQueue(SCNetworkReachability, dispatch_queue_t?) -> Bool](scnetworkreachabilitysetdispatchqueue(_:_:).md)
  Schedules callbacks for the specified target on the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitysetcallback(_:_:_:))*