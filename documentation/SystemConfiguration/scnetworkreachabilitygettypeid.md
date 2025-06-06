# SCNetworkReachabilityGetTypeID()

**Framework**: System Configuration  
**Kind**: func

Returns the type identifier of all `SCNetworkReachability` instances.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func SCNetworkReachabilityGetTypeID() -> CFTypeID
```

#### Return Value

The type identifier of all `SCNetworkReachability` instances.

## See Also

- [func SCNetworkReachabilitySetCallback(SCNetworkReachability, SCNetworkReachabilityCallBack?, UnsafeMutablePointer<SCNetworkReachabilityContext>?) -> Bool](scnetworkreachabilitysetcallback(_:_:_:).md)
  Assigns a client to the specified target, which receives callbacks when the reachability of the target changes.
- [func SCNetworkReachabilityScheduleWithRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](scnetworkreachabilityschedulewithrunloop(_:_:_:).md)
  Schedules the specified network target with the specified run loop and mode.
- [func SCNetworkReachabilityUnscheduleFromRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](scnetworkreachabilityunschedulefromrunloop(_:_:_:).md)
  Unschedules the specified target from the specified run loop and mode.
- [func SCNetworkReachabilitySetDispatchQueue(SCNetworkReachability, dispatch_queue_t?) -> Bool](scnetworkreachabilitysetdispatchqueue(_:_:).md)
  Schedules callbacks for the specified target on the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitygettypeid())*