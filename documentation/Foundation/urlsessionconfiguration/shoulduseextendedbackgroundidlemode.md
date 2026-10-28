# shouldUseExtendedBackgroundIdleMode

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether TCP connections should be kept open when the app moves to the background.

**Availability**:
- iOS 9.0+ - Deprecated in 18.4
- iPadOS 9.0+ - Deprecated in 18.4
- Mac Catalyst 13.1+ - Deprecated in 18.4
- macOS 10.11+ - Deprecated in 15.4
- tvOS 9.0+ - Deprecated in 18.4
- visionOS 1.0+ - Deprecated in 2.4
- watchOS 2.0+ - Deprecated in 11.4

> **Deprecated**: Not supported

## Declaration

```swift
var shouldUseExtendedBackgroundIdleMode: Bool { get set }
```

```objc
@property BOOL shouldUseExtendedBackgroundIdleMode;
```

## Discussion

In addition to requesting that the connection be kept open, setting this value to [`true`](../../Swift/true.md) asks the system to delay reclaiming the connection when the app moves to the background.

## See Also

### Related Documentation
- [Networking and Multitasking](https://developer.apple.com/library/archive/technotes/tn2277/_index.html#//apple_ref/doc/uid/DTS40010841)
### Supporting background transfers
- [var sessionSendsLaunchEvents: Bool](./sessionsendslaunchevents.md)
  A Boolean value that indicates whether the app should be resumed or launched in the background when transfers finish.
- [var isDiscretionary: Bool](./isdiscretionary.md)
  A Boolean value that determines whether background tasks can be scheduled at the discretion of the system for optimal performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/shoulduseextendedbackgroundidlemode)*