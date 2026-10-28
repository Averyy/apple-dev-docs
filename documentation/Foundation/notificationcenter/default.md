# default

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The app’s default notification center.

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
class var `default`: NotificationCenter { get }
```

```objc
@property (class, strong, readonly) NSNotificationCenter * defaultCenter;
```

## Discussion

All system notifications sent to an app are posted to the [`default`](./default.md) notification center. You can also post your own notifications there.

If your app uses notifications extensively, you may want to create and post to your own notification centers rather than posting only to the [`default`](./default.md) notification center. When a notification is posted to a notification center, the notification center scans through the list of registered observers, which may slow down your app. By organizing notifications functionally around one or more notification centers, less work is done each time a notification is posted, which can improve performance throughout your app.

## See Also

### Related Documentation
- [Notification Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/default)*