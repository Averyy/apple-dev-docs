# CFNotificationCenterRemoveObserver(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Stops an observer from receiving certain notifications.

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
func CFNotificationCenterRemoveObserver(_ center: CFNotificationCenter!, _ observer: UnsafeRawPointer!, _ name: CFNotificationName!, _ object: UnsafeRawPointer!)
```

```c
extern void CFNotificationCenterRemoveObserver(CFNotificationCenterRef center, const void *observer, CFNotificationName name, const void *object);
```

#### Discussion

If both `name` and `object` are `NULL`, this function unregisters `observer` from all the notifications for which it had previously registered with `center`.

## Parameters

- `center`: The notification center to modify.
- `observer`: The observer. This value must not be `NULL`.
- `name`: The name of the notification to stop observing. If `NULL`, `observer` stops receiving callbacks for all notifications posted by `object`.
- `object`: The object to stop observing. For distributed notifications, `object` must be a CFString object. If `NULL`, `observer` stops receiving callbacks for all objects posting notifications named `name`.

  If `center` is a Darwin notification center, this value is ignored.

## See Also

### Adding and Removing Observers
- [func CFNotificationCenterAddObserver(CFNotificationCenter!, UnsafeRawPointer!, CFNotificationCallback!, CFString!, UnsafeRawPointer!, CFNotificationSuspensionBehavior)](./cfnotificationcenteraddobserver%28_,_,_,_,_,_%29.md)
  Registers an observer to receive notifications.
- [func CFNotificationCenterRemoveEveryObserver(CFNotificationCenter!, UnsafeRawPointer!)](./cfnotificationcenterremoveeveryobserver%28_,_%29.md)
  Stops an observer from receiving any notifications from any object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationcenterremoveobserver(_:_:_:_:))*