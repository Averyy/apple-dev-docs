# fadeOut(duration:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that changes the opacity of the node to `0.0`.

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
class func fadeOut(duration sec: TimeInterval) -> SCNAction
```

```objc
+ (SCNAction *) fadeOutWithDuration:(NSTimeInterval) sec;
```

## Return Value

A new action object.

## Discussion

When the action executes, the node’s [`opacity`](../scnnode/opacity.md) property animates from its current value to `0.0`.

This action is reversible; the reverse is created as if the following code had been executed:

```objc
[SCNAction fadeInWithDuration: sec];
```

## Parameters

- `sec`: The duration, in seconds, of the animation.

## See Also

### Creating Actions That Change a Node’s Opacity
- [class func fadeIn(duration: TimeInterval) -> SCNAction](./fadein%28duration%29.md)
  Creates an action that changes the opacity of the node to `1.0`.
- [class func fadeOpacity(by: CGFloat, duration: TimeInterval) -> SCNAction](./fadeopacity%28by,duration%29.md)
  Creates an action that adjusts the opacity of a node by a relative value.
- [class func fadeOpacity(to: CGFloat, duration: TimeInterval) -> SCNAction](./fadeopacity%28to,duration%29.md)
  Creates an action that adjusts the opacity of a node to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/fadeout(duration:))*