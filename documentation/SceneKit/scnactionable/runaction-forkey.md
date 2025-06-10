# runAction(_:forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Adds an identifiable action to the list of actions executed by the node.

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
func runAction(_ action: SCNAction, forKey key: String?)
```

#### Discussion

This method is identical to [`runAction(_:)`](scnactionable/runaction(_:).md), but the action is stored and identified so that you can retrieve or cancel it later. If an action using the same key is already running, SceneKit removes it before adding the new action.

## Parameters

- `action`: The action to be performed.
- `key`: A unique key used to identify the action.

## See Also

- [func action(forKey: String) -> SCNAction?](scnactionable/action(forkey:).md)
  Returns an action associated with a specific key.
- [func removeAction(forKey: String)](scnactionable/removeaction(forkey:).md)
  Removes an action associated with a specific key.
- [func runAction(SCNAction)](scnactionable/runaction(_:).md)
  Adds an action to the list of actions executed by the node.
- [func runAction(SCNAction, completionHandler: (() -> Void)?)](scnactionable/runaction(_:completionhandler:).md)
  Adds an action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.
- [func runAction(SCNAction, forKey: String?, completionHandler: (() -> Void)?)](scnactionable/runaction(_:forkey:completionhandler:).md)
  Adds an identifiable action to the list of actions executed by the node. SceneKit calls the specified block when the action completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/runaction(_:forkey:))*