# suspended

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Suspends or resumes notification delivery.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var suspended: Bool { get set }
```

```objc
@property BOOL suspended;
```

#### Discussion

See [`DistributedNotificationCenter.SuspensionBehavior`](./suspensionbehavior.md) for details on how the receiver delivers notifications to their observers when normal notification delivery is suspended.

The [`NSApplication`](../../AppKit/nsapplication.md) class automatically suspends distributed notification delivery when the application is not active. Applications based on the Application Kit framework should let AppKit manage the suspension of notification delivery. Foundation-only programs may have occasional need to use this method.

## Parameters

- `suspended`: [`true`](../../Swift/true.md) suspends notification delivery, [`false`](../../Swift/false.md) resumes it.

## See Also

### Related Documentation
- [func addObserver(Any, selector: Selector, name: NSNotification.Name?, object: String?, suspensionBehavior: DistributedNotificationCenter.SuspensionBehavior)](./addobserver%28_,selector,name,object,suspensionbehavior%29.md)
  Adds an entry to the receiver’s dispatch table with a specific observer and suspended-notifications behavior, and optional notification name and sender.
- [func postNotificationName(NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?, deliverImmediately: Bool)](./postnotificationname%28_,object,userinfo,deliverimmediately%29.md)
  Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/suspended)*