# gameCenterViewControllerDidFinish(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles when the player dismisses the dashboard.

**Availability**:
- iOS 6.0+ - Deprecated in 26.0
- iPadOS 6.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.9+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
func gameCenterViewControllerDidFinish(_ gameCenterViewController: GKGameCenterViewController)
```

```objc
- (void) gameCenterViewControllerDidFinish:(GKGameCenterViewController *) gameCenterViewController;
```

## Mentions

- [Displaying the Game Center dashboard](../displaying-the-game-center-dashboard.md)

#### Discussion

Implement this method to dismiss the Game Center view controller. If your game paused any gameplay or other activities, this method can restart those services.

## Parameters

- `gameCenterViewController`: The view controller that the player closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecentercontrollerdelegate/gamecenterviewcontrollerdidfinish(_:))*