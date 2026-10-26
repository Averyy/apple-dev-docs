# Spatial

**Framework**: Spatial  
**Kind**: module  
**Role**: Framework

Create and manipulate 3D mathematical primitives.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

#### Overview

The Spatial module is a lightweight 3D mathematical library that provides a simple API for working with 3D primitives. Much of its functionality is similar to the 2D geometry support in Core Graphics, but in three dimensions.

## Topics

### Data structures
- [struct Vector3D](./vector3d.md)
  A three-element vector.
- [struct Vector3DFloat](./vector3dfloat.md)
  A single-precision structure that defines a three-element vector
- [struct Axis3D](./axis3d.md)
  Constants that describe an axis.
### 2D primitives
- [struct Angle2D](./angle2d.md)
  A geometric angle with a value you access in either radians or degrees.
- [struct Angle2DFloat](./angle2dfloat.md)
  A single-precision geometric angle whose value you access in either radians or degrees.
### 3D primitives
- [struct Point3D](./point3d.md)
  A point in a 3D coordinate system.
- [struct Point3DFloat](./point3dfloat.md)
  A single-precision structure that contains a point in a three-dimensional coordinate system.
- [struct Size3D](./size3d.md)
  A size that describes width, height, and depth in a 3D coordinate system.
- [struct Size3DFloat](./size3dfloat.md)
  A single-precision structure that contains width, height, and depth values.
- [struct Rect3D](./rect3d.md)
  A rectangle in a 3D coordinate system.
- [struct Rect3DFloat](./rect3dfloat.md)
  A single-precision structure that contains the location and dimensions of a 3D rectangle.
- [struct Rotation3D](./rotation3d.md)
  A rotation in three dimensions.
- [struct Rotation3DFloat](./rotation3dfloat.md)
  A single-precision structure that represents a rotation in three dimensions.
- [struct RotationAxis3D](./rotationaxis3d.md)
  A 3D rotation axis.
- [struct RotationAxis3DFloat](./rotationaxis3dfloat.md)
  A 3D axis.
- [struct Pose3D](./pose3d.md)
  A structure that contains a 3D position and a 3D rotation.
- [struct Pose3DFloat](./pose3dfloat.md)
  A single-precision structure that contains a position and rotation.
- [struct ScaledPose3D](./scaledpose3d.md)
  A structure that contains a position, rotation, and scale.
- [struct ScaledPose3DFloat](./scaledpose3dfloat.md)
  A structure that contains a position, rotation, and scale.
- [struct SphericalCoordinates3D](./sphericalcoordinates3d.md)
  A structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct SphericalCoordinates3DFloat](./sphericalcoordinates3dfloat.md)
  A single-precision structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct Ray3D](./ray3d.md)
  A ray in a 3D coordinate system.
- [struct Ray3DFloat](./ray3dfloat.md)
  A single-precision structure that contains the origin and direction of a 3D ray.
### Affine and projective transforms
- [struct AffineTransform3D](./affinetransform3d.md)
  A 3D affine transformation matrix.
- [struct AffineTransform3DFloat](./affinetransform3dfloat.md)
- [struct ProjectiveTransform3D](./projectivetransform3d.md)
  A 3D projective transformation matrix.
- [struct ProjectiveTransform3DFloat](./projectivetransform3dfloat.md)
  A single-precision 3D projective transformation matrix.
### Converting between coordinate spaces
- [protocol CoordinateSpace3D](./coordinatespace3d.md)
  A type that represents a coordinate space which you can use to convert values to and from other coordinate spaces.
- [protocol CoordinateSpace3DFloat](./coordinatespace3dfloat.md)
- [protocol CoordinateSpaceValue3D](./coordinatespacevalue3d.md)
  An opaque value which can be resolved to a concrete value in a `CoordinateSpace3D`
- [protocol ProjectiveTransformable3D](./projectivetransformable3d.md)
- [protocol ProjectiveTransformable3DFloat](./projectivetransformable3dfloat.md)
- [struct WorldReferenceCoordinateSpace](./worldreferencecoordinatespace.md)
  A coordinate space that represents a world reference point.
### Applying trigonometric functions
- [func cos(Angle2D) -> Double](./cos%28_%29-609v4.md)
- [func cos(Angle2DFloat) -> Float](./cos%28_%29-79fxe.md)
- [func cosh(Angle2D) -> Double](./cosh%28_%29-6cg6v.md)
- [func cosh(Angle2DFloat) -> Float](./cosh%28_%29-9mmhn.md)
- [func sin(Angle2DFloat) -> Float](./sin%28_%29-46su7.md)
- [func sin(Angle2D) -> Double](./sin%28_%29-5tddt.md)
- [func sinh(Angle2D) -> Double](./sinh%28_%29-4m7ds.md)
- [func sinh(Angle2DFloat) -> Float](./sinh%28_%29-8kigy.md)
- [func tan(Angle2D) -> Double](./tan%28_%29-1sjgu.md)
- [func tan(Angle2DFloat) -> Float](./tan%28_%29-9x99s.md)
- [func tanh(Angle2D) -> Double](./tanh%28_%29-1f341.md)
- [func tanh(Angle2DFloat) -> Float](./tanh%28_%29-5yozs.md)
### Protocols
- [protocol Primitive3D](./primitive3d.md)
  A set of methods common to Spatial primitives.
- [protocol Rotatable3D](./rotatable3d.md)
  A set of methods that defines the interface to rotate Spatial entities.
- [protocol Scalable3D](./scalable3d.md)
  A set of methods that defines the interface to scale Spatial entities.
- [protocol Shearable3D](./shearable3d.md)
  A set of methods that defines the interface to shear Spatial entities.
- [protocol Translatable3D](./translatable3d.md)
  A set of methods that defines the interface to translate Spatial entities.
- [protocol Volumetric](./volumetric.md)
  A set of methods for working with Spatial primitives with volume.
- [protocol ClampableWithinRectProtocol](./clampablewithinrectprotocol.md)
  A set of methods that defines the interface for Spatial entities that can be clamped to a volume.
- [protocol Primitive3DProtocol](./primitive3dprotocol.md)
  A set of methods common to Spatial primitives.
- [protocol Rotatable3DProtocol](./rotatable3dprotocol.md)
  A set of methods that defines the interface for Spatial entities that can rotate.
- [protocol Scalable3DProtocol](./scalable3dprotocol.md)
  A set of methods that defines the interface for Spatial entities that can scale.
- [protocol Shearable3DProtocol](./shearable3dprotocol.md)
  A set of methods that defines the interface for Spatial entities that can shear.
