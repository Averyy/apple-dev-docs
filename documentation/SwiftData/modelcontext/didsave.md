# didSave

**Framework**: SwiftData  
**Kind**: property

A notification that posts when the context finishes processing pending inserts, changes, and deletes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
static let didSave: Notification.Name
```

#### Discussion

The notification’s `userInfo` dictionary contains the persistent identifiers of any inserted, updated, or deleted models. Use the appropriate key to access those identifiers. For more information, see [`ModelContext.NotificationKey`](modelcontext/notificationkey.md).

## See Also

- [static let willSave: Notification.Name](modelcontext/willsave.md)
  A notification that posts when the context is about to process pending inserts, changes, and deletes.
- [ModelContext.NotificationKey](modelcontext/notificationkey.md)
  Describes the data in the user info dictionary of a notification sent by a model context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/didsave)*