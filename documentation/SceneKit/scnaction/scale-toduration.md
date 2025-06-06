# scale(to:duration:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that uniformly changes the scale factor of a node to an absolute value.

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
class func scale(to scale: CGFloat, duration sec: TimeInterval) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`scale`](scnnode/scale.md) property animates to the new value.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `scale`: The new value for all three components of the node’s scale.
- `sec`: The duration, in seconds, of the animation.

## See Also

- [class func scale(by: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/scale(by:duration:).md)
  Creates an action that uniformly changes the scale factor of a node by a relative value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/scale(to:duration:))*