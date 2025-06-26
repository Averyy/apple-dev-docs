# Metal Dynamic Libraries

**Framework**: Metal

Create a single Metal library containing reusable code to reduce library size and avoid repeated shader compilation at runtime.

#### Overview

As shaders grow in size, complexity, and scope, they often end up sharing utility functions. Under Metal’s default compilation model, linking embeds libraries, similar to static linking with the LLVM linker. For Metal, embedding libraries in this manner has two consequences: an increase in binary size, and an increase in compilation time. As each library loads, it compiles its own version of any utility functions, meaning Metal compiles and duplicates your utility functions multiple times.

To avoid this problem, Metal offers dynamic libraries, similar to an LLVM dynamically shared library. Your app loads and compiles dynamic libraries for the device GPU once, the first time a shader requests them. Subsequent shader calls use these compiled utility functions instead of compiling a separate version of the same shader binary.

To support Metal dynamic libraries in your app, call [`makeDynamicLibrary(library:)`](mtldevice/makedynamiclibrary(library:).md) with a dynamic library that you bundle as part of your app. Then add it to a pipeline descriptor’s dynamic library information through a property like [`preloadedLibraries`](mtlcomputepipelinedescriptor/preloadedlibraries.md).

## Topics

### Working with Metal Dynamic Libraries
- [Compiling and Linking Metal Dynamic Libraries](compiling-and-linking-metal-dynamic-libraries.md)
  Build a Metal dynamic library from the command line, allowing for runtime loading of shared shaders.
- [Creating a Metal Dynamic Library](creating-a-metal-dynamic-library.md)
  Compile a library of shaders and write it to a file as a dynamically linked library.

## See Also

- [Metal Libraries](metal-libraries.md)
  Compile and manage Metal libraries from the command line.
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
- [class MTL4BinaryFunctionReflection](mtl4binaryfunctionreflection.md)
  Represents reflection information for a binary function.
- [class MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md)
  Groups together properties to drive the dynamic linking process of a pipeline stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/metal-dynamic-libraries)*