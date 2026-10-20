# composeViewDelegate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The view controller’s delegate

**Availability**:
- iOS 4.2+ - Deprecated in 10.0
- iPadOS 4.2+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported.

## Declaration

```swift
weak var composeViewDelegate: (any GKFriendRequestComposeViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<GKFriendRequestComposeViewControllerDelegate> composeViewDelegate;
```

#### Discussion

Before displaying the friend request, your game must set a delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/composeviewdelegate)*