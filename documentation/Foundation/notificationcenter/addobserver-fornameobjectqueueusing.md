# addObserver(forName:object:queue:using:)

**Framework**: Foundation  
**Kind**: method

Adds an entry to the notification center to receive notifications that passed to the provided block.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addObserver(forName name: NSNotification.Name?, object obj: Any?, queue: OperationQueue?, using block: @escaping (Notification) -> Void) -> any NSObjectProtocol
```

#### Return Value

An opaque object to act as the observer. Notification center strongly holds this return value until you remove the observer registration.

#### Discussion

If a notification triggers more than one observer block, the blocks can all execute concurrently (but on their queue or on the current thread).

The following example shows how you can register to receive locale change notifications. It stores the return value from [`addObserver(forName:object:queue:using:)`](notificationcenter/addobserver(forname:object:queue:using:).md) in an instance property called `localeChangeObserver`.

Unregister an observer to stop receiving notifications. To unregister an observer, use [`removeObserver(_:)`](notificationcenter/removeobserver(_:).md) or [`removeObserver(_:name:object:)`](notificationcenter/removeobserver(_:name:object:).md) with the most specific detail possible. For example, if you used a name and object to register the observer, use the name and object to remove it.

You must invoke [`removeObserver(_:)`](notificationcenter/removeobserver(_:).md) or [`removeObserver(_:name:object:)`](notificationcenter/removeobserver(_:name:object:).md) before the system deallocates any object that [`addObserver(forName:object:queue:using:)`](notificationcenter/addobserver(forname:object:queue:using:).md) specifies.

Another common practice is to create a one-time notification by removing the observer from within the observation block, as in the following example.

This example stores the opaque observer object in an instance property called `token`, which you can use to remove the observer prior to receiving the notification.

> 💡 **Tip**:  To avoid a retain cycle, use a weak reference to `self` inside the block when `self` contains the observer as a strong reference.

 To avoid a retain cycle, use a weak reference to `self` inside the block when `self` contains the observer as a strong reference.

## Parameters

- `name`: When  , the sender doesn’t use notification names as criteria for delivery.
- `obj`: When  , the notification center doesn’t use the sender as criteria for the delivery.
- `queue`: When  , the block runs synchronously on the posting thread.
- `block`: The block takes one argument: the notification.

## See Also

- [func addObserver(Any, selector: Selector, name: NSNotification.Name?, object: Any?)](notificationcenter/addobserver(_:selector:name:object:).md)
  Adds an entry to the notification center to call the provided selector with the notification.
- [func removeObserver(Any, name: NSNotification.Name?, object: Any?)](notificationcenter/removeobserver(_:name:object:).md)
  Removes matching entries from the notification center’s dispatch table.
- [func removeObserver(Any)](notificationcenter/removeobserver(_:).md)
  Removes all entries specifying an observer from the notification center’s dispatch table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/addobserver(forname:object:queue:using:))*