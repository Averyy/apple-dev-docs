# runAction(_:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Adds an action to the list of actions executed by the node.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func runAction(_ action: SCNAction)
```

#### Discussion

SceneKit begins running a newly added action when it prepares to render the next frame.

## Parameters

- `action`: The action to be performed.

## See Also

- [func runAction(SCNAction, completionHandler: (() -> Void)?)](scnactionable/runaction(_:completionhandler:).md)
  Adds an action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.
- [func runAction(SCNAction, forKey: String?)](scnactionable/runaction(_:forkey:).md)
  Adds an identifiable action to the list of actions executed by the node.
- [func runAction(SCNAction, forKey: String?, completionHandler: (() -> Void)?)](scnactionable/runaction(_:forkey:completionhandler:).md)
  Adds an identifiable action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/runaction(_:))*