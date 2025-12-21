# MTL4BinaryFunction

**Framework**: Metal  
**Kind**: protocol

Represents a binary function.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTL4BinaryFunction : NSObjectProtocol, Sendable
```

#### Overview

A binary function is a shader that you precompile from Metal IR to GPU machine code.

## Topics

### Instance Properties
- [var functionType: MTLFunctionType](mtl4binaryfunction/functiontype.md)
  Describes the type of this binary function.
- [var name: String?](mtl4binaryfunction/name.md)
  Obtains the optional name of this binary function.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Metal libraries](metal-libraries.md)
  Compile and manage Metal libraries from the command line.
- [Metal dynamic libraries](metal-dynamic-libraries.md)
  Create a single Metal library containing reusable code to reduce library size and avoid repeated shader compilation at runtime.
- [Metal binary archives](metal-binary-archives.md)
  Distribute precompiled GPU-specific binaries as part of your app to avoid runtime compilation of Metal shaders.
- [protocol MTL4Compiler](mtl4compiler.md)
  A abstraction for a pipeline state and shader function compiler.
- [class MTL4CompilerDescriptor](mtl4compilerdescriptor.md)
  Groups together properties for creating a compiler context.
- [class MTL4CompilerTaskOptions](mtl4compilertaskoptions.md)
  The configuration options that control the behavior of a compilation task for a Metal 4 compiler instance.
- [enum MTL4CompilerTaskStatus](mtl4compilertaskstatus.md)
  Represents the status of a compiler task.
- [protocol MTL4Archive](mtl4archive.md)
  A read-only container that stores pipeline states from a shader compiler.
- [class MTL4BinaryFunctionDescriptor](mtl4binaryfunctiondescriptor.md)
  Base interface for other function-derived interfaces.
- [struct MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md)
  Options for configuring the creation of binary functions.
- [class MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md)
  Groups together properties to drive the dynamic linking process of a pipeline stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4binaryfunction)*