# Shader Libraries

**Framework**: Metal

Manage and load your app’s Metal shaders.

#### Overview

A Metal library represents a collection of one or more shaders. Xcode creates a library from the shader source files in a project, a Metal intermediate representation (IR) file, or a binary archive file. You can also create IR files from Metal source code by running the Metal compiler in a command-line environment.

Apps create the default library instance by calling a Metal device’s [`makeDefaultLibrary()`](mtldevice/makedefaultlibrary().md) method. The default library contains all the shaders from a project’s shader source files, which Xcode compiles at build time. Apps create additional libraries by passing an IR file to an [`MTLDevice`](mtldevice.md) instance’s [`makeLibrary(URL:)`](mtldevice/makelibrary(url:).md) method or one of its sibling methods. The device can also create a library directly from source code by passing it as a string to the [`makeLibrary(source:options:)`](mtldevice/makelibrary(source:options:).md) method. See [`Shader Library and Archive Creation`](shader-library-and-archive-creation.md) for more information.

You can apply a shader from a library to a pipeline state’s entry point, such as the [`computeFunction`](mtlcomputepipelinedescriptor/computefunction.md) property for a compute pass. Start by retrieving an [`MTLFunction`](mtlfunction.md) instance from a library, which is a reference to the library’s shader, by calling its [`makeFunction(name:)`](mtllibrary/makefunction(name:).md) method or a sibling method. Then set the function instance to the appropriate property of a pipeline descriptor. For example, an app can retrieve a vertex stage’s entry point shader from a library and assign it to the [`vertexFunction`](mtlrenderpipelinedescriptor/vertexfunction.md) property of an [`MTLRenderPipelineDescriptor`](mtlrenderpipelinedescriptor.md).

Dynamic libraries are a collection of other shaders, typically utility functions, that support the entry point shaders for a pipeline state. To create a dynamic library, pass an [`MTLLibrary`](mtllibrary.md) instance to a device’s [`makeDynamicLibrary(library:)`](mtldevice/makedynamiclibrary(library:).md) method, or pass a file URL to [`makeDynamicLibrary(url:)`](mtldevice/makedynamiclibrary(url:).md). Add a dynamic library to a pipeline state by including it in an array of a pipeline descriptor’s preloaded libraries property. For example, if a vertex shader calls a shader in a dynamic library, directly or indirectly, add that dynamic library to the [`vertexPreloadedLibraries`](mtlrenderpipelinedescriptor/vertexpreloadedlibraries.md) property’s array. You can also build dynamic libraries with the Metal compiler in Terminal.

Binary archives are precompiled static libraries for specific GPU architectures that allow you to avoid the cost of runtime shader compilation. Because Metal automatically builds and caches shaders on the device running an app, use binary archives as part of your distributed app, or deliver them through content updates. See [`Creating Binary Archives from Device-Built Pipeline State Objects`](creating-binary-archives-from-device-built-pipeline-state-objects.md) for more information on how to build and distribute binary archives for any device that supports Metal.

## Topics

### Shader Compilation
- [Metal Libraries](metal-libraries.md)
  Compile and manage Metal libraries from the command line.
- [Metal Dynamic Libraries](metal-dynamic-libraries.md)
  Create a single Metal library containing reusable code to reduce library size and avoid repeated shader compilation at runtime.
- [Metal Binary Archives](metal-binary-archives.md)
  Distribute precompiled GPU-specific binaries as part of your app to avoid runtime compilation of Metal shaders.
### Shader Library Management
- [protocol MTLLibrary](mtllibrary.md)
  A collection of Metal shader functions.
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
### Shader Functions
- [class MTLFunctionDescriptor](mtlfunctiondescriptor.md)
  A description of a function object to create.
- [protocol MTLFunction](mtlfunction.md)
  An object that represents a public shader function in a Metal library.
- [protocol MTLFunctionHandle](mtlfunctionhandle.md)
  An object representing a function that you can add to a visible function table.
- [class MTLVisibleFunctionTableDescriptor](mtlvisiblefunctiontabledescriptor.md)
  A specification of how to create a visible function table.
- [protocol MTLVisibleFunctionTable](mtlvisiblefunctiontable.md)
  A table of shader functions visible to your app that you can pass into compute commands to customize the behavior of a shader.
- [class MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md)
  A description of an intersection function that performs an intersection test.
- [class MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md)
  A specification of how to create an intersection function table.
- [protocol MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md)
  A table of intersection functions that Metal calls to perform ray-tracing intersection tests.
### Stitched Function Libraries
- [Customizing shaders using function pointers and stitching](customizing-shaders-using-function-pointers-and-stitching.md)
  Define custom shader behavior at runtime by creating functions from existing ones and preferentially linking to others in a dynamic library.
- [class MTLStitchedLibraryDescriptor](mtlstitchedlibrarydescriptor.md)
  A description of a new library of procedurally generated functions.
