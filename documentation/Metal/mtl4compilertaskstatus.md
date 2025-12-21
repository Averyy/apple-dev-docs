# MTL4CompilerTaskStatus

**Framework**: Metal  
**Kind**: enum

Represents the status of a compiler task.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum MTL4CompilerTaskStatus
```

## Topics

### Enumeration Cases
- [MTL4CompilerTaskStatus.compiling](mtl4compilertaskstatus/compiling.md)
  The compiler task is currently compiling.
- [MTL4CompilerTaskStatus.finished](mtl4compilertaskstatus/finished.md)
  The compiler task is finished.
- [MTL4CompilerTaskStatus.none](mtl4compilertaskstatus/none.md)
  No status.
- [MTL4CompilerTaskStatus.scheduled](mtl4compilertaskstatus/scheduled.md)
  The compiler task is currently scheduled.
### Initializers
- [init?(rawValue: Int)](mtl4compilertaskstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
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
- [protocol MTL4Archive](mtl4archive.md)
  A read-only container that stores pipeline states from a shader compiler.
- [protocol MTL4BinaryFunction](mtl4binaryfunction.md)
  Represents a binary function.
- [class MTL4BinaryFunctionDescriptor](mtl4binaryfunctiondescriptor.md)
  Base interface for other function-derived interfaces.
- [struct MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md)
  Options for configuring the creation of binary functions.
- [class MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md)
  Groups together properties to drive the dynamic linking process of a pipeline stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compilertaskstatus)*