- [protocol SpatialTypeProtocol](./spatialtypeprotocol.md)
- [protocol Transform3DProtocol](./transform3dprotocol.md)
  A set of methods that are common to transforms.
- [protocol Translatable3DProtocol](./translatable3dprotocol.md)
  A set of methods that defines the interface for Spatial entities that can translate.
- [protocol VolumetricProtocol](./volumetricprotocol.md)
  A set of methods for working with Spatial primitives with volume.
### Macros
- [Macros & Global Variables](./spatial-macros.md)
- [SPDefaultToleranceFloat](./spdefaulttolerancefloat.md)
### Structures
- [struct EulerAnglesFloat](./euleranglesfloat.md)
### Enumerations
- [enum AxisWithFactorsFloat](./axiswithfactorsfloat.md)
  The axis of a shear transform.
### Variables
- [SPRotation3DFloatIdentity](./rotation3dfloat/identity.md)
  A single-precision structure that represents a rotation in three dimensions.
- [SPRotationAxis3DFloatZero](./rotationaxis3dfloat/zero.md)
  A 3D axis.
- [SPAffineTransform3DFloatIdentity](./spaffinetransform3dfloatidentity.md)
- [SPAffineTransform3DFloatInvalid](./spaffinetransform3dfloatinvalid.md)
- [SPAffineTransform3DIdentity](./spaffinetransform3didentity.md)
  The identity affine transform.
- [SPAngleFloatZero](./spanglefloatzero.md)
  A single-precision geometric angle whose value you access in either radians or degrees.
- [SPPoint3DFloatInfinity](./sppoint3dfloatinfinity.md)
  A single-precision structure that contains a point in a three-dimensional coordinate system.
- [SPPoint3DFloatZero](./sppoint3dfloatzero.md)
  A single-precision structure that contains a point in a three-dimensional coordinate system.
- [SPPose3DFloatIdentity](./sppose3dfloatidentity.md)
  A single-precision structure that contains a position and rotation.
- [SPPose3DFloatInvalid](./sppose3dfloatinvalid.md)
  A single-precision structure that contains a position and rotation.
- [SPProjectiveTransform3DFloatIdentity](./spprojectivetransform3dfloatidentity.md)
  A single-precision 3D projective transformation matrix.
- [SPProjectiveTransform3DFloatInvalid](./spprojectivetransform3dfloatinvalid.md)
  A single-precision 3D projective transformation matrix.
- [SPProjectiveTransform3DIdentity](./spprojectivetransform3didentity.md)
  The identity projective transform.
- [SPRay3DFloatInfinity](./spray3dfloatinfinity.md)
- [SPRay3DFloatZero](./spray3dfloatzero.md)
- [SPRect3DFloatInfinity](./sprect3dfloatinfinity.md)
  A single-precision structure that contains the location and dimensions of a 3D rectangle.
- [SPRect3DFloatNull](./sprect3dfloatnull.md)
  A single-precision structure that contains the location and dimensions of a 3D rectangle.
- [SPRect3DFloatZero](./sprect3dfloatzero.md)
  A single-precision structure that contains the location and dimensions of a 3D rectangle.
- [SPRotation3DFloatInvalid](./sprotation3dfloatinvalid.md)
  A single-precision structure that represents a rotation in three dimensions.
- [SPScaledPose3DFloatIdentity](./spscaledpose3dfloatidentity.md)
  A structure that contains a position, rotation, and scale.
- [SPScaledPose3DFloatInvalid](./spscaledpose3dfloatinvalid.md)
  A structure that contains a position, rotation, and scale.
- [SPSize3DFloatInfinity](./spsize3dfloatinfinity.md)
  A single-precision structure that contains width, height, and depth values.
- [SPSize3DFloatInvalid](./spsize3dfloatinvalid.md)
  A single-precision structure that contains width, height, and depth values.
- [SPSize3DFloatZero](./spsize3dfloatzero.md)
  A single-precision structure that contains width, height, and depth values.
- [SPVector3DFloatInfinity](./spvector3dfloatinfinity.md)
  A single-precision structure that defines a three-element vector
- [SPVector3DFloatZero](./spvector3dfloatzero.md)
  A single-precision structure that defines a three-element vector
### Functions
- [SPAffineTransform3DFloatMakeWith4x3Matrix](./affinetransform3dfloat/init%28_%29-5ajh4.md)
- [SPAffineTransform3DFloatMakeWithTruncatedProjective](./affinetransform3dfloat/init%28truncating%29-1jfno.md)
- [SPAffineTransform3DFloatMakeWithTruncated4x4Matrix](./affinetransform3dfloat/init%28truncating%29-8jfn6.md)
- [SPAffineTransform3DFloatIsInvertible](./affinetransform3dfloat/isinvertible.md)
- [SPAffineTransform3DFloatGet3x3Matrix](./affinetransform3dfloat/matrix3x3.md)
- [SPAffineTransform3DFloatGet4x4Matrix](./affinetransform3dfloat/matrix4x4.md)
- [SPAffineTransform3DFloatGetScale](./affinetransform3dfloat/scale.md)
- [SPAngleFloatMakeWithRadians](./angle2dfloat/init%28radians%29-4uwyj.md)
- [SPPoint3DFloatRotateByQuaternionAroundPoint](./point3dfloat/rotated%28by,around%29-1ejmw.md)
- [SPPoint3DFloatRotateAroundPoint](./point3dfloat/rotated%28by,around%29-5xwwi.md)
- [SPProjectiveTransform3DFloatMakeWith4x4Matrix](./projectivetransform3dfloat/init%28_%29-56itt.md)
  Returns a new transform from the specified 4 x 4 matrix.
- [SPProjectiveTransform3DFloatMakeWithAffine](./projectivetransform3dfloat/init%28_%29-6ffxa.md)
  Returns a new transform from the specified affine transform.
