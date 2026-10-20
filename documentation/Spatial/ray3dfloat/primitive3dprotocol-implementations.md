# Primitive3DProtocol Implementations

**Framework**: Spatial  
**Role**: API Collection

## Topics

### Instance Properties
- [var isFinite: Bool](./isfinite.md)
  A Boolean value that indicates whether all of the values of the ray are finite.
- [var isNaN: Bool](./isnan.md)
  A Boolean value that indicates whether all of the values of the ray are finite.
- [var isZero: Bool](./iszero.md)
  A Boolean value that indicates whether all of the values of the ray are zero.
### Instance Methods
- [func apply(Pose3DFloat)](./apply%28_%29.md)
  Applies a pose.
- [func applying(Pose3DFloat) -> Ray3DFloat](./applying%28_%29-3spgk.md)
  Returns a ray that’s transformed by the specified pose.
- [func applying(ProjectiveTransform3DFloat) -> Ray3DFloat](./applying%28_%29-6phxw.md)
  Returns a ray that’s transformed by the specified projective transform.
- [func applying(AffineTransform3DFloat) -> Ray3DFloat](./applying%28_%29-7miic.md)
  Returns a ray that’s transformed by the specified affine transform.
- [func unapplying(Pose3DFloat) -> Ray3DFloat](./unapplying%28_%29-2ouak.md)
  Returns a ray that’s transformed by the inverse of the specified pose.
- [func unapplying(ProjectiveTransform3DFloat) -> Ray3DFloat](./unapplying%28_%29-6pcxp.md)
  Returns a ray that’s transformed by the inverse of the specified projective transform.
- [func unapplying(AffineTransform3DFloat) -> Ray3DFloat](./unapplying%28_%29-9mbz3.md)
  Returns a ray that’s transformed by the inverse of the specified affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3dfloat/primitive3dprotocol-implementations)*