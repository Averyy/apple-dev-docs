# scale(by:duration:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that uniformly changes the scale factor of a node by a relative value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func scale(by scale: CGFloat, duration sec: TimeInterval) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`scale`](scnnode/scale.md) property animates to the new value.

This action is reversible; the reverse is created as if the following code had been executed:

```objc
[SCNAction scaleBy: -scale duration: sec];
```

## Parameters

- `scale`: The amount of change to make to all three components of the node’s scale.
- `sec`: The duration, in seconds, of the animation.

## See Also

- [class func scale(to: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/scale(to:duration:).md)
  Creates an action that uniformly changes the scale factor of a node to an absolute value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/scale(by:duration:))*