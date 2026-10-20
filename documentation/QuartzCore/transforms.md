# Transforms

**Framework**: Core Animation  
**Role**: API Collection

Define transform matrices to apply affine transformations to layers in Core Animation.

## Topics

### Creating Transforms
- [func CATransform3DMakeTranslation(CGFloat, CGFloat, CGFloat) -> CATransform3D](./catransform3dmaketranslation%28_,_,_%29.md)
  Returns a transform that translates by `(tx, ty, tz)`.
- [func CATransform3DMakeScale(CGFloat, CGFloat, CGFloat) -> CATransform3D](./catransform3dmakescale%28_,_,_%29.md)
  Returns a transform that scales by `(sx, sy, sz)`.
- [func CATransform3DMakeRotation(CGFloat, CGFloat, CGFloat, CGFloat) -> CATransform3D](./catransform3dmakerotation%28_,_,_,_%29.md)
  Returns a transform that rotates by `angle` radians about the vector `(x, y, z)`.
### Chaining Transforms
- [func CATransform3DConcat(CATransform3D, CATransform3D) -> CATransform3D](./catransform3dconcat%28_,_%29.md)
  Concatenates `b` to `a` and returns the result: `t = a * b`.
- [func CATransform3DTranslate(CATransform3D, CGFloat, CGFloat, CGFloat) -> CATransform3D](./catransform3dtranslate%28_,_,_,_%29.md)
  Translates `t` by `(tx, ty, tz)` and returns the result: `t` `= translate(tx, ty, tz) * t`.
- [func CATransform3DScale(CATransform3D, CGFloat, CGFloat, CGFloat) -> CATransform3D](./catransform3dscale%28_,_,_,_%29.md)
  Scales `t` by `(sx, sy, sz)` and returns the result: `t = scale(sx, sy, sz) * t`.
- [func CATransform3DRotate(CATransform3D, CGFloat, CGFloat, CGFloat, CGFloat) -> CATransform3D](./catransform3drotate%28_,_,_,_,_%29.md)
  Rotates `t` by `angle` radians about the vector `(x, y, z)` and returns the result.
### Inverting a Transform
- [func CATransform3DInvert(CATransform3D) -> CATransform3D](./catransform3dinvert%28_%29.md)
  Inverts `t` and returns the result.
### Determining Transform Properties
- [func CATransform3DIsAffine(CATransform3D) -> Bool](./catransform3disaffine%28_%29.md)
  Returns a Boolean value that indicates whether a transform can be exactly represented by an affine transform.
- [func CATransform3DIsIdentity(CATransform3D) -> Bool](./catransform3disidentity%28_%29.md)
  Returns a Boolean value that indicates whether the transform is the identity transform.
- [func CATransform3DEqualToTransform(CATransform3D, CATransform3D) -> Bool](./catransform3dequaltotransform%28_,_%29.md)
  Returns a Boolean value that indicates whether the two transforms are exactly equal.
### Converting to and from Core Graphics Affine Transforms
- [func CATransform3DMakeAffineTransform(CGAffineTransform) -> CATransform3D](./catransform3dmakeaffinetransform%28_%29.md)
  Returns a transform with the same effect as affine transform `m`.
- [func CATransform3DGetAffineTransform(CATransform3D) -> CGAffineTransform](./catransform3dgetaffinetransform%28_%29.md)
  Returns the affine transform represented by `t`.
### Data Types
- [struct CATransform3D](./catransform3d.md)
  The standard transform matrix used throughout Core Animation.
### Constants
- [let CATransform3DIdentity: CATransform3D](./catransform3didentity.md)
  The identity transform: `[1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/transforms)*