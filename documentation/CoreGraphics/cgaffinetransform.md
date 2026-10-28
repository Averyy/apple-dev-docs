# CGAffineTransform

**Framework**: Core Graphics  
**Role**: API Collection

An affine transformation matrix for use in drawing 2D graphics.

## Overview

A transformation specifies how points in one coordinate system map to points in another coordinate system. An affine transformation is a special type of mapping that preserves parallel lines in a path but does not necessarily preserve lengths or angles. Scaling, rotation, and translation are the most commonly used manipulations supported by affine transforms, but skewing is also possible.

For more information on how to create, concatenate, and apply affine transformations, see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

You typically do not need to create an affine transform directly—[`CGContext`](./cgcontext.md) describes functions that modify the current affine transform. If you don’t plan to reuse an affine transform, you may want to use [`scaleBy(x:y:)`](./cgcontext/scaleby%28x,y%29.md), [`rotate(by:)`](./cgcontext/rotate%28by%29.md), [`translateBy(x:y:)`](./cgcontext/translateby%28x,y%29.md), or [`concatenate(_:)`](./cgcontext/concatenate%28_%29.md).

## Topics

### Creating an Affine Transformation Matrix
- [func CGAffineTransformMake(CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformmake%28_,_,_,_,_,_%29.md)
  Returns an affine transformation matrix constructed from values you provide.
- [func CGAffineTransformMakeRotation(CGFloat) -> CGAffineTransform](./cgaffinetransformmakerotation%28_%29.md)
  Returns an affine transformation matrix constructed from a rotation value you provide.
- [func CGAffineTransformMakeScale(CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformmakescale%28_,_%29.md)
  Returns an affine transformation matrix constructed from scaling values you provide.
- [func CGAffineTransformMakeTranslation(CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformmaketranslation%28_,_%29.md)
  Returns an affine transformation matrix constructed from translation values you provide.
### Modifying Affine Transformations
- [func CGAffineTransformTranslate(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformtranslate%28_,_,_%29.md)
  Returns an affine transformation matrix constructed by translating an existing affine transform.
- [func CGAffineTransformScale(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformscale%28_,_,_%29.md)
  Returns an affine transformation matrix constructed by scaling an existing affine transform.
- [func CGAffineTransformRotate(CGAffineTransform, CGFloat) -> CGAffineTransform](./cgaffinetransformrotate%28_,_%29.md)
  Returns an affine transformation matrix constructed by rotating an existing affine transform.
- [func CGAffineTransformInvert(CGAffineTransform) -> CGAffineTransform](./cgaffinetransforminvert%28_%29.md)
  Returns an affine transformation matrix constructed by inverting an existing affine transform.
- [func CGAffineTransformConcat(CGAffineTransform, CGAffineTransform) -> CGAffineTransform](./cgaffinetransformconcat%28_,_%29.md)
  Returns an affine transformation matrix constructed by combining two existing affine transforms.
### Applying Affine Transformations
- [func CGPointApplyAffineTransform(CGPoint, CGAffineTransform) -> CGPoint](./cgpointapplyaffinetransform%28_,_%29.md)
  Returns the point resulting from an affine transformation of an existing point.
- [func CGSizeApplyAffineTransform(CGSize, CGAffineTransform) -> CGSize](./cgsizeapplyaffinetransform%28_,_%29.md)
  Returns the height and width resulting from a transformation of an existing height and width.
- [func CGRectApplyAffineTransform(CGRect, CGAffineTransform) -> CGRect](./cgrectapplyaffinetransform%28_,_%29.md)
  Applies an affine transform to a rectangle.
### Evaluating Affine Transforms
- [func CGAffineTransformIsIdentity(CGAffineTransform) -> Bool](./cgaffinetransformisidentity%28_%29.md)
  Checks whether an affine transform is the identity transform.
- [func CGAffineTransformEqualToTransform(CGAffineTransform, CGAffineTransform) -> Bool](./cgaffinetransformequaltotransform%28_,_%29.md)
  Checks whether two affine transforms are equal.
### Data Types
- [struct CGAffineTransform](../CoreFoundation/cgaffinetransform.md)
### Constants
- [let CGAffineTransformIdentity: CGAffineTransform](./cgaffinetransformidentity.md)
  The identity transform.

## See Also

### Related Documentation
- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
### Reference
- [CGGeometry](./cggeometry.md)
  Various structures and associated functions for 2D geometric primitives.
- [Core Graphics Structures](./core-graphics-structures.md)
- [Core Graphics Enumerations](./core-graphics-enumerations.md)
- [Core Graphics Constants](./core-graphics-constants.md)
- [Core Graphics Functions](./core-graphics-functions.md)
- [Core Graphics Data Types](./core-graphics-data-types.md)
- [Core Graphics Macros](./core-graphics-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgaffinetransform)*