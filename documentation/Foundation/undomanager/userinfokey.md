# UndoManager.UserInfoKey

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * NSUndoManagerUserInfoKey;
```

## Discussion

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
- [init(String)](./userinfokey/init%28_%29.md)
  Creates a user info key from the given string.
- [init(rawValue: String)](./userinfokey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with user info
- [func setActionUserInfoValue(Any?, forKey: UndoManager.UserInfoKey)](./setactionuserinfovalue%28_,forkey%29.md)
  Sets a user info value for an undo or redo action.
- [func undoActionUserInfoValue(forKey: UndoManager.UserInfoKey) -> Any?](./undoactionuserinfovalue%28forkey%29.md)
  Retrieves the undo action’s user info value for the given key.
- [func redoActionUserInfoValue(forKey: UndoManager.UserInfoKey) -> Any?](./redoactionuserinfovalue%28forkey%29.md)
  Retrieves the redo action’s user info value for the given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/userinfokey)*