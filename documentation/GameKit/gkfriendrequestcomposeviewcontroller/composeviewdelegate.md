# composeViewDelegate

**Framework**: GameKit  
**Kind**: property

The view controller’s delegate

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var composeViewDelegate: (any GKFriendRequestComposeViewControllerDelegate)? { get set }
```

#### Discussion

Before displaying the friend request, your game must set a delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/composeviewdelegate)*