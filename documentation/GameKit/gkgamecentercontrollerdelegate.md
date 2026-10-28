# GKGameCenterControllerDelegate

**Framework**: GameKit  
**Kind**: protocol  
**Role**: Protocol

The delegate that GameKit calls when the player dismisses the dashboard.

**Availability**:
- iOS 6.0+ - Deprecated in 26.0
- iPadOS 6.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
protocol GKGameCenterControllerDelegate : NSObjectProtocol
```

```objc
@protocol GKGameCenterControllerDelegate <NSObject>
```

## Mentions

- [Displaying the Game Center dashboard](./displaying-the-game-center-dashboard.md)

## Overview

Delegates of [`GKGameCenterViewController`](./gkgamecenterviewcontroller.md) objects conform to the `GKGameCenterControllerDelegate` protocol.

## Topics

### Handling User Actions
- [func gameCenterViewControllerDidFinish(GKGameCenterViewController)](./gkgamecentercontrollerdelegate/gamecenterviewcontrollerdidfinish%28_%29.md)
  Handles when the player dismisses the dashboard.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setting the view controller delegate
- [var gameCenterDelegate: (any GKGameCenterControllerDelegate)?](./gkgamecenterviewcontroller/gamecenterdelegate.md)
  The view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecentercontrollerdelegate)*