- [SPProjectiveTransform3DFloatMakeWithRightHandPerspective](./projectivetransform3dfloat/init%28fovy,aspectratio,nearz,farz%29.md)
- [SPProjectiveTransform3DFloatMakeWithRightHandPerspective](./projectivetransform3dfloat/init%28fovy,aspectratio,nearz,farz,reversez%29.md)
- [SPProjectiveTransform3DFloatMakeFromTangents](./projectivetransform3dfloat/init%28lefttangent,righttangent,toptangent,bottomtangent,nearz,farz,reversez%29.md)
- [SPProjectiveTransform3DFloatIs3DFloatProjection](./projectivetransform3dfloat/is3dfloatprojection%28%29.md)
- [SPProjectiveTransform3DFloatIsAffine](./projectivetransform3dfloat/isaffine.md)
- [SPProjectiveTransform3DFloatIsInvertible](./projectivetransform3dfloat/isinvertible.md)
- [SPRay3DFloatIntersectsSphere](./ray3dfloat/intersects%28sphereorigin,sphereradius%29.md)
- [SPRect3DFloatGetCenter](./rect3dfloat/center.md)
- [SPRect3DFloatMakeAtCenter](./rect3dfloat/init%28center,size%29-e8la.md)
  Creates a rectangle at the specified center with the specified size.
- [SPRect3DFloatMakeAtOrigin](./rect3dfloat/init%28origin,size%29-8tqau.md)
- [SPRect3DFloatInset](./rect3dfloat/inset%28by%29.md)
- [SPRect3DFloatIntegral](./rect3dfloat/integral.md)
- [SPRect3DFloatIntersectsRect](./rect3dfloat/intersects%28_%29.md)
- [SPRect3DFloatIsEmpty](./rect3dfloat/isempty.md)
- [SPRect3DFloatIsNull](./rect3dfloat/isnull.md)
- [SPRect3DFloatGetMaximum](./rect3dfloat/max.md)
- [SPRect3DFloatGetMinimum](./rect3dfloat/min.md)
- [SPRect3DFloatRotateAroundPoint](./rect3dfloat/rotated%28by,around%29-1g90c.md)
- [SPRect3DFloatRotateByQuaternionAroundPoint](./rect3dfloat/rotated%28by,around%29-9yw64.md)
- [SPRect3DFloatStandardize](./rect3dfloat/standardized.md)
  Returns a rectangle with a positive width and height.
- [SPRotation3DFloatGetEulerAngles](./rotation3dfloat/eulerangles%28order%29.md)
- [SPRotation3DFloatMakeWithEulerAngles](./rotation3dfloat/init%28eulerangles%29.md)
- [SPRotation3DFloatInverse](./rotation3dfloat/inverse.md)
- [SPRotation3DFloatIsIdentity](./rotation3dfloat/isidentity.md)
- [SPRotation3DFloatSwing](./rotation3dfloat/swing%28twistaxis%29.md)
- [SPRotation3DFloatTwist](./rotation3dfloat/twist%28twistaxis%29.md)
- [SPAffineTransform3DConcatenation](./spaffinetransform3dconcatenation.md)
- [SPAffineTransform3DFloatAlmostEqualToTransform](./spaffinetransform3dfloatalmostequaltotransform-5b3so.md)
- [SPAffineTransform3DFloatAlmostEqualToTransform](./spaffinetransform3dfloatalmostequaltotransform-5lv5i.md)
- [SPAffineTransform3DFloatChangeBasis](./spaffinetransform3dfloatchangebasis.md)
- [SPAffineTransform3DFloatConcatenation](./spaffinetransform3dfloatconcatenation.md)
- [SPAffineTransform3DFloatFlip](./spaffinetransform3dfloatflip.md)
- [SPAffineTransform3DFloatGetRotation](./spaffinetransform3dfloatgetrotation.md)
- [SPAffineTransform3DFloatGetTranslation](./spaffinetransform3dfloatgettranslation.md)
- [SPAffineTransform3DFloatInverted](./spaffinetransform3dfloatinverted.md)
- [SPAffineTransform3DFloatIsIdentity](./spaffinetransform3dfloatisidentity.md)
- [SPAffineTransform3DFloatIsRectilinear](./spaffinetransform3dfloatisrectilinear.md)
- [SPAffineTransform3DFloatIsTranslation](./spaffinetransform3dfloatistranslation.md)
- [SPAffineTransform3DFloatIsUniform](./spaffinetransform3dfloatisuniform.md)
- [SPAffineTransform3DFloatIsUniformOverDimensions](./spaffinetransform3dfloatisuniformoverdimensions.md)
- [SPAffineTransform3DFloatIsValid](./spaffinetransform3dfloatisvalid.md)
- [SPAffineTransform3DFloatMake](./spaffinetransform3dfloatmake-7vsey.md)
- [SPAffineTransform3DFloatMake](./spaffinetransform3dfloatmake-9aze8.md)
- [SPAffineTransform3DFloatMakeRotation](./spaffinetransform3dfloatmakerotation.md)
- [SPAffineTransform3DFloatMakeScale](./spaffinetransform3dfloatmakescale.md)
- [SPAffineTransform3DFloatMakeShear](./spaffinetransform3dfloatmakeshear.md)
- [SPAffineTransform3DFloatMakeTranslation](./spaffinetransform3dfloatmaketranslation.md)
- [SPAffineTransform3DFloatMakeWithPose](./spaffinetransform3dfloatmakewithpose.md)
- [SPAffineTransform3DFloatMakeWithScaledPose](./spaffinetransform3dfloatmakewithscaledpose.md)
- [SPAffineTransform3DFloatRotate](./spaffinetransform3dfloatrotate.md)
- [SPAffineTransform3DFloatRotateByQuaternion](./spaffinetransform3dfloatrotatebyquaternion.md)
- [SPAffineTransform3DFloatScaleBy](./spaffinetransform3dfloatscaleby.md)
- [SPAffineTransform3DFloatScaleBySize](./spaffinetransform3dfloatscalebysize.md)
- [SPAffineTransform3DFloatScaleUniform](./spaffinetransform3dfloatscaleuniform.md)
- [SPAffineTransform3DFloatSetTranslation](./spaffinetransform3dfloatsettranslation.md)
- [SPAffineTransform3DFloatShear](./spaffinetransform3dfloatshear.md)
- [SPAffineTransform3DFloatTranslate](./spaffinetransform3dfloattranslate.md)
- [SPAffineTransform3DIsIdentity](./spaffinetransform3disidentity.md)
- [SPAffineTransform3DIsRectilinear](./spaffinetransform3disrectilinear.md)
- [SPAffineTransform3DIsTranslation](./spaffinetransform3distranslation.md)
- [SPAffineTransform3DIsUniform](./spaffinetransform3disuniform.md)
- [SPAffineTransform3DMake](./spaffinetransform3dmake-5pau5.md)
- [SPAffineTransform3DMakeRotation](./spaffinetransform3dmakerotation.md)
- [SPAffineTransform3DMakeScale](./spaffinetransform3dmakescale.md)
- [SPAffineTransform3DMakeTranslation](./spaffinetransform3dmaketranslation-9czpj.md)
- [SPAngleFloatAcos](./spanglefloatacos.md)
- [SPAngleFloatAcosh](./spanglefloatacosh.md)
- [SPAngleFloatAsin](./spanglefloatasin.md)
- [SPAngleFloatAsinh](./spanglefloatasinh.md)
- [SPAngleFloatAtan](./spanglefloatatan.md)
- [SPAngleFloatAtan2](./spanglefloatatan2.md)
- [SPAngleFloatAtanh](./spanglefloatatanh.md)
- [SPAngleFloatCos](./spanglefloatcos.md)
- [SPAngleFloatCosh](./spanglefloatcosh.md)
- [SPAngleFloatEqualToAngle](./spanglefloatequaltoangle.md)
  Returns @p true if both rotation angles are equal.
