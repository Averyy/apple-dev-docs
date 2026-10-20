# friendRequestComposeViewControllerDidFinish(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when the player dismisses the request.

**Availability**:
- iOS 4.2+ - Deprecated in 10.0
- iPadOS 4.2+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported.

## Declaration

```swift
func friendRequestComposeViewControllerDidFinish(_ viewController: GKFriendRequestComposeViewController)
```

```objc
- (void) friendRequestComposeViewControllerDidFinish:(GKFriendRequestComposeViewController *) viewController;
```

#### Discussion

Your delegate should dismiss the view controller. If your game paused any gameplay or other activities, it can restart those services in this method.

## Parameters

- `viewController`: The friend request view controller that was dismissed by the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontrollerdelegate/friendrequestcomposeviewcontrollerdidfinish(_:))*