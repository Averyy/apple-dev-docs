# fadeOpacity(by:duration:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that adjusts the opacity of a node by a relative value.

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
class func fadeOpacity(by factor: CGFloat, duration sec: TimeInterval) -> SCNAction
```

```objc
+ (SCNAction *) fadeOpacityBy:(CGFloat) factor duration:(NSTimeInterval) sec;
```

## Return Value

A new action object.

## Discussion

When the action executes, the node’s [`opacity`](../scnnode/opacity.md) property animates to its new value.

This action is reversible; the reverse is created as if the following code had been executed:

```objc
[SCNAction fadeOpacityBy: -factor duration: sec];
```

## Parameters

- `factor`: The amount to change the node’s opacity by.
- `sec`: The duration, in seconds, of the animation.

## See Also

### Creating Actions That Change a Node’s Opacity
- [class func fadeIn(duration: TimeInterval) -> SCNAction](./fadein%28duration%29.md)
  Creates an action that changes the opacity of the node to `1.0`.
- [class func fadeOut(duration: TimeInterval) -> SCNAction](./fadeout%28duration%29.md)
  Creates an action that changes the opacity of the node to `0.0`.
- [class func fadeOpacity(to: CGFloat, duration: TimeInterval) -> SCNAction](./fadeopacity%28to,duration%29.md)
  Creates an action that adjusts the opacity of a node to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/fadeopacity(by:duration:))*