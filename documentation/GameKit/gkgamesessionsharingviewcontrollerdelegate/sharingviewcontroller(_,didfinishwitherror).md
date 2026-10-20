# sharingViewController(_:didFinishWithError:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Indicates the sharing view controller is ready to be dismissed.

**Availability**:
- tvOS 10.0+ - Deprecated in 12.0

> **Deprecated**: For real-time matches, use GKMatchmakerViewControllerDelegate to receive notifications from the GKMatchmakerViewController. For turn-based matches, use GKTurnBasedMatchmakerViewControllerDelegate and GKLocalPlayerListener to receive notifications from the GKTurnBasedMatchmakerViewController.

## Declaration

```swift
func sharingViewController(_ viewController: GKGameSessionSharingViewController, didFinishWithError error: (any Error)?)
```

```objc
- (void) sharingViewController:(GKGameSessionSharingViewController *) viewController didFinishWithError:(NSError *) error;
```

## Parameters

- `viewController`: The sharing view controller to be dismissed.
- `error`: An optional GameKit error. This parameter is `nil` if the sharing view controller is successfully dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessionsharingviewcontrollerdelegate/sharingviewcontroller(_:didfinishwitherror:))*