# MTL4BinaryFunctionOptions

**Framework**: Metal  
**Kind**: struct

Options for configuring the creation of binary functions.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct MTL4BinaryFunctionOptions
```

## Topics

### Initializers
- [init(rawValue: UInt)](mtl4binaryfunctionoptions/init(rawvalue:).md)
### Type Properties
- [static var pipelineIndependent: MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions/pipelineindependent.md)
  Compiles the function to have its function handles return a constant MTLResourceID across all pipeline states. The function needs to be linked to the pipeline that will use this function.

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

- [Metal Libraries](metal-libraries.md)
  Compile and manage Metal libraries from the command line.
- [Metal Dynamic Libraries](metal-dynamic-libraries.md)
  Create a single Metal library containing reusable code to reduce library size and avoid repeated shader compilation at runtime.
- [Metal Binary Archives](metal-binary-archives.md)
  Distribute precompiled GPU-specific binaries as part of your app to avoid runtime compilation of Metal shaders.
- [protocol MTL4Compiler](mtl4compiler.md)
  A abstraction for a pipeline state and shader function compiler.
- [class MTL4CompilerDescriptor](mtl4compilerdescriptor.md)
  Groups together properties for creating a compiler context.
- [class MTL4CompilerTaskOptions](mtl4compilertaskoptions.md)
- [enum MTL4CompilerTaskStatus](mtl4compilertaskstatus.md)
  Represents the status of a compiler task.
- [protocol MTL4Archive](mtl4archive.md)
  A read-only container that stores pipeline states from a shader compiler.
- [protocol MTL4BinaryFunction](mtl4binaryfunction.md)
  Represents a binary function.
- [class MTL4BinaryFunctionDescriptor](mtl4binaryfunctiondescriptor.md)
  Base interface for other function-derived interfaces.
- [class MTL4BinaryFunctionReflection](mtl4binaryfunctionreflection.md)
  Represents reflection information for a binary function.
- [class MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md)
  Groups together properties to drive the dynamic linking process of a pipeline stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4binaryfunctionoptions)*