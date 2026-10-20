# Fractal Noise 3D

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Zero-centered 3D fractal noise created by summing several octaves of 3D Perlin noise.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

**Fractal Noise 3D (float)**:

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Fractal Noise 3D (color3f)**:

| Input | Type |
| --- | --- |
| `Amplitude` | Vector3f |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Fractal Noise 3D (color4f)**:

| Input | Type |
| --- | --- |
| `Amplitude` | Vector4f |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Fractal Noise 3D (vector2f)**:

| Input | Type |
| --- | --- |
| `Amplitude` | Vector2f |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Fractal Noise 3D (vector3f)**:

| Input | Type |
| --- | --- |
| `Amplitude` | Vector3f |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Fractal Noise 3D (vector2f FA)**:

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Fractal Noise 3D (vector3f FA)**:

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Fractal Noise 3D (vector4f FA)**:

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Fractal Noise 3D (color3f FA)**:

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Fractal Noise 3D (color4f FA)**:

| Input | Type |
| --- | --- |
| `Amplitude` | Float |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Fractal Noise 3D (vector4f)**:

| Input | Type |
| --- | --- |
| `Amplitude` | Vector4f |
| `Octaves` | Int32 |
| `Lacunarity` | Float |
| `Diminish` | Float |
| `Position` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

#### Parameter descriptions

- **`Amplitude`**: The intensity of the generated noise. The higher the amplitude, the more pronounced the variations of the noise pattern.
- **`Octaves`**: The number of layers of 3D Perlin noise that the node sums together. The default value is 3.
- **`Lacunarity`**: The exponential scale between each octave. This value determines how different each successive octave or layer of Perlin noise is from one another. The default value is `2.0`
- **`Diminish`**: The rate that the amplitude of each successive octave is decreased. Maintain the value for this parameter in the range of `0.0-1.0`. The default value is `0.5`.
- **`Position`**: The 3D coordinates at which the data is read in order to map the texture onto a surface. The default is to use the current 3D object-space coordinates.

#### Discussion

The Fractal Noise node produces its output by summing up multiple layers or octaves of 3D Perlin noise. The more octaves in the fractal noise, the finer the detail of the noise. Each successive octave differs from the previous; the `Lacunarity` and `Diminish` parameters determine the difference. *Lacunarity* refers to the difference in frequency between each octavex. As this value increases, the resulting fractal noise becomes more uneven and less smooth. *Diminish* refers to how the amplitude changes between octaves. A value of `1` indicates no change to the  amplitude. As the value decreases, the amplitude from octave to octave decreases more quickly. Below is an example of a simple node graph that uses the Fractal Noise 3D node to generate a black and white pattern procedurally:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/FractalNoise3DGraph.png)

Multiply the incoming position with a constant float. The float changes the frequency of the generated noise to a higher number that corresponds with the pattern repeating more often. Below, the resulting texture applies to a cube with various values for each parameter. All values are the default, unless specified under the image.

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Fractal3DOctaves1.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Fractal3DOctaves3.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Fractal3DOctaves5.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Fractal3DLacunarity1.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Fractal3DLacunarity2.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Fractal3DLacunarity5.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Fractal3DDiminish0.2.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Fractal3DDiminish0.5.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Fractal3DDiminish1.png)

## See Also

### Nodes
- [Noise 3D](./noise-3d.md)
  A 3D Perlin noise generator.
- [Cellular Noise 3D](./cellular-noise-3d.md)
  A 3D cellular noise generator.
- [Worley Noise 3D](./worley-noise-3d.md)
  A 3D Worley noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/3d-procedural/fractal-noise-3d)*