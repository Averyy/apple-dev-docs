# simdWorldFront

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The “forward” (-Z) direction vector relative to the node, expressed in world space.

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
var simdWorldFront: simd_float3 { get }
```

```objc
@property (nonatomic, readonly) simd_float3 simdWorldFront;
```

## Discussion

Reading this property is equivalent to reading the [`simdLocalFront`](./simdlocalfront.md) class property and using the [`simdConvertVector(_:to:)`](./simdconvertvector%28_,to%29.md) or [`simdConvertVector(_:from:)`](./simdconvertvector%28_,from%29.md) method to convert that vector from the node’s local coordinate space to the scene’s world coordinate space.

## See Also

### Related Documentation
- [var worldFront: SCNVector3](./worldfront.md)
  The “forward” (-Z) direction vector relative to the node, expressed in world space.
### Calculating Node-Relative Transforms
- [class var simdLocalRight: simd_float3](./simdlocalright.md)
  The direction SceneKit treats as “right” in local space for all nodes.
- [class var simdLocalUp: simd_float3](./simdlocalup.md)
  The direction SceneKit treats as “up” in local space for all nodes.
- [class var simdLocalFront: simd_float3](./simdlocalfront.md)
  The unit vector SceneKit treats as “forward” in local space for all nodes.
- [var simdWorldRight: simd_float3](./simdworldright.md)
  The “right” (+X) direction vector relative to the node, expressed in world space.
- [var simdWorldUp: simd_float3](./simdworldup.md)
  The “up” (+Y) direction vector relative to the node, expressed in world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/simdworldfront)*