- [SPAngleFloatGetDegrees](./spanglefloatgetdegrees.md)
- [SPAngleFloatMake](./spanglefloatmake.md)
- [SPAngleFloatMakeWithDegrees](./spanglefloatmakewithdegrees.md)
- [SPAngleFloatNegate](./spanglefloatnegate.md)
- [SPAngleFloatNormalize](./spanglefloatnormalize.md)
- [SPAngleFloatSin](./spanglefloatsin.md)
- [SPAngleFloatSinh](./spanglefloatsinh.md)
- [SPAngleFloatTan](./spanglefloattan.md)
- [SPAngleFloatTanh](./spanglefloattanh.md)
- [SPAngleMake](./spanglemake.md)
- [SPPoint3DClampToRect](./sppoint3dclamptorect.md)
- [SPPoint3DFloatAlmostEqualToPoint](./sppoint3dfloatalmostequaltopoint-6aviz.md)
- [SPPoint3DFloatAlmostEqualToPoint](./sppoint3dfloatalmostequaltopoint-8lazd.md)
- [SPPoint3DFloatApplyAffineTransform](./sppoint3dfloatapplyaffinetransform.md)
- [SPPoint3DFloatApplyPose](./sppoint3dfloatapplypose.md)
- [SPPoint3DFloatApplyProjectiveTransform](./sppoint3dfloatapplyprojectivetransform.md)
- [SPPoint3DFloatApplyScaledPose](./sppoint3dfloatapplyscaledpose.md)
- [SPPoint3DFloatClampToRect](./sppoint3dfloatclamptorect.md)
- [SPPoint3DFloatDistanceToPoint](./sppoint3dfloatdistancetopoint.md)
- [SPPoint3DFloatEqualToPoint](./sppoint3dfloatequaltopoint.md)
  Returns @p true if both points are equal.
- [SPPoint3DFloatGetPackedVector](./sppoint3dfloatgetpackedvector.md)
- [SPPoint3DFloatGetVector](./sppoint3dfloatgetvector.md)
- [SPPoint3DFloatIsFinite](./sppoint3dfloatisfinite.md)
- [SPPoint3DFloatIsNaN](./sppoint3dfloatisnan.md)
- [SPPoint3DFloatIsZero](./sppoint3dfloatiszero.md)
- [SPPoint3DFloatMake](./sppoint3dfloatmake-15os1.md)
- [SPPoint3DFloatMake](./sppoint3dfloatmake-ik8n.md)
- [SPPoint3DFloatMakeWithPackedVector](./sppoint3dfloatmakewithpackedvector.md)
- [SPPoint3DFloatMakeWithSize](./sppoint3dfloatmakewithsize.md)
- [SPPoint3DFloatMakeWithSphericalCoordinates](./sppoint3dfloatmakewithsphericalcoordinates.md)
- [SPPoint3DFloatMakeWithVector](./sppoint3dfloatmakewithvector-3j0i4.md)
- [SPPoint3DFloatMakeWithVector](./sppoint3dfloatmakewithvector-3kq7r.md)
- [SPPoint3DFloatRotate](./sppoint3dfloatrotate.md)
- [SPPoint3DFloatRotateByQuaternion](./sppoint3dfloatrotatebyquaternion.md)
- [SPPoint3DFloatTranslate](./sppoint3dfloattranslate.md)
- [SPPoint3DFloatUnapplyAffineTransform](./sppoint3dfloatunapplyaffinetransform.md)
- [SPPoint3DFloatUnapplyPose](./sppoint3dfloatunapplypose.md)
- [SPPoint3DFloatUnapplyProjectiveTransform](./sppoint3dfloatunapplyprojectivetransform.md)
- [SPPoint3DFloatUnapplyScaledPose](./sppoint3dfloatunapplyscaledpose.md)
- [SPPoint3DGetPackedVector](./sppoint3dgetpackedvector.md)
- [SPPoint3DMake](./sppoint3dmake-2g23y.md)
- [SPPoint3DMake](./sppoint3dmake-55fjd.md)
- [SPPoint3DMakeWithPackedVector](./sppoint3dmakewithpackedvector.md)
- [SPPose3DFloatAlmostEqualToPose](./sppose3dfloatalmostequaltopose-17q2l.md)
- [SPPose3DFloatAlmostEqualToPose](./sppose3dfloatalmostequaltopose-5t5q.md)
- [SPPose3DFloatConcatenation](./sppose3dfloatconcatenation.md)
- [SPPose3DFloatEqualToPose](./sppose3dfloatequaltopose.md)
  Returns @p true if both rays are equal.
- [SPPose3DFloatFlip](./sppose3dfloatflip.md)
- [SPPose3DFloatGet4x4Matrix](./sppose3dfloatget4x4matrix.md)
- [SPPose3DFloatGetInverse](./sppose3dfloatgetinverse.md)
- [SPPose3DFloatIsIdentity](./sppose3dfloatisidentity.md)
- [SPPose3DFloatIsValid](./sppose3dfloatisvalid.md)
- [SPPose3DFloatMake](./sppose3dfloatmake-2rx9m.md)
- [SPPose3DFloatMake](./sppose3dfloatmake-6wx8e.md)
- [SPPose3DFloatMakeLookAt](./sppose3dfloatmakelookat-3sv3j.md)
- [SPPose3DFloatMakeLookAt](./sppose3dfloatmakelookat-5v9ru.md)
- [SPPose3DFloatMakeLookAt](./sppose3dfloatmakelookat-8dre6.md)
- [SPPose3DFloatMakeWith4x4Matrix](./sppose3dfloatmakewith4x4matrix.md)
- [SPPose3DFloatMakeWithAffineTransform](./sppose3dfloatmakewithaffinetransform.md)
- [SPPose3DFloatMakeWithProjectiveTransform](./sppose3dfloatmakewithprojectivetransform.md)
- [SPPose3DFloatMakeWithVector](./sppose3dfloatmakewithvector.md)
- [SPPose3DFloatRotate](./sppose3dfloatrotate.md)
- [SPPose3DFloatRotateByQuaternion](./sppose3dfloatrotatebyquaternion.md)
- [SPPose3DFloatTranslate](./sppose3dfloattranslate.md)
- [SPPose3DMake](./sppose3dmake-2l1sq.md)
- [SPPose3DMake](./sppose3dmake-3yjxa.md)
- [SPProjectiveTransform3DConcatenation](./spprojectivetransform3dconcatenation.md)
  Returns a projective transformation matrix constructed by concatenating two existing Projective transforms.
