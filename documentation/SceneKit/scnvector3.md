# SCNVector3

**Framework**: SceneKit  
**Kind**: struct

A representation of a three-component vector.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct SCNVector3
```

#### Overview

SceneKit uses three-component vectors for a variety of purposes, such as describing node or vertex positions, surface normals, and scale or translation transforms. The different vector components should be interpreted based on the context in which the vector is being used.

> ❗ **Important**:  In macOS, the `x`, `y`, and `z` fields in this structure are [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct) values. In iOS, tvOS, and watchOS, these fields are `float` values.

 In macOS, the `x`, `y`, and `z` fields in this structure are [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct) values. In iOS, tvOS, and watchOS, these fields are `float` values.

## Topics

### Components
- [var x: Float](scnvector3/x.md)
  The first component in the vector.
- [var y: Float](scnvector3/y.md)
  The second component in the vector.
- [var z: Float](scnvector3/z.md)
  The third component in the vector.
### Creating Vectors
- [func SCNVector3Make(Float, Float, Float) -> SCNVector3](scnvector3make(_:_:_:).md)
  Returns a new three-component vector created from individual component values.
### Converting Vector Types
- [func SCNVector3FromGLKVector3(GLKVector3) -> SCNVector3](scnvector3fromglkvector3(_:).md)
  Returns a three-element SceneKit vector structure corresponding to a GLKit vector structure.
- [func SCNVector3ToGLKVector3(SCNVector3) -> GLKVector3](scnvector3toglkvector3(_:).md)
  Returns a three-element GLKit vector structure corresponding to a SceneKit vector structure.
### Comparing Vectors
- [func SCNVector3EqualToVector3(SCNVector3, SCNVector3) -> Bool](scnvector3equaltovector3(_:_:).md)
  Returns a Boolean value that indicates whether the corresponding components of two vectors are equal.
### Zero Constant
- [let SCNVector3Zero: SCNVector3](scnvector3zero.md)
  The three-component vector whose every component is `0.0`.
### Initializers
- [init()](scnvector3/init.md)
- [init(SIMD3<Double>)](scnvector3/init(_:)-10rap.md)
- [init(SIMD3<Float>)](scnvector3/init(_:)-9wg16.md)
- [init(Int, Int, Int)](scnvector3/init(_:_:_:)-2hhr6.md)
- [init(CGFloat, CGFloat, CGFloat)](scnvector3/init(_:_:_:)-50jm7.md)
- [init(Double, Double, Double)](scnvector3/init(_:_:_:)-7clbx.md)
- [init(Float, Float, Float)](scnvector3/init(_:_:_:)-8cwh7.md)
- [init(x: CGFloat, y: CGFloat, z: CGFloat)](scnvector3/init(x:y:z:)-28n6q.md)
- [init(x: Float, y: Float, z: Float)](scnvector3/init(x:y:z:)-mn27.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct SCNVector4](scnvector4.md)
  A representation of a four-component vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnvector3)*