# SCNVector4

**Framework**: SceneKit  
**Kind**: struct

A representation of a four-component vector.

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
struct SCNVector4
```

#### Overview

SceneKit uses four-component vectors to represent multiple kinds of data:

- Axis-angle rotation or torque. The `x`, `y`, and `z` fields contain the normalized x-, y-, and z-components of the rotation axis, and the `w` field contains the rotation angle, in radians, or torque magnitude, in newton-meters.
- Color value (or range). The `x`, `y`, `z`, and `w` fields contain the red, green, blue, and alpha components of the color, or the width of the color variation range in each component.

> ❗ **Important**:  In macOS, the `x`, `y`, `z` and `w` fields in this structure are [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct) values. In iOS, tvOS, and watchOS, these fields are `float` values.

 In macOS, the `x`, `y`, `z` and `w` fields in this structure are [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct) values. In iOS, tvOS, and watchOS, these fields are `float` values.

## Topics

### Components
- [var x: Float](scnvector4/x.md)
  The first component in the vector.
- [var y: Float](scnvector4/y.md)
  The second component in the vector.
- [var z: Float](scnvector4/z.md)
  The third component in the vector.
- [var w: Float](scnvector4/w.md)
  The fourth component in the vector.
### Creating Vectors
- [func SCNVector4Make(Float, Float, Float, Float) -> SCNVector4](scnvector4make(_:_:_:_:).md)
  Returns a new four-component vector created from individual component values.
### Converting Vector Types
- [func SCNVector4FromGLKVector4(GLKVector4) -> SCNVector4](scnvector4fromglkvector4(_:).md)
  Returns a four-element SceneKit vector structure corresponding to a GLKit vector structure.
- [func SCNVector4ToGLKVector4(SCNVector4) -> GLKVector4](scnvector4toglkvector4(_:).md)
  Returns a four-element GLKit vector structure corresponding to a SceneKit vector structure.
### Comparing Vectors
- [func SCNVector4EqualToVector4(SCNVector4, SCNVector4) -> Bool](scnvector4equaltovector4(_:_:).md)
  Returns a Boolean value that indicates whether the corresponding components of two vectors are equal.
### Zero Constant
- [let SCNVector4Zero: SCNVector4](scnvector4zero.md)
  The four-component vector whose every component is `0.0`.
### Initializers
- [init()](scnvector4/init.md)
- [init(SIMD4<Double>)](scnvector4/init(_:)-5q2cx.md)
- [init(SIMD4<Float>)](scnvector4/init(_:)-6w6mx.md)
- [init(Int, Int, Int, Int)](scnvector4/init(_:_:_:_:)-6otq6.md)
- [init(Double, Double, Double, Double)](scnvector4/init(_:_:_:_:)-85e6w.md)
- [init(CGFloat, CGFloat, CGFloat, CGFloat)](scnvector4/init(_:_:_:_:)-93hx1.md)
- [init(Float, Float, Float, Float)](scnvector4/init(_:_:_:_:)-pk7r.md)
- [init(x: Float, y: Float, z: Float, w: Float)](scnvector4/init(x:y:z:w:)-37b3a.md)
- [init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)](scnvector4/init(x:y:z:w:)-7hxmu.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct SCNVector3](scnvector3.md)
  A representation of a three-component vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnvector4)*