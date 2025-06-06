# CFNotificationCenterRemoveObserver(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Stops an observer from receiving certain notifications.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFNotificationCenterRemoveObserver(_ center: CFNotificationCenter!, _ observer: UnsafeRawPointer!, _ name: CFNotificationName!, _ object: UnsafeRawPointer!)
```

#### Discussion

If both `name` and `object` are `NULL`, this function unregisters `observer` from all the notifications for which it had previously registered with `center`.

## Parameters

- `center`: The notification center to modify.
- `observer`: The observer. This value must not be  .
- `name`: The name of the notification to stop observing. If  ,   stops receiving callbacks for all notifications posted by  .
- `object`: If   is a Darwin notification center, this value is ignored.

## See Also

- [func CFNotificationCenterAddObserver(CFNotificationCenter!, UnsafeRawPointer!, CFNotificationCallback!, CFString!, UnsafeRawPointer!, CFNotificationSuspensionBehavior)](cfnotificationcenteraddobserver(_:_:_:_:_:_:).md)
  Registers an observer to receive notifications.
- [func CFNotificationCenterRemoveEveryObserver(CFNotificationCenter!, UnsafeRawPointer!)](cfnotificationcenterremoveeveryobserver(_:_:).md)
  Stops an observer from receiving any notifications from any object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationcenterremoveobserver(_:_:_:_:))*