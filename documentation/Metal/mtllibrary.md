# MTLLibrary

**Framework**: Metal  
**Kind**: protocol

A collection of Metal shader functions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLLibrary : NSObjectProtocol, Sendable
```

## Mentions

- [Building a shader library by precompiling source files](building-a-shader-library-by-precompiling-source-files.md)
- [Logging shader debug messages](logging-shader-debug-messages.md)

#### Overview

An [`MTLLibrary`](mtllibrary.md) instance contains Metal shading language source code compiled during an app’s build process or at runtime from a text string.

Don’t implement this protocol yourself; instead, use the library creation methods provided by the [`MTLDevice`](mtldevice.md) protocol. To create an [`MTLLibrary`](mtllibrary.md) from a precompiled Metal library binary, call one of these [`MTLDevice`](mtldevice.md) methods:

- [`makeDefaultLibrary()`](mtldevice/makedefaultlibrary().md)
- [`makeLibrary(filepath:)`](mtldevice/makelibrary(filepath:).md)
- [`makeLibrary(data:)`](mtldevice/makelibrary(data:).md)

To create an [`MTLLibrary`](mtllibrary.md) by compiling source code at runtime, call one of these [`MTLDevice`](mtldevice.md) methods:

- [`makeLibrary(source:options:completionHandler:)`](mtldevice/makelibrary(source:options:completionhandler:).md)
- [`makeLibrary(source:options:)`](mtldevice/makelibrary(source:options:).md)

## Topics

### Querying basic library attributes
- [var installName: String?](mtllibrary/installname.md)
  The installation name for a dynamic library.
- [var type: MTLLibraryType](mtllibrary/type.md)
  The library’s basic type.
### Querying library contents
- [var functionNames: [String]](mtllibrary/functionnames.md)
  The names of all public functions in the library.
### Creating shader function instances
- [func makeFunction(name: String) -> (any MTLFunction)?](mtllibrary/makefunction(name:).md)
  Creates an instance that represents a shader function in the library.
- [func makeFunction(name: String, constantValues: MTLFunctionConstantValues, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](mtllibrary/makefunction(name:constantvalues:completionhandler:).md)
  Asynchronously creates a specialized shader function.
- [func makeFunction(name: String, constantValues: MTLFunctionConstantValues) throws -> any MTLFunction](mtllibrary/makefunction(name:constantvalues:).md)
  Synchronously creates a specialized shader function.
- [func makeFunction(descriptor: MTLFunctionDescriptor, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](mtllibrary/makefunction(descriptor:completionhandler:).md)
  Asynchronously creates an object representing a shader function, using the specified descriptor.
- [func makeFunction(descriptor: MTLFunctionDescriptor) throws -> any MTLFunction](mtllibrary/makefunction(descriptor:).md)
  Synchronously creates an object representing a shader function, using the specified descriptor.
### Creating intersection function instances
- [func makeIntersectionFunction(descriptor: MTLIntersectionFunctionDescriptor, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](mtllibrary/makeintersectionfunction(descriptor:completionhandler:).md)
  Asynchronously creates an object representing a ray-tracing intersection function, using the specified descriptor.
- [func makeIntersectionFunction(descriptor: MTLIntersectionFunctionDescriptor) throws -> any MTLFunction](mtllibrary/makeintersectionfunction(descriptor:).md)
  Synchronously creates an object representing a ray-tracing intersection function, using the specified descriptor.
### Identifying the library
- [var device: any MTLDevice](mtllibrary/device.md)
  The Metal device object that created the library.
- [var label: String?](mtllibrary/label.md)
  A string that identifies the library.
### Instance Methods
- [func reflection(functionName: String) -> MTLFunctionReflection?](mtllibrary/reflection(functionname:).md)
  Retrieves reflection information for a function in the library.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MTLDynamicLibrary](mtldynamiclibrary.md)
  A dynamically linkable representation of compiled shader code for a specific Metal device object.
- [protocol MTLBinaryArchive](mtlbinaryarchive.md)
  A container for pipeline state descriptors and their associated compiled shader code.
- [class MTLCompileOptions](mtlcompileoptions.md)
  Compilation settings for a Metal shader library.
- [enum MTLLibraryType](mtllibrarytype.md)
  A set of options for Metal library types.
- [enum MTLLanguageVersion](mtllanguageversion.md)
  Metal shading language versions.
- [enum MTLCompileSymbolVisibility](mtlcompilesymbolvisibility.md)
- [enum MTLLibraryOptimizationLevel](mtllibraryoptimizationlevel.md)
  The optimization options for the Metal compiler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibrary)*