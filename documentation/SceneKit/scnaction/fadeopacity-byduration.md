# fadeOpacity(by:duration:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that adjusts the opacity of a node by a relative value.

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
class func fadeOpacity(by factor: CGFloat, duration sec: TimeInterval) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`opacity`](scnnode/opacity.md) property animates to its new value.

This action is reversible; the reverse is created as if the following code had been executed:

```objc
[SCNAction fadeOpacityBy: -factor duration: sec];
```

## Parameters

- `factor`: The amount to change the node’s opacity by.
- `sec`: The duration, in seconds, of the animation.

## See Also

- [class func fadeIn(duration: TimeInterval) -> SCNAction](scnaction/fadein(duration:).md)
  Creates an action that changes the opacity of the node to `1.0`.
- [class func fadeOut(duration: TimeInterval) -> SCNAction](scnaction/fadeout(duration:).md)
  Creates an action that changes the opacity of the node to `0.0`.
- [class func fadeOpacity(to: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/fadeopacity(to:duration:).md)
  Creates an action that adjusts the opacity of a node to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/fadeopacity(by:duration:))*