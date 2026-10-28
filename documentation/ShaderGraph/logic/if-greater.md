# If Greater

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Outputs True Result or False Result depending on whether value1 > value2.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**If Greater (float)**:

| Input | Type |
| --- | --- |
| `Value1` | Float |
| `Value2` | Float |
| `True Result` | Float |
| `False Result` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

**If Greater (vector2h integer)**:

| Input | Type |
| --- | --- |
| `Value1` | Int32 |
| `Value2` | Int32 |
| `In 1` | Vector2h |
| `In 2` | Vector2h |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**If Greater (Float integer)**:

| Input | Type |
| --- | --- |
| `Value1` | Int32 |
| `Value2` | Int32 |
| `True Result` | Float |
| `False Result` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

**If Greater (vector3h)**:

| Input | Type |
| --- | --- |
| `Value1` | Float |
| `Value2` | Float |
| `In 1` | Vector3h |
| `In 2` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**If Greater (vector2f integer)**:

| Input | Type |
| --- | --- |
| `Value1` | Int32 |
| `Value2` | Int32 |
| `True Result` | Vector2f |
| `False Result` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**If Greater (vector4f)**:

| Input | Type |
| --- | --- |
| `Value1` | Float |
| `Value2` | Float |
| `True Result` | Vector4f |
| `False Result` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**If Greater (vector4h)**:

| Input | Type |
| --- | --- |
| `Value1` | Float |
| `Value2` | Float |
| `In 1` | Vector4h |
| `In 2` | Vector4h |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**If Greater (vector4h integer)**:

| Input | Type |
| --- | --- |
| `Value1` | Int32 |
| `Value2` | Int32 |
| `In 1` | Vector4h |
| `In 2` | Vector4h |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**If Greater (color3f)**:

| Input | Type |
| --- | --- |
| `Value1` | Float |
| `Value2` | Float |
| `True Result` | Color3 |
| `False Result` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**If Greater (vector4f integer)**:

| Input | Type |
| --- | --- |
| `Value1` | Int32 |
| `Value2` | Int32 |
| `True Result` | Vector4f |
| `False Result` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**If Greater (half integer)**:

| Input | Type |
| --- | --- |
| `Value1` | Int32 |
| `Value2` | Int32 |
| `In 1` | Half |
| `In 2` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

**If Greater (vector3f)**:

| Input | Type |
| --- | --- |
| `Value1` | Float |
| `Value2` | Float |
| `True Result` | Vector3f |
| `False Result` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**If Greater (vector3h integer)**:

| Input | Type |
| --- | --- |
| `Value1` | Int32 |
| `Value2` | Int32 |
| `In 1` | Vector3h |
| `In 2` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**If Greater (color4f integer)**:

| Input | Type |
| --- | --- |
| `Value1` | Int32 |
| `Value2` | Int32 |
| `True Result` | Color4 |
| `False Result` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**If Greater (half)**:

| Input | Type |
| --- | --- |
| `Value1` | Half |
| `Value2` | Half |
| `In 1` | Half |
| `In 2` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

**If Greater (vector2f)**:

| Input | Type |
| --- | --- |
| `Value1` | Float |
| `Value2` | Float |
| `True Result` | Vector2f |
| `False Result` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**If Greater (color4f)**:

| Input | Type |
| --- | --- |
| `Value1` | Float |
| `Value2` | Float |
| `True Result` | Color4 |
| `False Result` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**If Greater (color3f integer)**:

| Input | Type |
| --- | --- |
| `Value1` | Int32 |
| `Value2` | Int32 |
| `True Result` | Color3 |
| `False Result` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**If Greater (vector3f integer)**:

| Input | Type |
| --- | --- |
| `Value1` | Int32 |
| `Value2` | Int32 |
| `True Result` | Vector3f |
| `False Result` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**If Greater (vector2h)**:

| Input | Type |
| --- | --- |
| `Value1` | Float |
| `Value2` | Float |
| `In 1` | Vector2h |
| `In 2` | Vector2h |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

## Parameter descriptions

- **`Value1`**: The first value to compare.
- **`Value2`**: The second value to compare.
- **`True Result`**: The output of the node if the `Value1` input parameter is greater than the `Value2` input parameter.
- **`False Result`**: The output of the node if the `Value1` input parameter isn’t greater than the `Value2` input parameter.

## See Also

### Nodes
- [If Greater Or Equal](./if-greater-or-equal.md)
  Outputs True Result or False Result depending on whether value1 >= value2.
- [If Equal](./if-equal.md)
  Outputs True Result or False Result depending on whether value1 == value2.
- [Switch](./switch.md)
  Outputs the value from one of ten input streams, according to a selector .
- [And (RealityKit)](./and-%28realitykit%29.md)
  Boolean operation in1 && in2.
- [Or (RealityKit)](./or-%28realitykit%29.md)
  Boolean operation in1 || in2.
- [XOR (RealityKit)](./xor-%28realitykit%29.md)
  Returns true if only one of the inputs is true.
- [Not (RealityKit)](./not-%28realitykit%29.md)
  Returns !input.
- [Select (RealityKit)](./select-%28realitykit%29.md)
  Selects B if conditional is true, A if false.
- [Multiply Add 24 (RealityKit)](../realitykit/multiply-add-24-%28realitykit%29.md)
  Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result with 32-bit Z value added.
- [Multiply 24 (RealityKit)](../realitykit/multiply-24-%28realitykit%29.md)
  Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/logic/if-greater)*