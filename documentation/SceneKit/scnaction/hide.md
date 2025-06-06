# hide()

**Framework**: SceneKit  
**Kind**: method

Creates an action that hides a node.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func hide() -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`isHidden`](scnnode/ishidden.md) property is set to [`true`](https://developer.apple.com/documentation/swift/true).

This action is reversible; the reverse is equivalent to the [`unhide()`](scnaction/unhide().md) action.

## See Also

- [class func unhide() -> SCNAction](scnaction/unhide.md)
  Creates an action that ensures a node is not hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/hide())*