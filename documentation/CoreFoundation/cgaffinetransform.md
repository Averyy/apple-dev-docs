# CGAffineTransform

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct CGAffineTransform
```

```c
struct CGAffineTransform;
```

## Topics

### Initializers
- [init()](./cgaffinetransform/init%28%29.md)
- [init(CGAffineTransformComponents)](./cgaffinetransform/init%28_%29.md)
- [init(CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat)](./cgaffinetransform/init%28_,_,_,_,_,_%29.md)
- [init(a: Double, b: Double, c: Double, d: Double, tx: Double, ty: Double)](./cgaffinetransform/init%28a,b,c,d,tx,ty%29.md)
- [init(rotationAngle: CGFloat)](./cgaffinetransform/init%28rotationangle%29.md)
- [init(scaleX: CGFloat, y: CGFloat)](./cgaffinetransform/init%28scalex,y%29.md)
- [init(translationX: CGFloat, y: CGFloat)](./cgaffinetransform/init%28translationx,y%29.md)
### Instance Properties
- [var a: Double](./cgaffinetransform/a.md)
- [var b: Double](./cgaffinetransform/b.md)
- [var c: Double](./cgaffinetransform/c.md)
- [var d: Double](./cgaffinetransform/d.md)
- [var isIdentity: Bool](./cgaffinetransform/isidentity.md)
- [var tx: Double](./cgaffinetransform/tx.md)
- [var ty: Double](./cgaffinetransform/ty.md)
### Instance Methods
- [func concatenating(CGAffineTransform) -> CGAffineTransform](./cgaffinetransform/concatenating%28_%29.md)
- [func decomposed() -> CGAffineTransformComponents](./cgaffinetransform/decomposed%28%29.md)
- [func inverted() -> CGAffineTransform](./cgaffinetransform/inverted%28%29.md)
- [func rotated(by: CGFloat) -> CGAffineTransform](./cgaffinetransform/rotated%28by%29.md)
- [func scaledBy(x: CGFloat, y: CGFloat) -> CGAffineTransform](./cgaffinetransform/scaledby%28x,y%29.md)
- [func translatedBy(x: CGFloat, y: CGFloat) -> CGAffineTransform](./cgaffinetransform/translatedby%28x,y%29.md)
### Type Properties
- [static var identity: CGAffineTransform](./cgaffinetransform/identity.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Structures
- [struct CGAffineTransformComponents](./cgaffinetransformcomponents.md)
- [struct CGFloat](./cgfloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [struct CGPoint](./cgpoint.md)
- [struct CGRect](./cgrect.md)
- [struct CGSize](./cgsize.md)
  A structure that contains width and height values.
- [struct CGVector](./cgvector.md)
  A structure that contains a two-dimensional vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cgaffinetransform)*