# gameCenterViewControllerDidFinish(_:)

**Framework**: GameKit  
**Kind**: method  
**Required**: Yes

Handles when the player dismisses the dashboard.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func gameCenterViewControllerDidFinish(_ gameCenterViewController: GKGameCenterViewController)
```

## Mentions

- [Displaying the Game Center dashboard](displaying-the-game-center-dashboard.md)

#### Discussion

Implement this method to dismiss the Game Center view controller. If your game paused any gameplay or other activities, this method can restart those services.

## Parameters

- `gameCenterViewController`: The view controller that the player closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecentercontrollerdelegate/gamecenterviewcontrollerdidfinish(_:))*