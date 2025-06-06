# unhide()

**Framework**: SceneKit  
**Kind**: method

Creates an action that ensures a node is not hidden.

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
class func unhide() -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`isHidden`](scnnode/ishidden.md) property is set to [`false`](https://developer.apple.com/documentation/swift/false).

This action is reversible; the reverse is equivalent to the [`hide()`](scnaction/hide().md) action.

## See Also

- [class func hide() -> SCNAction](scnaction/hide.md)
  Creates an action that hides a node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/unhide())*