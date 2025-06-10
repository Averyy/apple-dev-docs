# setActionUserInfoValue(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Sets a user info value for an undo or redo action.

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
@MainActor
func setActionUserInfoValue(_ info: Any?, forKey key: UndoManager.UserInfoKey)
```

#### Discussion

Set user info on an undo action to provide custom information to the action beyond its action name. You can use this for things like an icon to represent the undoable action, or a timestamp of when the undo manager registers the action.

Start by extending [`UndoManager.UserInfoKey`](undomanager/userinfokey.md) with key names to identify the user info values you want to associate with undo actions.

```swift
extension UndoManager.UserInfoKey {
    static let icon: UndoManager.UserInfoKey = "icon"
}
```

Then set the user info value with this key as part of registering the undoable action. In this example, an app’s `insertLayer()` method provides a custom icon before setting up an undo action that calls the app’s `removeLayer()` method:

```swift
func insertLayer() {
    self.undoManager.setActionName("Insert layer")
    self.undoManager.setActionUserInfoValue(Image(named: "new_layer"), forKey: .icon)

    self.layers.append(Layer())

    self.undoManager.registerUndo(withTarget: self) {
        $0.removeLayer()
    }
}
```

## Parameters

- `info`: The value to save in the action’s user info.
- `key`: The key to associate with the user info value.

## See Also

- [func undoActionUserInfoValue(forKey: UndoManager.UserInfoKey) -> Any?](undomanager/undoactionuserinfovalue(forkey:).md)
  Retrieves the undo action’s user info value for the given key.
- [func redoActionUserInfoValue(forKey: UndoManager.UserInfoKey) -> Any?](undomanager/redoactionuserinfovalue(forkey:).md)
  Retrieves the redo action’s user info value for the given key.
- [UndoManager.UserInfoKey](undomanager/userinfokey.md)
  An extensible namespace for undo and redo user info keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/setactionuserinfovalue(_:forkey:))*