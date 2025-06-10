# removeFromParentNode()

**Framework**: SceneKit  
**Kind**: method

Creates an action that removes the node from its parent.

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
class func removeFromParentNode() -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node is immediately removed from its parent.

This action is not reversible; the reverse of this action is the same action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/removefromparentnode())*