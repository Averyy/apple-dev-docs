# ModelContext.NotificationKey.historyTokens

**Framework**: SwiftData  
**Kind**: case

A history token representing the persistent store state after the save.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Swift 5.9+

## Declaration

```swift
case historyTokens
```

#### Discussion

This key is available in `ModelContext.didSave` notifications (it is not present in `willSave` notifications). The value is an instance conforming to `HistoryToken`.

Use this token with `HistoryDescriptor` to fetch only changes that occurred after this save operation:

```swift
NotificationCenter.default.addObserver(
    forName: ModelContext.didSave,
    object: nil,
    queue: nil
) { notification in
    guard let token = notification.userInfo?[ModelContext.NotificationKey.historyToken] as? DefaultHistoryToken else {
        return
    }

    // Use token to fetch changes since this save
    let descriptor = HistoryDescriptor<DefaultHistoryTransaction>(
        predicate: #Predicate { $0.token > token }
    )
}
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontext/notificationkey/historytokens)*