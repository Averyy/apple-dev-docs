# isGimbalLockEnabled

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether constrained nodes are allowed to rotate.

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
var isGimbalLockEnabled: Bool { get set }
```

```objc
@property (nonatomic) BOOL gimbalLockEnabled;
```

## Discussion

If the value of this property is [`true`](../../Swift/true.md), constrained nodes are limited in rotation around a roll axis (the vector pointing from the constrained node to the target node). If the value of this property is [`false`](../../Swift/false.md) (the default), constrained nodes rotate freely around this axis when the constraint adjusts their orientation.

For example, when constraining a camera to follow a moving object, setting this property to [`true`](../../Swift/true.md) ensures that the horizon remains level from the camera’s point of view.

## See Also

### Modifying a Constraint
- [var target: SCNNode?](./target.md)
  The node toward which constrained nodes will point after being reoriented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlookatconstraint/isgimballockenabled)*