# CFNotificationCenterRemoveEveryObserver(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Stops an observer from receiving any notifications from any object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFNotificationCenterRemoveEveryObserver(_ center: CFNotificationCenter!, _ observer: UnsafeRawPointer!)
```

```c
extern void CFNotificationCenterRemoveEveryObserver(CFNotificationCenterRef center, const void *observer);
```

## Discussion

If you no longer want an observer to receive any notifications, perhaps because the observer is being deallocated, you can call this function to unregister the observer from all the notifications for which it had previously registered.

## Parameters

- `center`: The notification center from which to remove observers.
- `observer`: The observer. This value must not be `NULL`.

## See Also

### Adding and Removing Observers
- [func CFNotificationCenterAddObserver(CFNotificationCenter!, UnsafeRawPointer!, CFNotificationCallback!, CFString!, UnsafeRawPointer!, CFNotificationSuspensionBehavior)](./cfnotificationcenteraddobserver%28_,_,_,_,_,_%29.md)
  Registers an observer to receive notifications.
- [func CFNotificationCenterRemoveObserver(CFNotificationCenter!, UnsafeRawPointer!, CFNotificationName!, UnsafeRawPointer!)](./cfnotificationcenterremoveobserver%28_,_,_,_%29.md)
  Stops an observer from receiving certain notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationcenterremoveeveryobserver(_:_:))*