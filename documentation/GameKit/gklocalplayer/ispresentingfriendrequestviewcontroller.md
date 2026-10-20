# isPresentingFriendRequestViewController

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether your game presents the friends request view controller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var isPresentingFriendRequestViewController: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isPresentingFriendRequestViewController;
```

#### Discussion

[`true`](../../Swift/true.md) if the friends request view controller appears; otherwise, [`false`](../../Swift/false.md).

## See Also

### Adding Friends
- [func presentFriendRequestCreator(from: UIViewController) throws](./presentfriendrequestcreator%28from%29-7j1kn.md)
  Presents a view controller with a Messages sheet for the player to request friends.
- [func presentFriendRequestCreator(from: NSWindow?) throws](./presentfriendrequestcreator%28from%29-7clh6.md)
  Opens the Messages app with a sheet for the player to request friends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gklocalplayer/ispresentingfriendrequestviewcontroller)*