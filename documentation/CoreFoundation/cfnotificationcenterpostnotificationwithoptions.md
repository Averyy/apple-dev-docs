# CFNotificationCenterPostNotificationWithOptions(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Posts a notification for an object using specified options.

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
func CFNotificationCenterPostNotificationWithOptions(_ center: CFNotificationCenter!, _ name: CFNotificationName!, _ object: UnsafeRawPointer!, _ userInfo: CFDictionary!, _ options: CFOptionFlags)
```

## Parameters

- `center`: The notification center to post the notification.
- `name`: The name of the notification to post. This value must not be  .
- `object`: If   is a Darwin notification center, this value is ignored.
- `userInfo`: A dictionary to pass to observers. You populate this dictionary with additional information describing the notification. For distributed notifications, the dictionary must contain only property list objects. Can be  .   If   is a Darwin notification center, this value is ignored.
- `options`: If   is a Darwin notification center, this value is ignored.

## See Also

- [func CFNotificationCenterPostNotification(CFNotificationCenter!, CFNotificationName!, UnsafeRawPointer!, CFDictionary!, Bool)](cfnotificationcenterpostnotification(_:_:_:_:_:).md)
  Posts a notification for an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationcenterpostnotificationwithoptions(_:_:_:_:_:))*