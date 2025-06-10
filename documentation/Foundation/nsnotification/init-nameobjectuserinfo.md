# init(name:object:userInfo:)

**Framework**: Foundation  
**Kind**: init

Initializes a notification with a specified name, object, and user information.

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
init(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]? = nil)
```

## Parameters

- `name`: The name for the new notification. May not be  .
- `object`: The object for the new notification.
- `userInfo`: The user information dictionary for the new notification. May be  .

## See Also

- [init?(coder: NSCoder)](nsnotification/init(coder:).md)
  Initializes a notification with the data from an unarchiver.
- [convenience init(name: NSNotification.Name, object: Any?)](nsnotification/init(name:object:).md)
  Returns a new notification object with a specified name and object.
- [NSNotification.Name](nsnotification/name-swift.struct.md)
  A structure that defines the name of a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/init(name:object:userinfo:))*