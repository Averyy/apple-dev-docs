# scale(by:duration:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates an action that uniformly changes the scale factor of a node by a relative value.

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
class func scale(by scale: CGFloat, duration sec: TimeInterval) -> SCNAction
```

```objc
+ (SCNAction *) scaleBy:(CGFloat) scale duration:(NSTimeInterval) sec;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`scale`](../scnnode/scale.md) property animates to the new value.

This action is reversible; the reverse is created as if the following code had been executed:

```objc
[SCNAction scaleBy: -scale duration: sec];
```

## Parameters

- `scale`: The amount of change to make to all three components of the node’s scale.
- `sec`: The duration, in seconds, of the animation.

## See Also

### Creating Actions That Change a Node’s Scale
- [class func scale(to: CGFloat, duration: TimeInterval) -> SCNAction](./scale%28to,duration%29.md)
  Creates an action that uniformly changes the scale factor of a node to an absolute value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/scale(by:duration:))*