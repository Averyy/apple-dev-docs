# fadeOpacity(to:duration:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that adjusts the opacity of a node to a new value.

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
class func fadeOpacity(to opacity: CGFloat, duration sec: TimeInterval) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`opacity`](scnnode/opacity.md) property animates to its new value.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `opacity`: The new opacity value of the node.
- `sec`: The duration, in seconds, of the animation.

## See Also

- [class func fadeIn(duration: TimeInterval) -> SCNAction](scnaction/fadein(duration:).md)
  Creates an action that changes the opacity of the node to `1.0`.
- [class func fadeOut(duration: TimeInterval) -> SCNAction](scnaction/fadeout(duration:).md)
  Creates an action that changes the opacity of the node to `0.0`.
- [class func fadeOpacity(by: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/fadeopacity(by:duration:).md)
  Creates an action that adjusts the opacity of a node by a relative value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/fadeopacity(to:duration:))*