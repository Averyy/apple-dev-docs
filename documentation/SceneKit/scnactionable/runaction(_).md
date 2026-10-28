# runAction(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds an action to the list of actions executed by the node.

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
func runAction(_ action: SCNAction)
```

```objc
- (void) runAction:(SCNAction *) action;
```

## Discussion

SceneKit begins running a newly added action when it prepares to render the next frame.

## Parameters

- `action`: The action to be performed.

## See Also

### Running Actions
- [func runAction(SCNAction, completionHandler: (() -> Void)?)](./runaction%28_,completionhandler%29.md)
  Adds an action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.
- [func runAction(SCNAction, forKey: String?)](./runaction%28_,forkey%29.md)
  Adds an identifiable action to the list of actions executed by the node.
- [func runAction(SCNAction, forKey: String?, completionHandler: (() -> Void)?)](./runaction%28_,forkey,completionhandler%29.md)
  Adds an identifiable action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/runaction(_:))*