# init(CGAffineTransform:)

**Framework**: Foundation  
**Kind**: init

Creates a new value object containing the specified CoreGraphics affine transform structure.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(cgAffineTransform transform: CGAffineTransform)
```

#### Return Value

A new value object that contains the affine transform information.

## Parameters

- `transform`: The value for the new object.

## See Also

- [CGAffineTransform](../CoreGraphics/cgaffinetransform.md)
  An affine transformation matrix for use in drawing 2D graphics.
- [init(CGPoint: CGPoint)](nsvalue/init(cgpoint:).md)
  Creates a new value object containing the specified CoreGraphics point structure.
- [init(CGVector: CGVector)](nsvalue/init(cgvector:).md)
  Creates a new value object containing the specified CoreGraphics vector structure.
- [init(CGSize: CGSize)](nsvalue/init(cgsize:).md)
  Creates a new value object containing the specified CoreGraphics size structure.
- [init(CGRect: CGRect)](nsvalue/init(cgrect:).md)
  Creates a new value object containing the specified CoreGraphics rectangle structure.
- [var cgPointValue: CGPoint](nsvalue/cgpointvalue.md)
  Returns the CoreGraphics point structure representation of the value.
- [var cgVectorValue: CGVector](nsvalue/cgvectorvalue.md)
  Returns the CoreGraphics vector structure representation of the value.
- [var cgSizeValue: CGSize](nsvalue/cgsizevalue.md)
  Returns the CoreGraphics size structure representation of the value.
- [var cgRectValue: CGRect](nsvalue/cgrectvalue.md)
  Returns the CoreGraphics rectangle structure representation of the value.
- [var cgAffineTransformValue: CGAffineTransform](nsvalue/cgaffinetransformvalue.md)
  Returns the CoreGraphics affine transform representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(cgaffinetransform:))*