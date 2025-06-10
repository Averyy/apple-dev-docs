# name

**Framework**: Foundation  
**Kind**: property

The name of the notification.

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
var name: NSNotification.Name { get }
```

#### Discussion

Typically you use this property to find out what kind of notification you are dealing with when you receive a notification.

##### Special Considerations

Notification names can be any string. To avoid name collisions, you might want to use a prefix that’s specific to your application.

## See Also

- [var object: Any?](nsnotification/object.md)
  The object associated with the notification.
- [var userInfo: [AnyHashable : Any]?](nsnotification/userinfo.md)
  The user information dictionary associated with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.property)*