- [SPProjectiveTransform3DFloatAlmostEqualToTransform](./spprojectivetransform3dfloatalmostequaltotransform-29vcb.md)
- [SPProjectiveTransform3DFloatAlmostEqualToTransform](./spprojectivetransform3dfloatalmostequaltotransform-6ab39.md)
- [SPProjectiveTransform3DFloatConcatenation](./spprojectivetransform3dfloatconcatenation.md)
  Returns a projective transformation matrix constructed by concatenating two existing Projective transforms.
- [SPProjectiveTransform3DFloatFlip](./spprojectivetransform3dfloatflip.md)
- [SPProjectiveTransform3DFloatGetRotation](./spprojectivetransform3dfloatgetrotation.md)
- [SPProjectiveTransform3DFloatGetScale](./spprojectivetransform3dfloatgetscale.md)
- [SPProjectiveTransform3DFloatGetTranslation](./spprojectivetransform3dfloatgettranslation.md)
- [SPProjectiveTransform3DFloatInverted](./spprojectivetransform3dfloatinverted.md)
- [SPProjectiveTransform3DFloatIsIdentity](./spprojectivetransform3dfloatisidentity.md)
- [SPProjectiveTransform3DFloatIsRectilinear](./spprojectivetransform3dfloatisrectilinear.md)
- [SPProjectiveTransform3DFloatIsTranslation](./spprojectivetransform3dfloatistranslation.md)
- [SPProjectiveTransform3DFloatIsUniform](./spprojectivetransform3dfloatisuniform.md)
- [SPProjectiveTransform3DFloatIsUniformOverDimensions](./spprojectivetransform3dfloatisuniformoverdimensions.md)
- [SPProjectiveTransform3DFloatIsValid](./spprojectivetransform3dfloatisvalid.md)
- [SPProjectiveTransform3DFloatMake](./spprojectivetransform3dfloatmake-1o5dw.md)
- [SPProjectiveTransform3DFloatMake](./spprojectivetransform3dfloatmake-4yoh8.md)
- [SPProjectiveTransform3DFloatMakeRotation](./spprojectivetransform3dfloatmakerotation.md)
  Returns a new rotation transform.
- [SPProjectiveTransform3DFloatMakeScale](./spprojectivetransform3dfloatmakescale.md)
  Returns a new scale transform.
- [SPProjectiveTransform3DFloatMakeShear](./spprojectivetransform3dfloatmakeshear.md)
- [SPProjectiveTransform3DFloatMakeTranslation](./spprojectivetransform3dfloatmaketranslation.md)
  Returns a new translate transform.
- [SPProjectiveTransform3DFloatMakeWithPose](./spprojectivetransform3dfloatmakewithpose.md)
- [SPProjectiveTransform3DFloatMakeWithScaledPose](./spprojectivetransform3dfloatmakewithscaledpose.md)
- [SPProjectiveTransform3DFloatRotate](./spprojectivetransform3dfloatrotate.md)
- [SPProjectiveTransform3DFloatRotateByQuaternion](./spprojectivetransform3dfloatrotatebyquaternion.md)
- [SPProjectiveTransform3DFloatScaleBy](./spprojectivetransform3dfloatscaleby.md)
- [SPProjectiveTransform3DFloatScaleBySize](./spprojectivetransform3dfloatscalebysize.md)
- [SPProjectiveTransform3DFloatScaleUniform](./spprojectivetransform3dfloatscaleuniform.md)
- [SPProjectiveTransform3DFloatSetTranslation](./spprojectivetransform3dfloatsettranslation.md)
- [SPProjectiveTransform3DFloatShear](./spprojectivetransform3dfloatshear.md)
- [SPProjectiveTransform3DFloatTranslate](./spprojectivetransform3dfloattranslate.md)
- [SPProjectiveTransform3DIsIdentity](./spprojectivetransform3disidentity.md)
- [SPProjectiveTransform3DIsRectilinear](./spprojectivetransform3disrectilinear.md)
- [SPProjectiveTransform3DIsTranslation](./spprojectivetransform3distranslation.md)
- [SPProjectiveTransform3DIsUniform](./spprojectivetransform3disuniform.md)
- [SPProjectiveTransform3DMake](./spprojectivetransform3dmake-5qdj3.md)
- [SPProjectiveTransform3DMakeRotation](./spprojectivetransform3dmakerotation.md)
  Returns a new rotation transform.
- [SPProjectiveTransform3DMakeScale](./spprojectivetransform3dmakescale.md)
  Returns a new scale transform.
- [SPProjectiveTransform3DMakeTranslation](./spprojectivetransform3dmaketranslation-7l5gj.md)
  Returns a new translate transform.
- [SPRay3DFloatApplyAffineTransform](./spray3dfloatapplyaffinetransform.md)
- [SPRay3DFloatApplyPose](./spray3dfloatapplypose.md)
- [SPRay3DFloatApplyProjectiveTransform](./spray3dfloatapplyprojectivetransform.md)
- [SPRay3DFloatApplyScaledPose](./spray3dfloatapplyscaledpose.md)
- [SPRay3DFloatEqualToRay](./spray3dfloatequaltoray.md)
  Returns @p true if both rays are equal.
