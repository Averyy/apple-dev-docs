# shouldUseExtendedBackgroundIdleMode

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether TCP connections should be kept open when the app moves to the background.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var shouldUseExtendedBackgroundIdleMode: Bool { get set }
```

#### Discussion

In addition to requesting that the connection be kept open, setting this value to [`true`](https://developer.apple.com/documentation/Swift/true) asks the system to delay reclaiming the connection when the app moves to the background.

## See Also

- [Networking and Multitasking](https://developer.apple.comhttps://developer.apple.com/library/archive/technotes/tn2277/_index.html#//apple_ref/doc/uid/DTS40010841)
- [var sessionSendsLaunchEvents: Bool](urlsessionconfiguration/sessionsendslaunchevents.md)
  A Boolean value that indicates whether the app should be resumed or launched in the background when transfers finish.
- [var isDiscretionary: Bool](urlsessionconfiguration/isdiscretionary.md)
  A Boolean value that determines whether background tasks can be scheduled at the discretion of the system for optimal performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/shoulduseextendedbackgroundidlemode)*