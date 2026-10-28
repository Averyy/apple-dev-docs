# runAction(_:completionHandler:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds an action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func runAction(_ action: SCNAction, completionHandler block: (@Sendable () -> Void)? = nil)
```

```swift
func runAction(_ action: SCNAction) async
```

```objc
- (void) runAction:(SCNAction *) action completionHandler:(void (^)()) block;
```

## Discussion

The new action is processed the next time SceneKit prepares to render a frame.

SceneKit calls your block after the action’s duration is complete. For example, in a game you could use this method to show a Game Over message after performing a fade-out action on a node that displays a player character.

## Parameters

- `action`: The action to be performed.
- `block`: A completion block that SceneKit calls when the action completes.

## See Also

### Running Actions
- [func runAction(SCNAction)](./runaction%28_%29.md)
  Adds an action to the list of actions executed by the node.
- [func runAction(SCNAction, forKey: String?)](./runaction%28_,forkey%29.md)
  Adds an identifiable action to the list of actions executed by the node.
- [func runAction(SCNAction, forKey: String?, completionHandler: (() -> Void)?)](./runaction%28_,forkey,completionhandler%29.md)
  Adds an identifiable action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/runaction(_:completionhandler:))*