# presentFriendRequestCreator(from:)

**Framework**: GameKit  
**Kind**: method

Opens the Messages app with a sheet for the player to request friends.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func presentFriendRequestCreator(from window: NSWindow?) throws
```

#### Discussion

If this method throws an exception, it doesn’t open the Messages app.

## Parameters

- `window`: The window that’s the anchor for opening the Messages app.

## See Also

- [var isPresentingFriendRequestViewController: Bool](gklocalplayer/ispresentingfriendrequestviewcontroller.md)
  A Boolean value that indicates whether your game presents the friends request view controller.
- [func presentFriendRequestCreator(from: UIViewController) throws](gklocalplayer/presentfriendrequestcreator(from:)-7j1kn.md)
  Presents a view controller with a Messages sheet for the player to request friends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/presentfriendrequestcreator(from:)-7clh6)*