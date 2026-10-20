# scale(to:duration:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that uniformly changes the scale factor of a node to an absolute value.

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
class func scale(to scale: CGFloat, duration sec: TimeInterval) -> SCNAction
```

```objc
+ (SCNAction *) scaleTo:(CGFloat) scale duration:(NSTimeInterval) sec;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`scale`](../scnnode/scale.md) property animates to the new value.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `scale`: The new value for all three components of the node’s scale.
- `sec`: The duration, in seconds, of the animation.

## See Also

### Creating Actions That Change a Node’s Scale
- [class func scale(by: CGFloat, duration: TimeInterval) -> SCNAction](./scale%28by,duration%29.md)
  Creates an action that uniformly changes the scale factor of a node by a relative value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/scale(to:duration:))*