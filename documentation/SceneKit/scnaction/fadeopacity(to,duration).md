# fadeOpacity(to:duration:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that adjusts the opacity of a node to a new value.

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
class func fadeOpacity(to opacity: CGFloat, duration sec: TimeInterval) -> SCNAction
```

```objc
+ (SCNAction *) fadeOpacityTo:(CGFloat) opacity duration:(NSTimeInterval) sec;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`opacity`](../scnnode/opacity.md) property animates to its new value.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `opacity`: The new opacity value of the node.
- `sec`: The duration, in seconds, of the animation.

## See Also

### Creating Actions That Change a Node’s Opacity
- [class func fadeIn(duration: TimeInterval) -> SCNAction](./fadein%28duration%29.md)
  Creates an action that changes the opacity of the node to `1.0`.
- [class func fadeOut(duration: TimeInterval) -> SCNAction](./fadeout%28duration%29.md)
  Creates an action that changes the opacity of the node to `0.0`.
- [class func fadeOpacity(by: CGFloat, duration: TimeInterval) -> SCNAction](./fadeopacity%28by,duration%29.md)
  Creates an action that adjusts the opacity of a node by a relative value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/fadeopacity(to:duration:))*