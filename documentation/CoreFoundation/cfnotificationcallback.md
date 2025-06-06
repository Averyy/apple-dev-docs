# CFNotificationCallback

**Framework**: Core Foundation  
**Kind**: typealias

Callback function invoked for each observer of a notification when the notification is posted.

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
typealias CFNotificationCallback = (CFNotificationCenter?, UnsafeMutableRawPointer?, CFNotificationName?, UnsafeRawPointer?, CFDictionary?) -> Void
```

## Parameters

- `center`: The notification center handling the notification.
- `observer`: An arbitrary value, other than  , that identifies the observer.
- `name`: The name of the notification being posted.
- `object`: An arbitrary value that identifies the object posting the notification. For distributed notifications,   is always a CFString object. This value could be  .
- `userInfo`: If the notification center is a Darwin notification center, this value must be ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationcallback)*