# Select (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Selects B if conditional is true, A if false.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

**Select (half)**:

| Input | Type |
| --- | --- |
| `A` | Half |
| `B` | Half |
| `C` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Select (integer)**:

| Input | Type |
| --- | --- |
| `A` | Int32 |
| `B` | Int32 |
| `C` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Int32 |

**Select (float)**:

| Input | Type |
| --- | --- |
| `A` | Float |
| `B` | Float |
| `C` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Float |

## See Also

### Nodes
- [If Greater](./if-greater.md)
  Outputs True Result or False Result depending on whether value1 > value2.
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
- [Multiply Add 24 (RealityKit)](../realitykit/multiply-add-24-%28realitykit%29.md)
  Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result with 32-bit Z value added.
- [Multiply 24 (RealityKit)](../realitykit/multiply-24-%28realitykit%29.md)
  Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/logic/select-(realitykit))*