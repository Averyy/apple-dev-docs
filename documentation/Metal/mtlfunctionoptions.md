# MTLFunctionOptions

**Framework**: Metal  
**Kind**: struct

Options that define how Metal creates the function object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLFunctionOptions
```

## Topics

### Creating Function Options
- [init(rawValue: UInt)](mtlfunctionoptions/init(rawvalue:).md)
  Creates a new function options structure from a raw value.
### Function Option Values
- [static var compileToBinary: MTLFunctionOptions](mtlfunctionoptions/compiletobinary.md)
  An option that tells Metal to compile the function to a binary format for dynamic linking.
### Type Properties
- [static var failOnBinaryArchiveMiss: MTLFunctionOptions](mtlfunctionoptions/failonbinaryarchivemiss.md)
- [static var pipelineIndependent: MTLFunctionOptions](mtlfunctionoptions/pipelineindependent.md)
- [static var storeFunctionInMetalPipelinesScript: MTLFunctionOptions](mtlfunctionoptions/storefunctioninmetalpipelinesscript.md)
- [static var storeFunctionInMetalScript: MTLFunctionOptions](mtlfunctionoptions/storefunctioninmetalscript.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var device: any MTLDevice](mtlfunction/device.md)
  The device object that created the shader function.
- [var label: String?](mtlfunction/label.md)
  A string that identifies the shader function.
- [var functionType: MTLFunctionType](mtlfunction/functiontype.md)
  The shader function’s type.
- [var name: String](mtlfunction/name.md)
  The function’s name.
- [enum MTLFunctionType](mtlfunctiontype.md)
  The type of a top-level Metal Shading Language (MSL) function.
- [var options: MTLFunctionOptions](mtlfunction/options.md)
  The options that Metal used to compile this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionoptions)*