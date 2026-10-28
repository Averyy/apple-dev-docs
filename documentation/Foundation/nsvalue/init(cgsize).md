# init(CGSize:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a new value object containing the specified CoreGraphics size structure.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(CGSize size: CGSize)
```

```swift
init(cgSize size: CGSize)
```

```objc
+ (NSValue *) valueWithCGSize:(CGSize) size;
```

## Return Value

A new value object that contains the size information.

## Parameters

- `size`: The value for the new object.

## See Also

### Related Documentation
- [struct CGSize](../../CoreFoundation/cgsize.md)
  A structure that contains width and height values.
### Working with CoreGraphics Geometry Values
- [init(CGPoint: CGPoint)](./init%28cgpoint%29.md)
  Creates a new value object containing the specified CoreGraphics point structure.
- [init(CGVector: CGVector)](./init%28cgvector%29.md)
  Creates a new value object containing the specified CoreGraphics vector structure.
- [init(CGRect: CGRect)](./init%28cgrect%29.md)
  Creates a new value object containing the specified CoreGraphics rectangle structure.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(cgsize:))*