# gameCenterDelegate

**Framework**: GameKit  
**Kind**: property

The view controller’s delegate.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
weak var gameCenterDelegate: (any GKGameCenterControllerDelegate)? { get set }
```

#### Discussion

Before presenting the view controller, your game must set a delegate.

## See Also

- [protocol GKGameCenterControllerDelegate](gkgamecentercontrollerdelegate.md)
  The delegate that GameKit calls when the player dismisses the dashboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/gamecenterdelegate)*