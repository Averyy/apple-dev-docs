# gameCenterDelegate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The view controller’s delegate.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
weak var gameCenterDelegate: (any GKGameCenterControllerDelegate)? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, weak, nullable) id<GKGameCenterControllerDelegate> gameCenterDelegate;
```

*macOS*

```objc
@property (atomic, weak, nullable) id<GKGameCenterControllerDelegate> gameCenterDelegate;
```

#### Discussion

Before presenting the view controller, your game must set a delegate.

## See Also

### Setting the view controller delegate
- [protocol GKGameCenterControllerDelegate](../gkgamecentercontrollerdelegate.md)
  The delegate that GameKit calls when the player dismisses the dashboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/gamecenterdelegate)*