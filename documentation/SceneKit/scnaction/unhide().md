# unhide()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that ensures a node is not hidden.

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
class func unhide() -> SCNAction
```

```objc
+ (SCNAction *) unhide;
```

## Return Value

A new action object.

## Discussion

When the action executes, the node’s [`isHidden`](../scnnode/ishidden.md) property is set to [`false`](../../Swift/false.md).

This action is reversible; the reverse is equivalent to the [`hide()`](./hide%28%29.md) action.

## See Also

### Creating Actions That Change a Node’s Visibility
- [class func hide() -> SCNAction](./hide%28%29.md)
  Creates an action that hides a node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/unhide())*