# addObserver(_:selector:name:object:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds an entry to the notification center’s dispatch table with an observer, a selector, and an optional notification name and sender.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func addObserver(_ observer: Any, selector aSelector: Selector, name aName: NSNotification.Name?, object anObject: String?)
```

```objc
- (void) addObserver:(id) observer selector:(SEL) aSelector name:(NSNotificationName) aName object:(NSString *) anObject;
```

#### Discussion

This method calls [`addObserver(_:selector:name:object:suspensionBehavior:)`](./addobserver%28_,selector,name,object,suspensionbehavior%29.md), passing [`DistributedNotificationCenter.SuspensionBehavior.coalesce`](./suspensionbehavior/coalesce.md) for `suspensionBehavior`.

## Parameters

- `observer`: An object registering as an observer.
- `aSelector`: A selector that the notification center sends `notificationObserver` to notify when posting the notification.
- `aName`: The name of the notification for which to register the observer; that is, only notifications with this name are delivered to the observer. When `nil`, the notification center doesn’t use a notification’s name to decide whether to deliver it to the observer.
- `anObject`: The object whose notifications the observer wants to receive; that is, only notifications sent by this sender are delivered to the observer. When `nil`, the notification center doesn’t use a notification’s sender to decide whether to deliver it to the observer.

## See Also

### Managing Observers
- [func addObserver(Any, selector: Selector, name: NSNotification.Name?, object: String?, suspensionBehavior: DistributedNotificationCenter.SuspensionBehavior)](./addobserver%28_,selector,name,object,suspensionbehavior%29.md)
  Adds an entry to the receiver’s dispatch table with a specific observer and suspended-notifications behavior, and optional notification name and sender.
- [func removeObserver(Any, name: NSNotification.Name?, object: String?)](./removeobserver%28_,name,object%29.md)
  Removes matching entries from the receiver’s dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/distributednotificationcenter/addobserver(_:selector:name:object:))*