# UndoManager.UserInfoKey

**Framework**: Foundation  
**Kind**: struct

An extensible namespace for undo and redo user info keys.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct UserInfoKey
```

#### Discussion

Extend this type with the names of user info keys you want to associate with undo actions, like this:

```swift
extension UndoManager.UserInfoKey {
    static let icon: UndoManager.UserInfoKey = "icon"
}
```

You then use this key when you set and get undo user info values.

```swift
self.undoManager.setActionUserInfoValue(Image(named: "new_layer"), forKey: .icon)

```

## Topics

### Creating a user info key from a raw value
- [init(String)](undomanager/userinfokey/init(_:).md)
  Creates a user info key from the given string.
- [init(rawValue: String)](undomanager/userinfokey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setActionUserInfoValue(Any?, forKey: UndoManager.UserInfoKey)](undomanager/setactionuserinfovalue(_:forkey:).md)
  Sets a user info value for an undo or redo action.
- [func undoActionUserInfoValue(forKey: UndoManager.UserInfoKey) -> Any?](undomanager/undoactionuserinfovalue(forkey:).md)
  Retrieves the undo action’s user info value for the given key.
- [func redoActionUserInfoValue(forKey: UndoManager.UserInfoKey) -> Any?](undomanager/redoactionuserinfovalue(forkey:).md)
  Retrieves the redo action’s user info value for the given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/userinfokey)*