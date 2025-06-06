# friendRequestComposeViewControllerDidFinish(_:)

**Framework**: GameKit  
**Kind**: method  
**Required**: Yes

Called when the player dismisses the request.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
func friendRequestComposeViewControllerDidFinish(_ viewController: GKFriendRequestComposeViewController)
```

#### Discussion

Your delegate should dismiss the view controller. If your game paused any gameplay or other activities, it can restart those services in this method.

## Parameters

- `viewController`: The friend request view controller that was dismissed by the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontrollerdelegate/friendrequestcomposeviewcontrollerdidfinish(_:))*