- [SPRay3DFloatIntersectsRect](./spray3dfloatintersectsrect.md)
- [SPRay3DFloatIsFinite](./spray3dfloatisfinite.md)
- [SPRay3DFloatIsNaN](./spray3dfloatisnan.md)
- [SPRay3DFloatIsZero](./spray3dfloatiszero.md)
- [SPRay3DFloatMake](./spray3dfloatmake-5yjgm.md)
- [SPRay3DFloatMake](./spray3dfloatmake-8d6wq.md)
- [SPRay3DFloatMakeWithVector](./spray3dfloatmakewithvector.md)
- [SPRay3DFloatRotate](./spray3dfloatrotate.md)
- [SPRay3DFloatRotateAroundPoint](./spray3dfloatrotatearoundpoint.md)
- [SPRay3DFloatRotateByQuaternion](./spray3dfloatrotatebyquaternion.md)
- [SPRay3DFloatRotateByQuaternionAroundPoint](./spray3dfloatrotatebyquaternionaroundpoint.md)
- [SPRay3DFloatTranslate](./spray3dfloattranslate.md)
- [SPRay3DFloatUnapplyAffineTransform](./spray3dfloatunapplyaffinetransform.md)
- [SPRay3DFloatUnapplyPose](./spray3dfloatunapplypose.md)
- [SPRay3DFloatUnapplyProjectiveTransform](./spray3dfloatunapplyprojectivetransform.md)
- [SPRay3DFloatUnapplyScaledPose](./spray3dfloatunapplyscaledpose.md)
- [SPRay3DMake](./spray3dmake-3296l.md)
- [SPRay3DMake](./spray3dmake-9x6y7.md)
- [SPRect3DFloatApplyAffineTransform](./sprect3dfloatapplyaffinetransform.md)
- [SPRect3DFloatApplyPose](./sprect3dfloatapplypose.md)
- [SPRect3DFloatApplyProjectiveTransform](./sprect3dfloatapplyprojectivetransform.md)
- [SPRect3DFloatApplyScaledPose](./sprect3dfloatapplyscaledpose.md)
- [SPRect3DFloatContainsAnyPoint](./sprect3dfloatcontainsanypoint.md)
- [SPRect3DFloatContainsPoint](./sprect3dfloatcontainspoint.md)
- [SPRect3DFloatContainsRect](./sprect3dfloatcontainsrect.md)
- [SPRect3DFloatEqualToRect](./sprect3dfloatequaltorect.md)
  Returns @p true if both rectangles are equal.
- [SPRect3DFloatGetCornerPoints](./sprect3dfloatgetcornerpoints.md)
- [SPRect3DFloatIntersection](./sprect3dfloatintersection.md)
- [SPRect3DFloatIsFinite](./sprect3dfloatisfinite.md)
- [SPRect3DFloatIsNaN](./sprect3dfloatisnan.md)
- [SPRect3DFloatIsZero](./sprect3dfloatiszero.md)
- [SPRect3DFloatMake](./sprect3dfloatmake.md)
- [SPRect3DFloatMakeAtCenterWithVector](./sprect3dfloatmakeatcenterwithvector-70afe.md)
- [SPRect3DFloatMakeAtCenterWithVector](./sprect3dfloatmakeatcenterwithvector-9o2lm.md)
- [SPRect3DFloatMakeAtOriginWithVector](./sprect3dfloatmakeatoriginwithvector-6uu22.md)
- [SPRect3DFloatMakeAtOriginWithVector](./sprect3dfloatmakeatoriginwithvector-72c27.md)
- [SPRect3DFloatMakeBoundingFromPoints](./sprect3dfloatmakeboundingfrompoints.md)
- [SPRect3DFloatRotate](./sprect3dfloatrotate.md)
- [SPRect3DFloatRotateByQuaternion](./sprect3dfloatrotatebyquaternion.md)
- [SPRect3DFloatScaleBy](./sprect3dfloatscaleby.md)
- [SPRect3DFloatScaleBySize](./sprect3dfloatscalebysize.md)
- [SPRect3DFloatScaleUniform](./sprect3dfloatscaleuniform.md)
- [SPRect3DFloatShear](./sprect3dfloatshear.md)
- [SPRect3DFloatTranslate](./sprect3dfloattranslate.md)
- [SPRect3DFloatUnapplyAffineTransform](./sprect3dfloatunapplyaffinetransform.md)
- [SPRect3DFloatUnapplyPose](./sprect3dfloatunapplypose.md)
- [SPRect3DFloatUnapplyProjectiveTransform](./sprect3dfloatunapplyprojectivetransform.md)
- [SPRect3DFloatUnapplyScaledPose](./sprect3dfloatunapplyscaledpose.md)
- [SPRect3DFloatUnion](./sprect3dfloatunion.md)
- [SPRect3DMake](./sprect3dmake.md)
- [SPRotation3DFloatAlmostEqualToRotation](./sprotation3dfloatalmostequaltorotation-2krut.md)
- [SPRotation3DFloatAlmostEqualToRotation](./sprotation3dfloatalmostequaltorotation-9s06b.md)
- [SPRotation3DFloatEqualToRotation](./sprotation3dfloatequaltorotation.md)
  Returns @p true if both rotations are equal.
- [SPRotation3DFloatGetAngle](./sprotation3dfloatgetangle.md)
- [SPRotation3DFloatGetAxis](./sprotation3dfloatgetaxis.md)
- [SPRotation3DFloatGetPackedVector](./sprotation3dfloatgetpackedvector.md)
- [SPRotation3DFloatGetQuaternion](./sprotation3dfloatgetquaternion.md)
- [SPRotation3DFloatIsValid](./sprotation3dfloatisvalid.md)
- [SPRotation3DFloatMake](./sprotation3dfloatmake-2fg8z.md)
- [SPRotation3DFloatMake](./sprotation3dfloatmake-3pbt1.md)
- [SPRotation3DFloatMakeLookAt](./sprotation3dfloatmakelookat-2pvrg.md)
- [SPRotation3DFloatMakeLookAt](./sprotation3dfloatmakelookat-3zivr.md)
- [SPRotation3DFloatMakeLookAt](./sprotation3dfloatmakelookat-4d35y.md)
- [SPRotation3DFloatMakeWithPackedVector](./sprotation3dfloatmakewithpackedvector.md)
- [SPRotation3DFloatMakeWithQuaternion](./sprotation3dfloatmakewithquaternion.md)
- [SPRotation3DFloatSetAngle](./sprotation3dfloatsetangle.md)
- [SPRotation3DFloatSetAxis](./sprotation3dfloatsetaxis.md)
- [SPRotation3DFloatSlerp](./sprotation3dfloatslerp.md)
- [SPRotation3DFloatSlerpLongest](./sprotation3dfloatslerplongest.md)
- [SPRotation3DFloatSpline](./sprotation3dfloatspline.md)
- [SPRotation3DGetPackedVector](./sprotation3dgetpackedvector.md)
- [SPRotation3DMake](./sprotation3dmake-35x05.md)
- [SPRotation3DMakeWithPackedVector](./sprotation3dmakewithpackedvector.md)
- [SPRotationAxis3DFloatEqualToRotationAxis](./sprotationaxis3dfloatequaltorotationaxis.md)
  Returns @p true if both rotation axes are equal.
