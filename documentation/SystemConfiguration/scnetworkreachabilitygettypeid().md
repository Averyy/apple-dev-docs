# SCNetworkReachabilityGetTypeID()

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the type identifier of all `SCNetworkReachability` instances.

**Availability**:
- iOS 2.0+ - Deprecated in 17.4
- iPadOS 2.0+ - Deprecated in 17.4
- Mac Catalyst 13.1+ - Deprecated in 17.4
- macOS 10.3+ - Deprecated in 14.4
- tvOS - Deprecated in 17.4
- visionOS 1.0+ - Deprecated in 1.1

## Declaration

```swift
func SCNetworkReachabilityGetTypeID() -> CFTypeID
```

```c
CFTypeID SCNetworkReachabilityGetTypeID();
```

#### Return Value

The type identifier of all `SCNetworkReachability` instances.

## See Also

### Preparing to Determine Reachability
- [func SCNetworkReachabilitySetCallback(SCNetworkReachability, SCNetworkReachabilityCallBack?, UnsafeMutablePointer<SCNetworkReachabilityContext>?) -> Bool](./scnetworkreachabilitysetcallback%28_,_,_%29.md)
  Assigns a client to the specified target, which receives callbacks when the reachability of the target changes.
- [func SCNetworkReachabilityScheduleWithRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](./scnetworkreachabilityschedulewithrunloop%28_,_,_%29.md)
  Schedules the specified network target with the specified run loop and mode.
- [func SCNetworkReachabilityUnscheduleFromRunLoop(SCNetworkReachability, CFRunLoop, CFString) -> Bool](./scnetworkreachabilityunschedulefromrunloop%28_,_,_%29.md)
  Unschedules the specified target from the specified run loop and mode.
- [func SCNetworkReachabilitySetDispatchQueue(SCNetworkReachability, dispatch_queue_t?) -> Bool](./scnetworkreachabilitysetdispatchqueue%28_,_%29.md)
  Schedules callbacks for the specified target on the specified dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitygettypeid())*