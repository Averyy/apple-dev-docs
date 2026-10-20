# hide()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that hides a node.

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
class func hide() -> SCNAction
```

```objc
+ (SCNAction *) hide;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`isHidden`](../scnnode/ishidden.md) property is set to [`true`](../../Swift/true.md).

This action is reversible; the reverse is equivalent to the [`unhide()`](./unhide%28%29.md) action.

## See Also

### Creating Actions That Change a Node’s Visibility
- [class func unhide() -> SCNAction](./unhide%28%29.md)
  Creates an action that ensures a node is not hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/hide())*