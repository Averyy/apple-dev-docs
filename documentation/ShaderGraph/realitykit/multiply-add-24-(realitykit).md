# Multiply Add 24 (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result with 32-bit Z value added.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Overview

X and Y are 32-bit integers but only the low 24 bits perform the multiplication

#### Parameter Types

| Input | Type |
| --- | --- |
| `X` | Int32 |
| `Y` | Int32 |
| `Z` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Int32 |

## See Also

### Nodes
- [If Greater](../logic/if-greater.md)
  Outputs True Result or False Result depending on whether value1 > value2.
- [If Greater Or Equal](../logic/if-greater-or-equal.md)
  Outputs True Result or False Result depending on whether value1 >= value2.
- [If Equal](../logic/if-equal.md)
  Outputs True Result or False Result depending on whether value1 == value2.
- [Switch](../logic/switch.md)
  Outputs the value from one of ten input streams, according to a selector .
- [And (RealityKit)](../logic/and-%28realitykit%29.md)
  Boolean operation in1 && in2.
- [Or (RealityKit)](../logic/or-%28realitykit%29.md)
  Boolean operation in1 || in2.
- [XOR (RealityKit)](../logic/xor-%28realitykit%29.md)
  Returns true if only one of the inputs is true.
- [Not (RealityKit)](../logic/not-%28realitykit%29.md)
  Returns !input.
- [Select (RealityKit)](../logic/select-%28realitykit%29.md)
  Selects B if conditional is true, A if false.
- [Multiply 24 (RealityKit)](./multiply-24-%28realitykit%29.md)
  Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit/multiply-add-24-(realitykit))*