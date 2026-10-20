# XOR (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Returns true if only one of the inputs is true.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

| Input | Type |
| --- | --- |
| `In 1` | Bool |
| `In 2` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Bool |

#### Discussion

This node mimics the logical `Xor` operator, as shown in the table below:

| In1 | In2 | Out |
| --- | --- | --- |
| True | True | False |
| True | False | True |
| False | True | True |
| False | False | False |

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
- [Not (RealityKit)](./not-%28realitykit%29.md)
  Returns !input.
- [Select (RealityKit)](./select-%28realitykit%29.md)
  Selects B if conditional is true, A if false.
- [Multiply Add 24 (RealityKit)](../realitykit/multiply-add-24-%28realitykit%29.md)
  Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result with 32-bit Z value added.
- [Multiply 24 (RealityKit)](../realitykit/multiply-24-%28realitykit%29.md)
  Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/logic/xor-(realitykit))*