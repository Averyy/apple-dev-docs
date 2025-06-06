# CFNotificationCenter

**Framework**: Core Foundation  
**Kind**: class

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
class CFNotificationCenter
```

#### Overview

A CFNotificationCenter object provides the means by which you can send a message, or notification, to any number of recipients, or observers, without having to know anything about the recipients. A notification message consists of a notification name (a CFString), a pointer value that identifies the object posting the notification, and an optional dictionary that contains additional information about the particular notification.

To register as an observer of a notification, you call [`CFNotificationCenterAddObserver(_:_:_:_:_:_:)`](cfnotificationcenteraddobserver(_:_:_:_:_:_:).md), providing an identifier for your observer, the callback function that should be called when the notification is posted, and the name of the notification and the object in which you are interested. The observer identifier is passed back to the callback function, along with the notification information. You can use the identifier to distinguish multiple observers using the same callback function. The identifier is also used to unregister the observer with [`CFNotificationCenterRemoveObserver(_:_:_:_:)`](cfnotificationcenterremoveobserver(_:_:_:_:).md) and [`CFNotificationCenterRemoveEveryObserver(_:_:)`](cfnotificationcenterremoveeveryobserver(_:_:).md).

To send a notification, you call [`CFNotificationCenterPostNotification(_:_:_:_:_:)`](cfnotificationcenterpostnotification(_:_:_:_:_:).md), passing in the notification information. The notification center then looks up all the observers that registered for this notification and sends the notification information to their callback functions.

There are three types of CFNotificationCenter—a distributed notification center, a local notification center, and a Darwin notification center—an application may have at most one of each type. The distributed notification is obtained with [`CFNotificationCenterGetDistributedCenter()`](cfnotificationcentergetdistributedcenter().md). A distributed notification center delivers notifications between applications. In this case, the notification object must always be a CFString object and the notification dictionary must contain only property list values. The local and Darwin notification centers are available in macOS 10.4 and later, and obtained using [`CFNotificationCenterGetLocalCenter()`](cfnotificationcentergetlocalcenter().md) and [`CFNotificationCenterGetDarwinNotifyCenter()`](cfnotificationcentergetdarwinnotifycenter().md) respectively.

Unlike some other Core Foundation opaque types with names similar to a Cocoa Foundation class (such as CFString and `NSString`), CFNotificationCenter objects cannot be cast (“toll-free bridged”) to [`NotificationCenter`](https://developer.apple.com/documentation/Foundation/NotificationCenter) objects or vice-versa.

## Topics

### Accessing a Notification Center
- [func CFNotificationCenterGetDarwinNotifyCenter() -> CFNotificationCenter!](cfnotificationcentergetdarwinnotifycenter().md)
  Returns the application’s Darwin notification center.
- [func CFNotificationCenterGetDistributedCenter() -> CFNotificationCenter!](cfnotificationcentergetdistributedcenter().md)
  Returns the application’s distributed notification center.
- [func CFNotificationCenterGetLocalCenter() -> CFNotificationCenter!](cfnotificationcentergetlocalcenter().md)
  Returns the application’s local notification center.
### Posting a Notification
- [func CFNotificationCenterPostNotification(CFNotificationCenter!, CFNotificationName!, UnsafeRawPointer!, CFDictionary!, Bool)](cfnotificationcenterpostnotification(_:_:_:_:_:).md)
  Posts a notification for an object.
- [func CFNotificationCenterPostNotificationWithOptions(CFNotificationCenter!, CFNotificationName!, UnsafeRawPointer!, CFDictionary!, CFOptionFlags)](cfnotificationcenterpostnotificationwithoptions(_:_:_:_:_:).md)
  Posts a notification for an object using specified options.
### Adding and Removing Observers
- [func CFNotificationCenterAddObserver(CFNotificationCenter!, UnsafeRawPointer!, CFNotificationCallback!, CFString!, UnsafeRawPointer!, CFNotificationSuspensionBehavior)](cfnotificationcenteraddobserver(_:_:_:_:_:_:).md)
  Registers an observer to receive notifications.
- [func CFNotificationCenterRemoveEveryObserver(CFNotificationCenter!, UnsafeRawPointer!)](cfnotificationcenterremoveeveryobserver(_:_:).md)
  Stops an observer from receiving any notifications from any object.
- [func CFNotificationCenterRemoveObserver(CFNotificationCenter!, UnsafeRawPointer!, CFNotificationName!, UnsafeRawPointer!)](cfnotificationcenterremoveobserver(_:_:_:_:).md)
  Stops an observer from receiving certain notifications.
### Getting the CFNotificationCenter Type ID
- [func CFNotificationCenterGetTypeID() -> CFTypeID](cfnotificationcentergettypeid().md)
  Returns the type identifier for the CFNotificationCenter opaque type.
### Callbacks
- [typealias CFNotificationCallback](cfnotificationcallback.md)
  Callback function invoked for each observer of a notification when the notification is posted.
### Constants
- [enum CFNotificationSuspensionBehavior](cfnotificationsuspensionbehavior.md)
  Suspension flags that indicate how distributed notifications should be handled when the receiving application is in the background.
- [Notification Posting Options](1569610-notification-posting-options.md)
  Possible options when posting notifications.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Notification Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html#//apple_ref/doc/uid/10000043i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationcenter)*