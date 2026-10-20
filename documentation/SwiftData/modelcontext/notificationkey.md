# ModelContext.NotificationKey

**Framework**: SwiftData  
**Kind**: enum  
**Role**: Enumeration

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
- [ModelContext.NotificationKey.deletedIdentifiers](./notificationkey/deletedidentifiers.md)
  A set of values identifying the context’s deleted models.
- [ModelContext.NotificationKey.insertedIdentifiers](./notificationkey/insertedidentifiers.md)
  A set of values identifying the context’s inserted models.
- [ModelContext.NotificationKey.invalidatedAllIdentifiers](./notificationkey/invalidatedallidentifiers.md)
  A set of values identifying the context’s invalidated models.
- [ModelContext.NotificationKey.updatedIdentifiers](./notificationkey/updatedidentifiers.md)
  A set of values identifying the context’s updated models.
- [ModelContext.NotificationKey.queryGeneration](./notificationkey/querygeneration.md)
  A token that indicates which generation of the model store SwiftData is using.
- [ModelContext.NotificationKey.historyTokens](./notificationkey/historytokens.md)
  A history token representing the persistent store state after the save.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Registering for notifications
- [static let willSave: Notification.Name](./willsave.md)
  A notification that posts when the context is about to process pending inserts, changes, and deletes.
- [static let didSave: Notification.Name](./didsave.md)
  A notification that posts when the context finishes processing pending inserts, changes, and deletes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/notificationkey)*