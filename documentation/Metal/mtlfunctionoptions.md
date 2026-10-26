# MTLFunctionOptions

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

Options that define how Metal compiles a GPU function.

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

```c
enum MTLFunctionOptions : NSUInteger;
```

## Topics

### Function compilation options
- [static var failOnBinaryArchiveMiss: MTLFunctionOptions](./mtlfunctionoptions/failonbinaryarchivemiss.md)
  An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [static var compileToBinary: MTLFunctionOptions](./mtlfunctionoptions/compiletobinary.md)
  An option that instructs the compiler to generate a binary format for dynamic linking.
- [static var pipelineIndependent: MTLFunctionOptions](./mtlfunctionoptions/pipelineindependent.md)
  An option that generates the same function handle across all pipeline states that link a function, which lets you share function tables across pipeline states.
- [static var storeFunctionInMetalPipelinesScript: MTLFunctionOptions](./mtlfunctionoptions/storefunctioninmetalpipelinesscript.md)
  An option that instructs the compiler to store function information for inspecting binary archives.
- [static var storeFunctionInMetalScript: MTLFunctionOptions](./mtlfunctionoptions/storefunctioninmetalscript.md)
  An option that instructs the compiler to store function information for inspecting binary archives.
- [MTLFunctionOptionNone](./mtlfunctionoptions/mtlfunctionoptionnone.md)
  A sentinel value that represents an empty set of options, which is the default behavior for creating functions.
### Swift support
- [init(rawValue: UInt)](./mtlfunctionoptions/init%28rawvalue%29.md)
  Creates a new function options structure from a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Identifying shader functions
- [var device: any MTLDevice](./mtlfunction/device.md)
  The device object that created the shader function.
- [var label: String?](./mtlfunction/label.md)
  A string that identifies the shader function.
- [var functionType: MTLFunctionType](./mtlfunction/functiontype.md)
  The shader function’s type.
- [var name: String](./mtlfunction/name.md)
  The function’s name.
- [enum MTLFunctionType](./mtlfunctiontype.md)
  The type of a top-level Metal Shading Language (MSL) function.
- [var options: MTLFunctionOptions](./mtlfunction/options.md)
  The options that Metal used to compile this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionoptions)*