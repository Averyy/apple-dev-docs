# undoActionUserInfoValue(forKey:)

**Framework**: Foundation  
**Kind**: method

Retrieves the undo action’s user info value for the given key.

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
func undoActionUserInfoValue(forKey key: UndoManager.UserInfoKey) -> Any?
```

#### Return Value

The value that you previously registered to this key with [`setActionUserInfoValue(_:forKey:)`](undomanager/setactionuserinfovalue(_:forkey:).md), or `nil` if the key is absent.

#### Discussion

Use this method to retrieve a user info value for the undo action you previously set with [`setActionUserInfoValue(_:forKey:)`](undomanager/setactionuserinfovalue(_:forkey:).md).

In this example, an app’s `undoButton()` method provides a SwiftUI view that incorporates a previously assigned icon for the undo action:

```swift
func undoButton() -> some SwiftUI.View {
    Button(action: {
        self.undoManager.undo()
    }) {
        Label(self.undoManager.undoActionName,
              image: self.undoManager.undoActionUserInfoValue(forKey: .icon) as? Image)
    }
}
```

## Parameters

- `key`: The key associated with the value to return.

## See Also

- [func setActionUserInfoValue(Any?, forKey: UndoManager.UserInfoKey)](undomanager/setactionuserinfovalue(_:forkey:).md)
  Sets a user info value for an undo or redo action.
- [func redoActionUserInfoValue(forKey: UndoManager.UserInfoKey) -> Any?](undomanager/redoactionuserinfovalue(forkey:).md)
  Retrieves the redo action’s user info value for the given key.
- [UndoManager.UserInfoKey](undomanager/userinfokey.md)
  An extensible namespace for undo and redo user info keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/undoactionuserinfovalue(forkey:))*