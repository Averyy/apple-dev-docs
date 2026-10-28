# MTLLibrary

**Framework**: Metal  
**Kind**: protocol  
**Role**: Protocol

A collection of Metal shader functions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
protocol MTLLibrary : NSObjectProtocol, Sendable
```

```objc
@protocol MTLLibrary <NSObject>
```

## Mentions

- [Building a shader library by precompiling source files](./building-a-shader-library-by-precompiling-source-files.md)
- [Logging shader debug messages](./logging-shader-debug-messages.md)

## Overview

An [`MTLLibrary`](./mtllibrary.md) instance contains Metal shading language source code compiled during an app’s build process or at runtime from a text string.

Don’t implement this protocol yourself; instead, use the library creation methods provided by the [`MTLDevice`](./mtldevice.md) protocol. To create an [`MTLLibrary`](./mtllibrary.md) from a precompiled Metal library binary, call one of these [`MTLDevice`](./mtldevice.md) methods:

- [`makeDefaultLibrary()`](./mtldevice/makedefaultlibrary%28%29.md)
- [`makeLibrary(filepath:)`](./mtldevice/makelibrary%28filepath%29.md)
- [`makeLibrary(data:)`](./mtldevice/makelibrary%28data%29.md)

To create an [`MTLLibrary`](./mtllibrary.md) by compiling source code at runtime, call one of these [`MTLDevice`](./mtldevice.md) methods:

- [`makeLibrary(source:options:completionHandler:)`](./mtldevice/makelibrary%28source,options,completionhandler%29.md)
- [`makeLibrary(source:options:)`](./mtldevice/makelibrary%28source,options%29.md)

## Topics

### Querying basic library attributes
- [var installName: String?](./mtllibrary/installname.md)
  The installation name for a dynamic library.
- [var type: MTLLibraryType](./mtllibrary/type.md)
  The library’s basic type.
### Querying library contents
- [var functionNames: [String]](./mtllibrary/functionnames.md)
  The names of all public functions in the library.
### Creating shader function instances
- [func makeFunction(name: String) -> (any MTLFunction)?](./mtllibrary/makefunction%28name%29.md)
  Creates an instance that represents a shader function in the library.
- [func makeFunction(name: String, constantValues: MTLFunctionConstantValues, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](./mtllibrary/makefunction%28name,constantvalues,completionhandler%29.md)
  Asynchronously creates a specialized shader function.
- [func makeFunction(name: String, constantValues: MTLFunctionConstantValues) throws -> any MTLFunction](./mtllibrary/makefunction%28name,constantvalues%29.md)
  Synchronously creates a specialized shader function.
- [func makeFunction(descriptor: MTLFunctionDescriptor, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](./mtllibrary/makefunction%28descriptor,completionhandler%29.md)
  Asynchronously creates an object representing a shader function, using the specified descriptor.
- [func makeFunction(descriptor: MTLFunctionDescriptor) throws -> any MTLFunction](./mtllibrary/makefunction%28descriptor%29.md)
  Synchronously creates an object representing a shader function, using the specified descriptor.
### Creating intersection function instances
- [func makeIntersectionFunction(descriptor: MTLIntersectionFunctionDescriptor, completionHandler: ((any MTLFunction)?, (any Error)?) -> Void)](./mtllibrary/makeintersectionfunction%28descriptor,completionhandler%29.md)
  Asynchronously creates an object representing a ray-tracing intersection function, using the specified descriptor.
- [func makeIntersectionFunction(descriptor: MTLIntersectionFunctionDescriptor) throws -> any MTLFunction](./mtllibrary/makeintersectionfunction%28descriptor%29.md)
  Synchronously creates an object representing a ray-tracing intersection function, using the specified descriptor.
### Identifying the library
- [var device: any MTLDevice](./mtllibrary/device.md)
  The Metal device object that created the library.
- [var label: String?](./mtllibrary/label.md)
  A string that identifies the library.
### Instance Methods
- [func reflection(functionName: String) -> MTLFunctionReflection?](./mtllibrary/reflection%28functionname%29.md)
  Retrieves reflection information for a function in the library.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Shader library management
- [protocol MTLDynamicLibrary](./mtldynamiclibrary.md)
  A dynamically linkable representation of compiled shader code for a specific Metal device object.
- [protocol MTLBinaryArchive](./mtlbinaryarchive.md)
  A container for pipeline state descriptors and their associated compiled shader code.
- [class MTLCompileOptions](./mtlcompileoptions.md)
  Compilation settings for a Metal shader library.
- [enum MTLLibraryType](./mtllibrarytype.md)
  A set of options for Metal library types.
- [enum MTLLanguageVersion](./mtllanguageversion.md)
  Metal shading language versions.
- [enum MTLCompileSymbolVisibility](./mtlcompilesymbolvisibility.md)
- [enum MTLLibraryOptimizationLevel](./mtllibraryoptimizationlevel.md)
  The optimization options for the Metal compiler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllibrary)*