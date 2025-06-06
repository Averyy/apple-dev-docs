# DistributedNotificationCenter

**Framework**: Foundation  
**Kind**: class

A notification dispatch mechanism that enables the broadcast of notifications across task boundaries.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class DistributedNotificationCenter
```

#### Overview

A [`DistributedNotificationCenter`](distributednotificationcenter.md) instance broadcasts [`NSNotification`](nsnotification.md) objects to objects in other tasks that have registered for the notification with their task’s default distributed notification center.

##### Principal Attributes

- Notification dispatch table. See “Class at a Glance” > “Principal Attributes” in [`NotificationCenter`](notificationcenter.md) for information about the dispatch table.

In addition to the notification name and sender, dispatch table entries for distributed notification centers specify when the notification center delivers notifications to its observers. See the [`postNotificationName(_:object:userInfo:deliverImmediately:)`](distributednotificationcenter/postnotificationname(_:object:userinfo:deliverimmediately:).md) method, Suspending and Resuming Notification Delivery, and [`DistributedNotificationCenter.SuspensionBehavior`](distributednotificationcenter/suspensionbehavior.md) for details.

##### Commonly Used Methods

##### Overview

Each task has a default distributed notification center that you access with the [`default()`](distributednotificationcenter/default().md) class method. There may be different types of distributed notification centers. Currently there is a single type—`NSLocalNotificationCenterType`. This type of distributed notification center handles notifications that can be sent between tasks on a single computer. For communication between tasks on different computers, use [`Distributed Objects Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i).

Posting a  is an expensive operation. The notification gets sent to a system-wide server that distributes it to all the tasks that have objects registered for distributed notifications. The latency between posting the notification and the notification’s arrival in another task is unbounded. In fact, when too many notifications are posted and the server’s queue fills up, notifications may be dropped.

Distributed notifications are delivered via a task’s run loop. A task must be running a run loop in one of the “common” modes, such as `NSDefaultRunLoopMode`, to receive a distributed notification. For multithreaded applications running in macOS 10.3 and later, distributed notifications are always delivered to the main thread. For multithreaded applications running in OS X v10.2.8 and earlier, notifications are delivered to the thread that first used the distributed notifications API, which in most cases is the main thread.

> ❗ **Important**:  `NSDistributedNotificationCenter` does not implement a secure communications protocol. When using distributed notifications, your app should treat any data passed in the notification as untrusted. See [`Security Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/Security_Overview/Introduction/Introduction.html#//apple_ref/doc/uid/TP30000976) for general guidance on secure coding practices.

> **Note**:  `NSDistributedNotificationCenter` objects should not be used to send notifications between threads within the same task. Use [`Distributed Objects Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i) or the [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class) method [`performSelector(onMainThread:with:waitUntilDone:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/performSelector(onMainThread:with:waitUntilDone:)), instead. You can also setup an [`Port`](port.md) object to receive and distribute messages from other threads.

## Topics

### Getting Distributed Notification Centers
- [class func `default`() -> DistributedNotificationCenter](distributednotificationcenter/default.md)
  Returns the default distributed notification center, representing the local notification center for the computer.
- [class func forType(DistributedNotificationCenter.CenterType) -> DistributedNotificationCenter](distributednotificationcenter/fortype(_:).md)
  Returns the distributed notification center for a particular notification center type.
### Managing Observers
- [func addObserver(Any, selector: Selector, name: NSNotification.Name?, object: String?)](distributednotificationcenter/addobserver(_:selector:name:object:).md)
  Adds an entry to the notification center’s dispatch table with an observer, a selector, and an optional notification name and sender.
- [func addObserver(Any, selector: Selector, name: NSNotification.Name?, object: String?, suspensionBehavior: DistributedNotificationCenter.SuspensionBehavior)](distributednotificationcenter/addobserver(_:selector:name:object:suspensionbehavior:).md)
  Adds an entry to the receiver’s dispatch table with a specific observer and suspended-notifications behavior, and optional notification name and sender.
- [func removeObserver(Any, name: NSNotification.Name?, object: String?)](distributednotificationcenter/removeobserver(_:name:object:).md)
  Removes matching entries from the receiver’s dispatch table.
### Posting Notifications
- [func post(name: NSNotification.Name, object: String?)](distributednotificationcenter/post(name:object:).md)
  Creates a notification, and posts it to the receiver.
- [func post(name: NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?)](distributednotificationcenter/post(name:object:userinfo:).md)
  Creates a notification with information, and posts it to the receiver.
- [func postNotificationName(NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?, deliverImmediately: Bool)](distributednotificationcenter/postnotificationname(_:object:userinfo:deliverimmediately:).md)
  Creates a notification with information and an immediate-delivery specifier, and posts it to the receiver.
- [func postNotificationName(NSNotification.Name, object: String?, userInfo: [AnyHashable : Any]?, options: DistributedNotificationCenter.Options)](distributednotificationcenter/postnotificationname(_:object:userinfo:options:).md)
  Creates a notification with information, and posts it to the receiver.
### Suspending and Resuming Notification Delivery
- [var suspended: Bool](distributednotificationcenter/suspended.md)
  Suspends or resumes notification delivery.
### Constants
- [DistributedNotificationCenter.Options](distributednotificationcenter/options.md)
  These constants specify the behavior of notifications posted using the [`postNotificationName(_:object:userInfo:options:)`](distributednotificationcenter/postnotificationname(_:object:userinfo:options:).md) method.
- [DistributedNotificationCenter.CenterType](distributednotificationcenter/centertype.md)
  This constant specifies the notification center type.
- [DistributedNotificationCenter.SuspensionBehavior](distributednotificationcenter/suspensionbehavior.md)
  These constants specify the types of notification delivery suspension behaviors.

## Relationships

### Inherits From
- [NotificationCenter](notificationcenter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Foundation/distributednotificationcenter)*