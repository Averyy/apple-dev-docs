# removeAction(forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Removes an action associated with a specific key.

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
func removeAction(forKey key: String)
```

#### Discussion

If the node is currently running an action that matches the key, SceneKit removes that action from the node, skipping any remaining animation it would perform but keeping any changes already made to the node.

Use this method to cancel actions you scheduled using the [`runAction(_:forKey:)`](scnactionable/runaction(_:forkey:).md) or [`runAction(_:forKey:completionHandler:)`](scnactionable/runaction(_:forkey:completionhandler:).md) method.

## Parameters

- `key`: A string that uniquely identifies a action.

## See Also

- [func removeAllActions()](scnactionable/removeallactions.md)
  Ends and removes all actions from the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/removeaction(forkey:))*