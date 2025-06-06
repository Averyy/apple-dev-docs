# init(name:object:userInfo:)

**Framework**: Foundation  
**Kind**: init

Initializes a new notification.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(name: Notification.Name, object: Any? = nil, userInfo: [AnyHashable : Any]? = nil)
```

#### Discussion

The default value for `userInfo` is nil.

## See Also

- [Notification.Name](notification/name-swift.typealias.md)
  An alias for a type used to represent the name of a notification.
- [NSNotification.Name](nsnotification/name-swift.struct.md)
  A structure that defines the name of a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notification/init(name:object:userinfo:))*