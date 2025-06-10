# MTL4PipelineStageDynamicLinkingDescriptor

**Framework**: Metal  
**Kind**: class

Groups together properties to drive the dynamic linking process of a pipeline stage.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MTL4PipelineStageDynamicLinkingDescriptor
```

## Topics

### Instance Properties
- [var binaryLinkedFunctions: [any MTL4BinaryFunction]?](mtl4pipelinestagedynamiclinkingdescriptor/binarylinkedfunctions.md)
  Provides the array of binary functions to link.
- [var maxCallStackDepth: Int](mtl4pipelinestagedynamiclinkingdescriptor/maxcallstackdepth.md)
  Limits the maximum depth of the call stack for indirect function calls in the pipeline stage function.
- [var preloadedLibraries: [any MTLDynamicLibrary]](mtl4pipelinestagedynamiclinkingdescriptor/preloadedlibraries.md)
  Provides an array of dynamic libraries the compiler loads when it builds the pipeline.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [struct MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md)
  Options for configuring the creation of binary functions.
- [struct MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md)
  Options for configuring the creation of binary functions.
- [class MTL4BinaryFunctionReflection](mtl4binaryfunctionreflection.md)
  Represents reflection information for a binary function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4pipelinestagedynamiclinkingdescriptor)*