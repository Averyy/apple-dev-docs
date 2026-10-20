# init(CGRect:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a new value object containing the specified CoreGraphics rectangle structure.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(CGRect rect: CGRect)
```

```swift
init(cgRect rect: CGRect)
```

```objc
+ (NSValue *) valueWithCGRect:(CGRect) rect;
```

#### Return Value

A new value object that contains the rectangle information.

## Parameters

- `rect`: The value for the new object.

## See Also

### Related Documentation
- [struct CGRect](../../CoreFoundation/cgrect.md)
### Working with CoreGraphics Geometry Values
- [init(CGPoint: CGPoint)](./init%28cgpoint%29.md)
  Creates a new value object containing the specified CoreGraphics point structure.
- [init(CGVector: CGVector)](./init%28cgvector%29.md)
  Creates a new value object containing the specified CoreGraphics vector structure.
- [init(CGSize: CGSize)](./init%28cgsize%29.md)
  Creates a new value object containing the specified CoreGraphics size structure.
- [init(CGAffineTransform: CGAffineTransform)](./init%28cgaffinetransform%29.md)
  Creates a new value object containing the specified CoreGraphics affine transform structure.
- [var cgPointValue: CGPoint](./cgpointvalue.md)
  Returns the CoreGraphics point structure representation of the value.
- [var cgVectorValue: CGVector](./cgvectorvalue.md)
  Returns the CoreGraphics vector structure representation of the value.
- [var cgSizeValue: CGSize](./cgsizevalue.md)
  Returns the CoreGraphics size structure representation of the value.
- [var cgRectValue: CGRect](./cgrectvalue.md)
  Returns the CoreGraphics rectangle structure representation of the value.
- [var cgAffineTransformValue: CGAffineTransform](./cgaffinetransformvalue.md)
  Returns the CoreGraphics affine transform representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(cgrect:))*