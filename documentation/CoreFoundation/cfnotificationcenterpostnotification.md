# CFNotificationCenterPostNotification(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Posts a notification for an object.

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
func CFNotificationCenterPostNotification(_ center: CFNotificationCenter!, _ name: CFNotificationName!, _ object: UnsafeRawPointer!, _ userInfo: CFDictionary!, _ deliverImmediately: Bool)
```

## Parameters

- `center`: The notification center to post the notification.
- `name`: The name of the notification to post. This value must not be  .
- `object`: If   is a Darwin notification center, this value is ignored.
- `userInfo`: If   is a Darwin notification center, this value is ignored.
- `deliverImmediately`: If   is a Darwin notification center, this value is ignored.

## See Also

- [func CFNotificationCenterPostNotificationWithOptions(CFNotificationCenter!, CFNotificationName!, UnsafeRawPointer!, CFDictionary!, CFOptionFlags)](cfnotificationcenterpostnotificationwithoptions(_:_:_:_:_:).md)
  Posts a notification for an object using specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationcenterpostnotification(_:_:_:_:_:))*