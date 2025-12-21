# addObserver(_:selector:name:object:)

**Framework**: Foundation  
**Kind**: method

Adds an entry to the notification center to call the provided selector with the notification.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addObserver(_ observer: Any, selector aSelector: Selector, name aName: NSNotification.Name?, object anObject: Any?)
```

#### Discussion

Unregister an observer to stop receiving notifications.

To unregister an observer, use `NotificationCenter/removeObserver(_:)` or [`removeObserver(_:name:object:)`](notificationcenter/removeobserver(_:name:object:).md) with the most specific detail possible. For example, if you used a name and object to register the observer, use the name and object to remove it.

If your app targets iOS 9.0 and later or macOS 10.11 and later, you do not need to unregister an observer that you created with this function. If you forget or are unable to remove an observer, the system cleans up the next time it would have posted to it.

## Parameters

- `observer`: An object to register as an observer.
- `aSelector`: A selector that specifies the message the receiver sends   to alert it to the notification posting. The method that   specifies must have one and only one argument (an instance of  ).
- `aName`: When  , the sender doesn’t use notification names as criteria for the delivery.
- `anObject`: When  , the notification center doesn’t use sender names as criteria for delivery.

## See Also

- [func addObserver(forName: NSNotification.Name?, object: Any?, queue: OperationQueue?, using: (Notification) -> Void) -> any NSObjectProtocol](notificationcenter/addobserver(forname:object:queue:using:).md)
  Adds an entry to the notification center to receive notifications that passed to the provided block.
- [func removeObserver(Any, name: NSNotification.Name?, object: Any?)](notificationcenter/removeobserver(_:name:object:).md)
  Removes matching entries from the notification center’s dispatch table.
- [func removeObserver(Any)](notificationcenter/removeobserver(_:)-2yciv.md)
  Removes all entries specifying an observer from the notification center’s dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/addobserver(_:selector:name:object:))*