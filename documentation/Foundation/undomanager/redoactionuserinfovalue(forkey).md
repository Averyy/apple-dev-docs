# redoActionUserInfoValue(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Retrieves the redo action’s user info value for the given key.

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
func redoActionUserInfoValue(forKey key: UndoManager.UserInfoKey) -> Any?
```

```objc
- (id) redoActionUserInfoValueForKey:(NSUndoManagerUserInfoKey) key;
```

## Return Value

The value that you previously registered to this key with [`setActionUserInfoValue(_:forKey:)`](./setactionuserinfovalue%28_,forkey%29.md), or `nil` if the key is absent.

## Discussion

Use this method to retrieve a user info value for the redo action you previously set with [`setActionUserInfoValue(_:forKey:)`](./setactionuserinfovalue%28_,forkey%29.md).

In this example, an app’s `redoButton()` method provides a SwiftUI view that incorporates a previously assigned icon for the action:

```swift
func redoButton() -> some SwiftUI.View {
    Button(action: {
        self.undoManager.redo()
    }) {
        Label(self.undoManager.redoActionName,
              image: self.undoManager.redoActionUserInfoValue(forKey: .icon) as? Image)
    }
}
```

## Parameters

- `key`: The key associated with the value to return.

## See Also

### Working with user info
- [func setActionUserInfoValue(Any?, forKey: UndoManager.UserInfoKey)](./setactionuserinfovalue%28_,forkey%29.md)
  Sets a user info value for an undo or redo action.
- [func undoActionUserInfoValue(forKey: UndoManager.UserInfoKey) -> Any?](./undoactionuserinfovalue%28forkey%29.md)
  Retrieves the undo action’s user info value for the given key.
- [UndoManager.UserInfoKey](./userinfokey.md)
  An extensible namespace for undo and redo user info keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/redoactionuserinfovalue(forkey:))*