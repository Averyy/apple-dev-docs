# presentFriendRequestCreator(from:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Presents a view controller with a Messages sheet for the player to request friends.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
func presentFriendRequestCreator(from viewController: UIViewController) throws
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (BOOL) presentFriendRequestCreatorFromViewController:(UIViewController *) viewController error:(NSError **) error;
```

*macOS*

```objc
- (BOOL) presentFriendRequestCreatorFromViewController:(NSViewController *) viewController error:(NSError **) error;
```

## Mentions

- [Connecting players with their friends in your game](../connecting-players-with-their-friends-in-your-game.md)

## Discussion

If this method throws an exception, it doesn’t present the view controller.

## Parameters

- `viewController`: The view controller that contains the Messages sheet, and that this method presents.

## See Also

### Adding Friends
- [var isPresentingFriendRequestViewController: Bool](./ispresentingfriendrequestviewcontroller.md)
  A Boolean value that indicates whether your game presents the friends request view controller.
- [func presentFriendRequestCreator(from: NSWindow?) throws](./presentfriendrequestcreator%28from%29-7clh6.md)
  Opens the Messages app with a sheet for the player to request friends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/presentfriendrequestcreator(from:)-7j1kn)*