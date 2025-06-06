# removeAllActions()

**Framework**: SceneKit  
**Kind**: method  
**Required**: Yes

Ends and removes all actions from the node.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func removeAllActions()
```

#### Discussion

When SceneKit removes an action from a node, it skips any remaining animation the action would perform. However, any changes the action has already made to the node’s state remain in effect.

## See Also

- [func removeAction(forKey: String)](scnactionable/removeaction(forkey:).md)
  Removes an action associated with a specific key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactionable/removeallactions())*