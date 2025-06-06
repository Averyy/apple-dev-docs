# GKGameCenterControllerDelegate

**Framework**: GameKit  
**Kind**: protocol

The delegate that GameKit calls when the player dismisses the dashboard.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol GKGameCenterControllerDelegate : NSObjectProtocol
```

## Mentions

- [Displaying the Game Center dashboard](displaying-the-game-center-dashboard.md)

#### Overview

Delegates of [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) objects conform to the `GKGameCenterControllerDelegate` protocol.

## Topics

### Handling User Actions
- [func gameCenterViewControllerDidFinish(GKGameCenterViewController)](gkgamecentercontrollerdelegate/gamecenterviewcontrollerdidfinish(_:).md)
  Handles when the player dismisses the dashboard.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var gameCenterDelegate: (any GKGameCenterControllerDelegate)?](gkgamecenterviewcontroller/gamecenterdelegate.md)
  The view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecentercontrollerdelegate)*