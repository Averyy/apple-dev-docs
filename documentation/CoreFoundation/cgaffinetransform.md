# CGAffineTransform

**Framework**: Core Foundation  
**Kind**: struct

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
struct CGAffineTransform
```

## Topics

### Initializers
- [init()](cgaffinetransform/init.md)
- [init(CGAffineTransformComponents)](cgaffinetransform/init(_:).md)
- [init(CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)](cgaffinetransform/init(_:_:_:_:_:_:).md)
- [init(a: Double, b: Double, c: Double, d: Double, tx: Double, ty: Double)](cgaffinetransform/init(a:b:c:d:tx:ty:).md)
- [init(rotationAngle: CGFloat)](cgaffinetransform/init(rotationangle:).md)
- [init(scaleX: CGFloat, y: CGFloat)](cgaffinetransform/init(scalex:y:).md)
- [init(translationX: CGFloat, y: CGFloat)](cgaffinetransform/init(translationx:y:).md)
### Instance Properties
- [var a: Double](cgaffinetransform/a.md)
- [var b: Double](cgaffinetransform/b.md)
- [var c: Double](cgaffinetransform/c.md)
- [var d: Double](cgaffinetransform/d.md)
- [var isIdentity: Bool](cgaffinetransform/isidentity.md)
- [var tx: Double](cgaffinetransform/tx.md)
- [var ty: Double](cgaffinetransform/ty.md)
### Instance Methods
- [func concatenating(CGAffineTransform) -> CGAffineTransform](cgaffinetransform/concatenating(_:).md)
- [func decomposed() -> CGAffineTransformComponents](cgaffinetransform/decomposed.md)
- [func inverted() -> CGAffineTransform](cgaffinetransform/inverted.md)
- [func rotated(by: CGFloat) -> CGAffineTransform](cgaffinetransform/rotated(by:).md)
- [func scaledBy(x: CGFloat, y: CGFloat) -> CGAffineTransform](cgaffinetransform/scaledby(x:y:).md)
- [func translatedBy(x: CGFloat, y: CGFloat) -> CGAffineTransform](cgaffinetransform/translatedby(x:y:).md)
### Type Properties
- [static var identity: CGAffineTransform](cgaffinetransform/identity.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CGAffineTransformComponents](cgaffinetransformcomponents.md)
- [struct CGFloat](cgfloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [struct CGPoint](cgpoint.md)
- [struct CGRect](cgrect.md)
- [struct CGSize](cgsize.md)
  A structure that contains width and height values.
- [struct CGVector](cgvector.md)
  A structure that contains a two-dimensional vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cgaffinetransform)*