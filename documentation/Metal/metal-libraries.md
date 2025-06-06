# Metal Libraries

**Framework**: Metal

Compile and manage Metal libraries from the command line.

#### Overview

By default, your Metal shaders compile as a format called  (Metal IR), a GPU-independent bytecode. At your app’s runtime, Metal compiles this bytecode to a GPU-specific binary for the host device. If you provide your shader functions as strings, they first compile to Metal IR on device, and then go through a secondary compilation for GPU.

Metal source files you add to an app’s source compilation Build Phase compile to a Metal IR library named `default.metallib`. Load this library at runtime by calling the [`makeDefaultLibrary()`](mtldevice/makedefaultlibrary().md) method of an [`MTLDevice`](mtldevice.md) in your app. For more complicated projects, you may want to create individual targets for Metal libraries, modify them in build scripts, or perform other optimizations.

Compilation of Metal IR completes before executing a shader function call. When your library consists of utility functions that other shaders use, use [`Metal Dynamic Libraries`](metal-dynamic-libraries.md). To distribute GPU-specific binaries and avoid runtime shader compilation, use [`Metal Binary Archives`](metal-binary-archives.md).

## Topics

### Working with Metal Intermediate Representation Libraries
- [Building a Shader Library by Precompiling Source Files](building-a-shader-library-by-precompiling-source-files.md)
  Create a shader library that you can add to an Xcode project with the Metal compiler tools in a command-line environment.
- [Minimizing the Binary Size of a Shader Library](minimizing-the-binary-size-of-a-shader-library.md)
  Reduce the storage footprint of your shaders, and potentially reduce their compile time, by selecting the Metal compiler’s size optimization option.
- [Generating and Loading a Metal Library Symbol File](generating-and-loading-a-metal-library-symbol-file.md)
  Debug your Metal shaders from your production apps by creating companion symbol files at compile time and loading them at debug time.

## See Also

- [Metal Dynamic Libraries](metal-dynamic-libraries.md)
  Create a single Metal library containing reusable code to reduce library size and avoid repeated shader compilation at runtime.
- [Metal Binary Archives](metal-binary-archives.md)
  Distribute precompiled GPU-specific binaries as part of your app to avoid runtime compilation of Metal shaders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/metal-libraries)*