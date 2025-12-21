# ModelContext.NotificationKey

**Framework**: SwiftData  
**Kind**: enum

Describes the data in the user info dictionary of a notification sent by a model context.

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
enum NotificationKey
```

## Topics

### Accessing notification keys
- [ModelContext.NotificationKey.deletedIdentifiers](modelcontext/notificationkey/deletedidentifiers.md)
  A set of values identifying the context’s deleted models.
- [ModelContext.NotificationKey.insertedIdentifiers](modelcontext/notificationkey/insertedidentifiers.md)
  A set of values identifying the context’s inserted models.
- [ModelContext.NotificationKey.invalidatedAllIdentifiers](modelcontext/notificationkey/invalidatedallidentifiers.md)
  A set of values identifying the context’s invalidated models.
- [ModelContext.NotificationKey.updatedIdentifiers](modelcontext/notificationkey/updatedidentifiers.md)
  A set of values identifying the context’s updated models.
- [ModelContext.NotificationKey.queryGeneration](modelcontext/notificationkey/querygeneration.md)
  A token that indicates which generation of the model store SwiftData is using.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [static let willSave: Notification.Name](modelcontext/willsave.md)
  A notification that posts when the context is about to process pending inserts, changes, and deletes.
- [static let didSave: Notification.Name](modelcontext/didsave.md)
  A notification that posts when the context finishes processing pending inserts, changes, and deletes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/notificationkey)*