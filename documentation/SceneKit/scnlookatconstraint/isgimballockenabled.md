# isGimbalLockEnabled

**Framework**: SceneKit  
**Kind**: property

A Boolean value that specifies whether constrained nodes are allowed to rotate.

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
var isGimbalLockEnabled: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), constrained nodes are limited in rotation around a roll axis (the vector pointing from the constrained node to the target node). If the value of this property is [`false`](https://developer.apple.com/documentation/swift/false) (the default), constrained nodes rotate freely around this axis when the constraint adjusts their orientation.

For example, when constraining a camera to follow a moving object, setting this property to [`true`](https://developer.apple.com/documentation/swift/true) ensures that the horizon remains level from the camera’s point of view.

## See Also

- [var target: SCNNode?](scnlookatconstraint/target.md)
  The node toward which constrained nodes will point after being reoriented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlookatconstraint/isgimballockenabled)*