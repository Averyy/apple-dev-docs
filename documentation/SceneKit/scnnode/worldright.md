# worldRight

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The “right” (+X) direction vector relative to the node, expressed in world space.

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
var worldRight: SCNVector3 { get }
```

```objc
@property (nonatomic, readonly) SCNVector3 worldRight;
```

## Discussion

Reading this property is equivalent to reading the [`localRight`](./localright.md) class property and using the [`convertVector(_:to:)`](./convertvector%28_,to%29.md) or [`convertVector(_:from:)`](./convertvector%28_,from%29.md) method to convert that vector from the node’s local coordinate space to the scene’s world coordinate space.

## See Also

### Related Documentation
- [var simdWorldRight: simd_float3](./simdworldright.md)
  The “right” (+X) direction vector relative to the node, expressed in world space.
### Calculating Node-Relative Transforms (SceneKit Types)
- [class var localRight: SCNVector3](./localright.md)
  The direction SceneKit treats as “right” in local space for all nodes.
- [class var localUp: SCNVector3](./localup.md)
  The direction SceneKit treats as “up” in local space for all nodes.
- [class var localFront: SCNVector3](./localfront.md)
  The unit vector SceneKit treats as “forward” in local space for all nodes.
- [var worldUp: SCNVector3](./worldup.md)
  The “up” (+Y) direction vector relative to the node, expressed in world space.
- [var worldFront: SCNVector3](./worldfront.md)
  The “forward” (-Z) direction vector relative to the node, expressed in world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/worldright)*