- [class MTLFunctionStitchingGraph](mtlfunctionstitchinggraph.md)
  A description of a new stitched function.
- [class MTLFunctionStitchingInputNode](mtlfunctionstitchinginputnode.md)
  A call graph node that describes an input to the call graph.
- [class MTLFunctionStitchingFunctionNode](mtlfunctionstitchingfunctionnode.md)
  A call graph node that describes a function call and its inputs.
- [protocol MTLFunctionStitchingNode](mtlfunctionstitchingnode.md)
  A protocol to identify call graph nodes.
- [class MTLFunctionStitchingAttributeAlwaysInline](mtlfunctionstitchingattributealwaysinline.md)
  An attribute to specify that Metal needs to inline all of the function calls when generating the stitched function.
- [protocol MTLFunctionStitchingAttribute](mtlfunctionstitchingattribute.md)
  A protocol to identify types that customize how the Metal compiler stitches a function together.
### Compile-Time Variant Functions
- [class MTLFunctionConstant](mtlfunctionconstant.md)
  A constant that specializes the behavior of a shader.
- [class MTLFunctionConstantValues](mtlfunctionconstantvalues.md)
  A set of constant values that specialize a graphics or compute function.
### Introspection Data
- [class MTLComputePipelineReflection](mtlcomputepipelinereflection.md)
  Information about the arguments of a compute function.
- [typealias MTLAutoreleasedComputePipelineReflection](mtlautoreleasedcomputepipelinereflection.md)
  A convenience type alias for an autoreleased compute pipeline reflection object.
- [class MTLRenderPipelineReflection](mtlrenderpipelinereflection.md)
  Information about the arguments of a graphics function.
- [typealias MTLAutoreleasedRenderPipelineReflection](mtlautoreleasedrenderpipelinereflection.md)
  A convenience type alias for an autoreleased pipeline reflection instance.
- [enum MTLBindingType](mtlbindingtype.md)
- [protocol MTLBinding](mtlbinding.md)
- [enum MTLBindingAccess](mtlbindingaccess.md)
- [protocol MTLBufferBinding](mtlbufferbinding.md)
- [protocol MTLTextureBinding](mtltexturebinding.md)
- [protocol MTLThreadgroupBinding](mtlthreadgroupbinding.md)
- [protocol MTLObjectPayloadBinding](mtlobjectpayloadbinding.md)
### Function Arguments
- [class MTLAttribute](mtlattribute.md)
  An object that describes an attribute defined in the stage-in argument for a shader.
- [class MTLVertexAttribute](mtlvertexattribute.md)
  An object that represents an attribute of a vertex function.
- [class MTLArgument](mtlargument.md)
  Information about an argument of a graphics or compute function.
- [typealias MTLAutoreleasedArgument](mtlautoreleasedargument.md)
  A convenience type alias for an autoreleased argument instance.
- [enum MTLArgumentType](mtlargumenttype.md)
  The resource type for an argument of a function.
- [typealias MTLArgumentAccess](mtlargumentaccess.md)
  Function access restrictions to argument data in the shading language code.
### Shader Types
- [class MTLType](mtltype.md)
  A description of a data type.
- [enum MTLDataType](mtldatatype.md)
  The types of GPU functions, including shaders and compute kernels.
- [class MTLArrayType](mtlarraytype.md)
  A description of an array.
- [class MTLStructType](mtlstructtype.md)
  A description of a structure.
- [class MTLStructMember](mtlstructmember.md)
  An object that provides information about a field in a structure.
- [class MTLPointerType](mtlpointertype.md)
  A description of a pointer.
- [class MTLTextureReferenceType](mtltexturereferencetype.md)
  A description of a texture.
### Shader Logging
- [class MTLLogStateDescriptor](mtllogstatedescriptor.md)
  An interface that represents a log state configuration.
- [protocol MTLLogState](mtllogstate.md)
  A container for shader log messages.
### Errors
- [struct MTLLibraryError](mtllibraryerror-swift.struct.md)
  Metal errors related to libraries.
- [MTLLibraryError.Code](mtllibraryerror-swift.struct/code.md)
  Error codes for Metal library errors.
- [let MTLLibraryErrorDomain: String](mtllibraryerrordomain.md)
  The error domain for Metal libraries.

## See Also

- [Stepping through code and inspecting variables to isolate bugs](../Xcode/stepping-through-code-and-inspecting-variables-to-isolate-bugs.md)
  Find the cause of your bugs by watching variables change as you step through your source code in the debugger.
- [Optimizing GPU performance](../Xcode/Optimizing-GPU-performance.md)
  Find and address performance bottlenecks using the Metal debugger.
- [Logging shader debug messages](logging-shader-debug-messages.md)
  Print debugging messages that a shader generates using shader logging.
- [Using Function Specialization to Build Pipeline Variants](using-function-specialization-to-build-pipeline-variants.md)
  Create pipelines for different levels of detail from a common shader source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/shader-libraries)*