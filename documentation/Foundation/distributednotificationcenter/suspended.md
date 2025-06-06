# suspended

**Framework**: Foundation  
**Kind**: property

Suspends or resumes notification delivery.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var suspended: Bool { get set }
```

#### Discussion

See [`DistributedNotificationCenter.SuspensionBehavior`](distributednotificationcenter/suspensionbehavior.md) for details on how the receiver delivers notifications to their observers when normal notification delivery is suspended.

The [`NSApplication`](https://developer.apple.com/documentation/AppKit/NSApplication) class automatically suspends distributed notification delivery when the application is not active. Applications based on the Application Kit framework should let AppKit manage the suspension of notification delivery. Foundation-only programs may have occasional need to use this method.

## Parameters

- `suspended`:   suspends notification delivery,   resumes it.

## See Also

- [func addObserver(Any, selector: Selector, name: NSNotification.Name?, object: String?, suspensionBehavior: DistributedNotificationCenter.SuspensionBehavior)](distributednotificationcenter/addobserver(_:selector:name:object:suspensionbehavior:).md)
  Adds an entry to the receiver’s dispatch table with a specific observer and suspended-notifications behavior, and optional notification name and sender.
- [func postNotificationName(NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?, deliverImmediately: Bool)](distributednotificationcenter/postnotificationname(_:object:userinfo:deliverimmediately:).md)
  Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/suspended)*