- [SPRotationAxis3DFloatGetPackedVector](./sprotationaxis3dfloatgetpackedvector.md)
- [SPRotationAxis3DFloatGetVector](./sprotationaxis3dfloatgetvector.md)
- [SPRotationAxis3DFloatIsZero](./sprotationaxis3dfloatiszero.md)
- [SPRotationAxis3DFloatMake](./sprotationaxis3dfloatmake-4qq2.md)
- [SPRotationAxis3DFloatMake](./sprotationaxis3dfloatmake-5v6mj.md)
- [SPRotationAxis3DFloatMakeWithPackedVector](./sprotationaxis3dfloatmakewithpackedvector.md)
- [SPRotationAxis3DFloatMakeWithVector](./sprotationaxis3dfloatmakewithvector-1xodl.md)
- [SPRotationAxis3DFloatMakeWithVector](./sprotationaxis3dfloatmakewithvector-5rswz.md)
- [SPRotationAxis3DGetPackedVector](./sprotationaxis3dgetpackedvector.md)
- [SPRotationAxis3DMake](./sprotationaxis3dmake-3diey.md)
- [SPRotationAxis3DMake](./sprotationaxis3dmake-6y99b.md)
- [SPRotationAxis3DMakeWithPackedVector](./sprotationaxis3dmakewithpackedvector.md)
- [SPScaledPose3DFloatAlmostEqualToPose](./spscaledpose3dfloatalmostequaltopose-3vziw.md)
- [SPScaledPose3DFloatAlmostEqualToPose](./spscaledpose3dfloatalmostequaltopose-8m831.md)
- [SPScaledPose3DFloatConcatenation](./spscaledpose3dfloatconcatenation-7o06.md)
- [SPScaledPose3DFloatConcatenation](./spscaledpose3dfloatconcatenation-8f0ta.md)
- [SPScaledPose3DFloatConcatenation](./spscaledpose3dfloatconcatenation-9dkwv.md)
- [SPScaledPose3DFloatEqualToPose](./spscaledpose3dfloatequaltopose.md)
  Returns @p true if both scaled poses are equal.
- [SPScaledPose3DFloatFlip](./spscaledpose3dfloatflip.md)
- [SPScaledPose3DFloatGet4x4Matrix](./spscaledpose3dfloatget4x4matrix.md)
- [SPScaledPose3DFloatGetInverse](./spscaledpose3dfloatgetinverse.md)
- [SPScaledPose3DFloatIsIdentity](./spscaledpose3dfloatisidentity.md)
- [SPScaledPose3DFloatIsValid](./spscaledpose3dfloatisvalid.md)
- [SPScaledPose3DFloatMake](./spscaledpose3dfloatmake-9ihr7.md)
- [SPScaledPose3DFloatMake](./spscaledpose3dfloatmake-9ju0j.md)
- [SPScaledPose3DFloatMake](./spscaledpose3dfloatmake-9nz6v.md)
- [SPScaledPose3DFloatMakeLookAt](./spscaledpose3dfloatmakelookat-4kx9a.md)
- [SPScaledPose3DFloatMakeLookAt](./spscaledpose3dfloatmakelookat-61u16.md)
- [SPScaledPose3DFloatMakeLookAt](./spscaledpose3dfloatmakelookat-625ym.md)
- [SPScaledPose3DFloatMakeWith4x4Matrix](./spscaledpose3dfloatmakewith4x4matrix.md)
- [SPScaledPose3DFloatMakeWithAffineTransform](./spscaledpose3dfloatmakewithaffinetransform.md)
- [SPScaledPose3DFloatMakeWithProjectiveTransform](./spscaledpose3dfloatmakewithprojectivetransform.md)
- [SPScaledPose3DFloatMakeWithVector](./spscaledpose3dfloatmakewithvector.md)
- [SPScaledPose3DFloatRotate](./spscaledpose3dfloatrotate.md)
- [SPScaledPose3DFloatRotateByQuaternion](./spscaledpose3dfloatrotatebyquaternion.md)
- [SPScaledPose3DFloatTranslate](./spscaledpose3dfloattranslate.md)
- [SPScaledPose3DMake](./spscaledpose3dmake-88h4b.md)
- [SPSize3DFloatApplyAffineTransform](./spsize3dfloatapplyaffinetransform.md)
- [SPSize3DFloatApplyPose](./spsize3dfloatapplypose.md)
- [SPSize3DFloatApplyProjectiveTransform](./spsize3dfloatapplyprojectivetransform.md)
- [SPSize3DFloatApplyScaledPose](./spsize3dfloatapplyscaledpose.md)
- [SPSize3DFloatContainsAnyPoint](./spsize3dfloatcontainsanypoint.md)
- [SPSize3DFloatContainsPoint](./spsize3dfloatcontainspoint.md)
- [SPSize3DFloatContainsSize](./spsize3dfloatcontainssize.md)
- [SPSize3DFloatEqualToSize](./spsize3dfloatequaltosize.md)
  Returns @p true if both sizes are equal.
