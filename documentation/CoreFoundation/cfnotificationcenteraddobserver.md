# CFNotificationCenterAddObserver(_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Registers an observer to receive notifications.

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
func CFNotificationCenterAddObserver(_ center: CFNotificationCenter!, _ observer: UnsafeRawPointer!, _ callBack: CFNotificationCallback!, _ name: CFString!, _ object: UnsafeRawPointer!, _ suspensionBehavior: CFNotificationSuspensionBehavior)
```

#### Discussion

Notification delivery is registered for the main thread.

If you need to control which thread processes a notification, your callback function must be able to forward the notification to the proper thread. You can use a `CFMessagePort` object or a custom `CFRunLoopSource` object to send notifications to the correct thread’s run loop.

## Parameters

- `center`: The notification center to which to add the observer.
- `observer`: The observer. In macOS 10.3 and later, this parameter may be  .
- `callBack`: The callback function to call when   posts the notification named  .
- `name`: If   is a Darwin notification center, this value must   be  .
- `object`: If   is a Darwin notification center, this value is ignored.
- `suspensionBehavior`: If   is a Darwin notification center, this value is ignored.

## See Also

- [class CFRunLoopSource](cfrunloopsource.md)
- [class CFMessagePort](cfmessageport.md)
- [func CFNotificationCenterRemoveEveryObserver(CFNotificationCenter!, UnsafeRawPointer!)](cfnotificationcenterremoveeveryobserver(_:_:).md)
  Stops an observer from receiving any notifications from any object.
- [func CFNotificationCenterRemoveObserver(CFNotificationCenter!, UnsafeRawPointer!, CFNotificationName!, UnsafeRawPointer!)](cfnotificationcenterremoveobserver(_:_:_:_:).md)
  Stops an observer from receiving certain notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationcenteraddobserver(_:_:_:_:_:_:))*