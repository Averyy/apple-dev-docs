# MTLFunction

**Framework**: Metal  
**Kind**: protocol

An object that represents a public shader function in a Metal library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLFunction : NSObjectProtocol, Sendable
```

#### Overview

Use [`MTLFunction`](mtlfunction.md) objects to specify which shaders a Metal pipeline calls when the GPU executes commands that specify that pipeline. For more information on creating pipeline state objects, see [`MTLRenderPipelineDescriptor`](mtlrenderpipelinedescriptor.md) and [`MTLComputePipelineDescriptor`](mtlcomputepipelinedescriptor.md).

A [`MTLFunction`](mtlfunction.md) object is a  function if the shader contains function constants, otherwise it is a  function.

Don’t use standard allocation and initialization techniques to create a [`MTLFunction`](mtlfunction.md) object. Instead, use the function creation methods provided by the [`MTLLibrary`](mtllibrary.md) protocol. To create a nonspecialized function, call the [`makeFunction(name:)`](mtllibrary/makefunction(name:).md) method.

To create a specialized function, call one of these [`MTLLibrary`](mtllibrary.md) methods:

- [`makeFunction(name:constantValues:completionHandler:)`](mtllibrary/makefunction(name:constantvalues:completionhandler:).md)
- [`makeFunction(name:constantValues:)`](mtllibrary/makefunction(name:constantvalues:).md)

[`MTLFunction`](mtlfunction.md) objects can use a significant amount of memory; release any strong references to them after you finish creating pipeline objects.

## Topics

### Identifying Shader Functions
- [var device: any MTLDevice](mtlfunction/device.md)
  The device object that created the shader function.
- [var label: String?](mtlfunction/label.md)
  A string that identifies the shader function.
- [var functionType: MTLFunctionType](mtlfunction/functiontype.md)
  The shader function’s type.
- [var name: String](mtlfunction/name.md)
  The function’s name.
- [enum MTLFunctionType](mtlfunctiontype.md)
  The type of a top-level Metal Shading Language (MSL) function.
- [var options: MTLFunctionOptions](mtlfunction/options.md)
  The options that Metal used to compile this function.
- [struct MTLFunctionOptions](mtlfunctionoptions.md)
  Options that define how Metal creates the function object.
### Identifying the Tessellation Patch
- [var patchType: MTLPatchType](mtlfunction/patchtype.md)
  The tessellation patch type of a post-tessellation vertex function.
- [var patchControlPointCount: Int](mtlfunction/patchcontrolpointcount.md)
  The number of patch control points in the post-tessellation vertex function.
- [enum MTLPatchType](mtlpatchtype.md)
  Types of tessellation patches that can be inputs of a post-tessellation vertex function.
### Retrieving Function Attributes
- [var vertexAttributes: [MTLVertexAttribute]?](mtlfunction/vertexattributes.md)
  An array that describes the vertex input attributes to a vertex function.
- [var stageInputAttributes: [MTLAttribute]?](mtlfunction/stageinputattributes.md)
  An array that describes the input attributes to the function.
### Retrieving Function Constants
- [var functionConstantsDictionary: [String : MTLFunctionConstant]](mtlfunction/functionconstantsdictionary.md)
  A dictionary of function constants for a specialized function.
### Creating Argument Encoders
- [func makeArgumentEncoder(bufferIndex: Int) -> any MTLArgumentEncoder](mtlfunction/makeargumentencoder(bufferindex:).md)
  Creates an argument encoder for an argument buffer that’s one of this function’s arguments.
- [func makeArgumentEncoder(bufferIndex: Int, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedArgument?>?) -> any MTLArgumentEncoder](mtlfunction/makeargumentencoder(bufferindex:reflection:).md)
  Creates an argument encoder and returns reflection information for an argument buffer that’s one of this function’s arguments

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MTLFunctionDescriptor](mtlfunctiondescriptor.md)
  A description of a function object to create.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunction)*