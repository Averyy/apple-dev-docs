# Worley Noise 2D

**Framework**: ShaderGraph  
**Kind**: subscript

A 2D Worley noise generator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

#### Parameter Description

- **`Texture Coordinates`**: The 2D coordinate at which the data is read for mapping a texture to a surface. The default uses the current UV coordinates, in which U is the horizontal axis and V is the vertical axis.
- **`Jitter`**: The amount to *jitter* or shift the center of each cell experiences. The default value is `1.0`. A smaller value creates a more regular pattern, and `0` creates perfect squares.

### Discussion

The `Worley Noise 2D` node procedurally generates nonuniform cellular regions. Creates a finite number of center points, and each region is a polygon that surrounds the points closest to each center point. Below is an example of a simple node graph that uses the `Worley Noise 2D` node to generate a black and white pattern procedurally:

![None](/images/ShaderGraph-Docs/WorleyNoise2dGraph.png)

Multiply the incoming texture coordinates with a constant float, which changes the frequency of the generated noise. A higher value corresponds to the pattern repeating more often. You then run the output through a convert node to change it to a black and white color value.
Below is an example of a simple node graph that uses the `Worley Noise 2D` node to generate a black and white pattern procedurally:

![None](/images/ShaderGraph-Docs/WorleyNoise2dMaterial.png)

## See Also

- [Ramp Horizontal](2d-procedural/ramp-horizontal.md)
  A left-to-right linear value ramp (gradient) generator.
- [Ramp Vertical](2d-procedural/ramp-vertical.md)
  A top-to-bottom linear value ramp (gradient) generator.
- [Ramp 4 Corners](2d-procedural/ramp-4-corners.md)
  A four-point linear value ramp (gradient) generator.
- [Split Horizontal](2d-procedural/split-horizontal.md)
  A left-to-right split matte, split at a specified U value.
- [Split Vertical](2d-procedural/split-vertical.md)
  A top-to-bottom split matte, split at a specified V value.
- [Noise 2D](2d-procedural/noise-2d.md)
  A 2D Perlin noise generator.
- [Cellular Noise 2D](2d-procedural/cellular-noise-2d.md)
  A 2D cellular noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-procedural/worley-noise-2d)*