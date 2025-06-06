# fadeIn(duration:)

**Framework**: SceneKit  
**Kind**: method

Creates an action that changes the opacity of the node to `1.0`.

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
class func fadeIn(duration sec: TimeInterval) -> SCNAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`opacity`](scnnode/opacity.md) property animates from its current value to `1.0`.

This action is reversible; the reverse is created as if the following code had been executed:

```objc
[SCNAction fadeOutWithDuration: sec];
```

## Parameters

- `sec`: The duration, in seconds, of the animation.

## See Also

- [class func fadeOut(duration: TimeInterval) -> SCNAction](scnaction/fadeout(duration:).md)
  Creates an action that changes the opacity of the node to `0.0`.
- [class func fadeOpacity(by: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/fadeopacity(by:duration:).md)
  Creates an action that adjusts the opacity of a node by a relative value.
- [class func fadeOpacity(to: CGFloat, duration: TimeInterval) -> SCNAction](scnaction/fadeopacity(to:duration:).md)
  Creates an action that adjusts the opacity of a node to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnaction/fadein(duration:))*