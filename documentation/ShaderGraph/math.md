# Math

**Framework**: ShaderGraph  
**Kind**: dictionary

Perform a wide variety of mathematical and transformative operations on data values.

#### Overview

Include math nodes in your graph when you want to perform typical mathematical operations on data values. A wide range of nodes are available, supporting basic arithmetic, trigonometry, logs, exponents, dot and cross products, and more. Some nodes operate on specific data types of values but most operate on a wide range of data types, including numbers, colors, and vectors.

## Topics

### Nodes
- [Add](math/add.md)
  Adds two values.
- [Subtract](math/subtract.md)
  Subtracts two values.
- [Multiply](math/multiply.md)
  Multiplies two values.
- [Divide](math/divide.md)
  Divides two values.
- [Modulo](math/modulo.md)
  Outputs the remaining fraction after dividing the input by a value and subtracting the integer portion.
- [Abs](math/abs.md)
  Outputs the per-channel absolute value of the input.
- [Floor](math/floor.md)
  Outputs the nearest integer value, per-channel, less than or equal to the incoming values.
- [Ceiling](math/ceiling.md)
  Outputs the nearest integer value, per-channel, greater than or equal to the incoming values.
- [Power](math/power.md)
  Raises the incoming value to an exponent.
- [Sin](math/sin.md)
  The sine of the incoming value in radians.
- [Cos](math/cos.md)
  The cosine of the incoming value in radians.
- [Tan](math/tan.md)
  The tangent of the incoming value in radians.
- [Asin](math/asin.md)
  The arcsine of the incoming value in radians.
- [Acos](math/acos.md)
  The arccosine of the incoming value in radians.
- [Atan2](math/atan2.md)
  The arctangent of the expression (iny/inx) in radians.
- [Square Root](math/square-root.md)
  The square root of the incoming value.
- [Natural Log](math/natural-log.md)
  The natural log of the input.
- [Exp](math/exp.md)
  Outputs ‘e’ to the power of the input.
- [Sign](math/sign.md)
  The per-channel sign of the input value: -1 for negative, +1 for positive, 0 for zero.
- [Clamp](math/clamp.md)
  Clamps the input per-channel to a specified range.
- [Min](math/min.md)
  Outputs the minimum of two incoming values.
- [Max](math/max.md)
  Outputs the maximum of two incoming values.
- [Normalize](math/normalize.md)
  Outputs a normalized vector.
- [Magnitude](math/magnitude.md)
  Outputs the float magnitude of a vector.
- [Dot Product](math/dot-product.md)
  Outputs the dot product of two vectors.
- [Cross Product](math/cross-product.md)
  Calculates the cross product vector of 2 input vectors.
- [Transform Point](math/transform-point.md)
  Transforms a coordinate from one space to another.
- [Transform Vector](math/transform-vector.md)
  Transforms a vector3 from one space to another.
- [Transform Normal](math/transform-normal.md)
  Transforms a normal from one space to another.
- [Transform Matrix](math/transform-matrix.md)
  Transforms a vector by a matrix.
- [Transpose](math/transpose.md)
  Outputs the tranpose of a matrix.
- [Determinant](math/determinant.md)
  Outputs the float determinant of a matrix.
- [Invert Matrix](math/invert-matrix.md)
  Outputs the inverse of a matrix.
- [Rotate 2D](math/rotate-2d.md)
  Rotates a Vector2 (Float) about the origin in 2D.
- [Rotate 3D](math/rotate-3d.md)
  Rotates a Vector3 (Float) about a specified unit axis vector.
- [Place 2D](math/place-2d.md)
  Transforms UV texture coordinates for 2D texture placement.
- [Round](math/round.md)
  Rounds to the nearest integer value, per-channel.
- [Safe Power](math/safe-power.md)
  Raises the incoming value to an exponent and assigns the sign of the base to the output.
- [Normal Map](math/normal-map.md)
  Transforms a normal vector from object or tangent space into world space.
- [Fractional (RealityKit)](math/fractional-(realitykit).md)
  Returns the fractional part of a floating point number.
- [One Minus (RealityKit)](math/one-minus-(realitykit).md)
  Outputs one minus the input
- [Normal Map Decode](math/normal-map-decode.md)
  Remaps a normal’s value from [0,1] to [-1,1] by applying 2x-1.

## See Also

- [2D-Procedural](2d-procedural.md)
  Generate 2D gradients, noise, and other patterns programmatically for your material.
- [2D-Texture](2d-texture.md)
  Load and configure 2D texture files.
- [3D-Procedural](3d-procedural.md)
  Generate 3D noise patterns programmatically for your material.
- [3D-Texture](3d-texture.md)
  Project multiple 2D images onto a surface to create a 3D texture.
- [Adjustment](adjustment.md)
  Modify or convert values, or ranges of values, from one form to another.
- [Application](application.md)
  Get system values such as the current time or the direction of the up vector.
- [Compositing](compositing.md)
  Generate a single output from the combination of multiple data values.
- [Data](data.md)
  Convert data values to different formats, or manipulate individual elements within a data structure.
- [Geometric](geometric.md)
  Access scene geometry while your graph runs.
- [Logic](logic.md)
  Perform Boolean operations and other logical comparisons on data values.
- [Material](material.md)
  Encapsulate a set of shader graph nodes into a single module.
- [Organization](organization.md)
  Modify the visual flow of data within your graph without changing any values.
- [Procedural](procedural.md)
  Add a constant number, vector, matrix, color, string, or other value to your graph.
- [RealityKit](realitykit.md)
  Add RealityKit surfaces or textures to your material and access and manipulate scene geometry.
- [Surface](surface.md)
  Generate a MaterialX preview surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/math)*