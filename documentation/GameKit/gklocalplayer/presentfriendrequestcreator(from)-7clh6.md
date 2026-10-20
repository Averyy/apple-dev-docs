# presentFriendRequestCreator(from:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Opens the Messages app with a sheet for the player to request friends.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func presentFriendRequestCreator(from window: NSWindow?) throws
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (BOOL) presentFriendRequestCreatorFromWindow:(UIWindow *) window error:(NSError **) error;
```

*macOS*

```objc
- (BOOL) presentFriendRequestCreatorFromWindow:(NSWindow *) window error:(NSError **) error;
```

#### Discussion

If this method throws an exception, it doesn’t open the Messages app.

## Parameters

- `window`: The window that’s the anchor for opening the Messages app.

## See Also

### Adding Friends
- [var isPresentingFriendRequestViewController: Bool](./ispresentingfriendrequestviewcontroller.md)
  A Boolean value that indicates whether your game presents the friends request view controller.
- [func presentFriendRequestCreator(from: UIViewController) throws](./presentfriendrequestcreator%28from%29-7j1kn.md)
  Presents a view controller with a Messages sheet for the player to request friends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/presentfriendrequestcreator(from:)-7clh6)*