# simd

**Framework**: Accelerate

Perform computations on small vectors and matrices.

#### Overview

simd provides types and functions for small vector and matrix computations. The types include integer and floating-point vectors and matrices, and the functions provide basic arithmetic operations, element-wise mathematical operations, and geometric and linear algebra operations.

simd supports vectors containing up to 16 elements (for single-precision values) or 8 elements (for double-precision values), and matrices up to 4 x 4 elements in size. Other frameworks, such as [`vForce`](veclib/vforce.md), allow you to work with larger vectors.

## Topics

### Boolean Scalar Data Type
- [typealias simd_bool](../simd/simd_bool.md)
  A Boolean scalar value.
### Signed Integer Vectors
- [8-Bit Signed Integer Vectors](8-bit-signed-integer-vectors.md)
  Perform operations on vectors that contain signed 8-bit integer elements.
- [16-Bit Signed Integer Vectors](16-bit-signed-integer-vectors.md)
  Perform operations on vectors that contain signed 16-bit integer elements.
- [32-Bit Signed Integer Vectors](32-bit-signed-integer-vectors.md)
  Perform operations on vectors that contain signed 32-bit integer elements.
- [64-Bit Signed Integer Vectors](64-bit-signed-integer-vectors.md)
  Perform operations on vectors that contain signed 64-bit integer elements.
### Unsigned Integer Vectors
- [8-Bit Unsigned Integer Vectors](8-bit-unsigned-integer-vectors.md)
  Perform operations on vectors that contain unsigned 8-bit integer elements.
- [16-Bit Unsigned Integer Vectors](16-bit-unsigned-integer-vectors.md)
  Perform operations on vectors that contain unsigned 16-bit integer elements.
- [32-Bit Unsigned Integer Vectors](32-bit-unsigned-integer-vectors.md)
  Perform operations on vectors that contain unsigned 32-bit integer elements.
- [64-Bit Unsigned Integer Vectors](64-bit-unsigned-integer-vectors.md)
  Perform operations on vectors that contain unsigned 64-bit integer elements.
### Floating-Point Vectors
- [Working with Vectors](working-with-vectors.md)
  Use vectors to calculate geometric values, calculate dot products and cross products, and interpolate between values.
- [Half-precision floating-point vectors](half-precision-floating-point-vectors.md)
  Perform operations on vectors that contain half-precision floating-point elements.
- [Single-precision floating-point vectors](single-precision-floating-point-vectors.md)
  Perform operations on vectors that contain single-precision floating-point elements.
- [Double-precision floating-point vectors](double-precision-floating-point-vectors.md)
  Perform operations on vectors that contain double-precision floating-point elements.
### Matrices
- [Working with Matrices](working-with-matrices.md)
  Solve simultaneous equations and transform points in space.
- [Half-precision floating-point matrices](half-precision-floating-point-matrices.md)
  Perform operations on matrices that contain half-precision floating-point elements.
- [Single-precision floating-point matrices](single-precision-floating-point-matrices.md)
  Perform operations on matrices that contain single-precision floating-point elements.
- [Double-precision floating-point matrices](double-precision-floating-point-matrices.md)
  Perform operations on matrices that contain double-precision floating-point elements.
### Quaternions
- [Working with Quaternions](working-with-quaternions.md)
  Rotate points around the surface of a sphere, and interpolate between them.
- [Rotating a cube by transforming its vertices](rotating-a-cube-by-transforming-its-vertices.md)
  Rotate a cube through a series of keyframes using quaternion interpolation to transition between them.
- [struct simd_quatf](../simd/simd_quatf.md)
  A single-precision quaternion.
- [struct simd_quatd](../simd/simd_quatd.md)
  A double-precision quaternion.
### Constants
- [var SIMD_COMPILER_HAS_REQUIRED_FEATURES: Int32](../simd/simd_compiler_has_required_features.md)
- [var SIMD_LIBRARY_VERSION: Int32](../simd/simd_library_version.md)
### Macros
- [simd Macros](simd-macros.md)

## See Also

- [Working with Vectors](working-with-vectors.md)
  Use vectors to calculate geometric values, calculate dot products and cross products, and interpolate between values.
- [Working with Matrices](working-with-matrices.md)
  Solve simultaneous equations and transform points in space.
- [Working with Quaternions](working-with-quaternions.md)
  Rotate points around the surface of a sphere, and interpolate between them.
- [Rotating a cube by transforming its vertices](rotating-a-cube-by-transforming-its-vertices.md)
  Rotate a cube through a series of keyframes using quaternion interpolation to transition between them.
- [vForce](vforce-library.md)
  Perform transcendental and trigonometric functions on vectors of any length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/simd-library)*