- [SPSize3DFloatGetPackedVector](./spsize3dfloatgetpackedvector.md)
- [SPSize3DFloatGetVector](./spsize3dfloatgetvector.md)
- [SPSize3DFloatIntersection](./spsize3dfloatintersection.md)
- [SPSize3DFloatIsFinite](./spsize3dfloatisfinite.md)
- [SPSize3DFloatIsNaN](./spsize3dfloatisnan.md)
- [SPSize3DFloatIsValid](./spsize3dfloatisvalid.md)
- [SPSize3DFloatIsZero](./spsize3dfloatiszero.md)
- [SPSize3DFloatMake](./spsize3dfloatmake-391r4.md)
- [SPSize3DFloatMake](./spsize3dfloatmake-9onwa.md)
- [SPSize3DFloatMakeWithPackedVector](./spsize3dfloatmakewithpackedvector.md)
- [SPSize3DFloatMakeWithPoint](./spsize3dfloatmakewithpoint.md)
- [SPSize3DFloatMakeWithVector](./spsize3dfloatmakewithvector-4vmp5.md)
- [SPSize3DFloatMakeWithVector](./spsize3dfloatmakewithvector-7j8ez.md)
- [SPSize3DFloatRotate](./spsize3dfloatrotate.md)
- [SPSize3DFloatRotateByQuaternion](./spsize3dfloatrotatebyquaternion.md)
- [SPSize3DFloatScaleBy](./spsize3dfloatscaleby.md)
- [SPSize3DFloatScaleBySize](./spsize3dfloatscalebysize.md)
- [SPSize3DFloatScaleUniform](./spsize3dfloatscaleuniform.md)
- [SPSize3DFloatShear](./spsize3dfloatshear.md)
- [SPSize3DFloatUnapplyAffineTransform](./spsize3dfloatunapplyaffinetransform.md)
- [SPSize3DFloatUnapplyPose](./spsize3dfloatunapplypose.md)
- [SPSize3DFloatUnapplyProjectiveTransform](./spsize3dfloatunapplyprojectivetransform.md)
- [SPSize3DFloatUnapplyScaledPose](./spsize3dfloatunapplyscaledpose.md)
- [SPSize3DFloatUnion](./spsize3dfloatunion.md)
- [SPSize3DGetPackedVector](./spsize3dgetpackedvector.md)
- [SPSize3DMake](./spsize3dmake-7u1jt.md)
- [SPSize3DMake](./spsize3dmake-ft60.md)
- [SPSize3DMakeWithPackedVector](./spsize3dmakewithpackedvector.md)
- [SPSphericalCoordinates3DFloatGetPackedVector](./spsphericalcoordinates3dfloatgetpackedvector.md)
- [SPSphericalCoordinates3DFloatMake](./spsphericalcoordinates3dfloatmake-hl8u.md)
- [SPSphericalCoordinates3DFloatMakeWithCartesianPoint](./spsphericalcoordinates3dfloatmakewithcartesianpoint.md)
- [SPSphericalCoordinates3DFloatMakeWithCartesianVector](./spsphericalcoordinates3dfloatmakewithcartesianvector-5vuvy.md)
- [SPSphericalCoordinates3DFloatMakeWithCartesianVector](./spsphericalcoordinates3dfloatmakewithcartesianvector-7mbkj.md)
- [SPSphericalCoordinates3DFloatMakeWithPackedVector](./spsphericalcoordinates3dfloatmakewithpackedvector.md)
- [SPSphericalCoordinates3DGetPackedVector](./spsphericalcoordinates3dgetpackedvector.md)
- [SPSphericalCoordinates3DMake](./spsphericalcoordinates3dmake-9dqz0.md)
- [SPSphericalCoordinates3DMakeWithPackedVector](./spsphericalcoordinates3dmakewithpackedvector.md)
- [SPVector3DFloatApplyAffineTransform](./spvector3dfloatapplyaffinetransform.md)
- [SPVector3DFloatApplyPose](./spvector3dfloatapplypose.md)
- [SPVector3DFloatApplyProjectiveTransform](./spvector3dfloatapplyprojectivetransform.md)
- [SPVector3DFloatApplyScaledPose](./spvector3dfloatapplyscaledpose.md)
- [SPVector3DFloatCrossProduct](./spvector3dfloatcrossproduct.md)
- [SPVector3DFloatDotProduct](./spvector3dfloatdotproduct.md)
- [SPVector3DFloatEqualToVector](./spvector3dfloatequaltovector.md)
  Returns @p true if both points are equal.
- [SPVector3DFloatGetPackedVector](./spvector3dfloatgetpackedvector.md)
- [SPVector3DFloatIsFinite](./spvector3dfloatisfinite.md)
- [SPVector3DFloatIsNaN](./spvector3dfloatisnan.md)
- [SPVector3DFloatIsZero](./spvector3dfloatiszero.md)
- [SPVector3DFloatLength](./spvector3dfloatlength.md)
- [SPVector3DFloatLengthSquared](./spvector3dfloatlengthsquared.md)
- [SPVector3DFloatLerp](./spvector3dfloatlerp.md)
- [SPVector3DFloatMake](./spvector3dfloatmake-345rz.md)
- [SPVector3DFloatMake](./spvector3dfloatmake-41xdv.md)
- [SPVector3DFloatMakeWithPackedVector](./spvector3dfloatmakewithpackedvector.md)
- [SPVector3DFloatMakeWithPoint](./spvector3dfloatmakewithpoint.md)
- [SPVector3DFloatMakeWithRotationAxis](./spvector3dfloatmakewithrotationaxis.md)
- [SPVector3DFloatMakeWithSize](./spvector3dfloatmakewithsize.md)
- [SPVector3DFloatMakeWithSphericalCoordinates](./spvector3dfloatmakewithsphericalcoordinates.md)
- [SPVector3DFloatMakeWithVector](./spvector3dfloatmakewithvector.md)
- [SPVector3DFloatNormalize](./spvector3dfloatnormalize.md)
- [SPVector3DFloatProject](./spvector3dfloatproject.md)
- [SPVector3DFloatReflect](./spvector3dfloatreflect.md)
- [SPVector3DFloatRotate](./spvector3dfloatrotate.md)
- [SPVector3DFloatRotateByQuaternion](./spvector3dfloatrotatebyquaternion.md)
- [SPVector3DFloatRotationToVector](./spvector3dfloatrotationtovector.md)
- [SPVector3DFloatScaleBy](./spvector3dfloatscaleby.md)
- [SPVector3DFloatScaleBySize](./spvector3dfloatscalebysize.md)
- [SPVector3DFloatScaleUniform](./spvector3dfloatscaleuniform.md)
- [SPVector3DFloatShear](./spvector3dfloatshear.md)
- [SPVector3DFloatSmoothstep](./spvector3dfloatsmoothstep.md)
- [SPVector3DFloatUnapplyAffineTransform](./spvector3dfloatunapplyaffinetransform.md)
- [SPVector3DFloatUnapplyPose](./spvector3dfloatunapplypose.md)
- [SPVector3DFloatUnapplyProjectiveTransform](./spvector3dfloatunapplyprojectivetransform.md)
- [SPVector3DFloatUnapplyScaledPose](./spvector3dfloatunapplyscaledpose.md)
- [SPVector3DGetPackedVector](./spvector3dgetpackedvector.md)
- [SPVector3DLerp](./spvector3dlerp.md)
- [SPVector3DMake](./spvector3dmake-60yox.md)
- [SPVector3DMake](./spvector3dmake-6biur.md)
- [SPVector3DMakeWithPackedVector](./spvector3dmakewithpackedvector.md)
- [SPVector3DSmoothstep](./spvector3dsmoothstep.md)
- [SPSphericalCoordinates3DFloatMake](./sphericalcoordinates3dfloat/init%28radius,inclination,azimuth%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Spatial)*