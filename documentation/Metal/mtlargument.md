# MTLArgument

**Framework**: Metal  
**Kind**: class

Information about an argument of a graphics or compute function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLArgument
```

#### Overview

A [`MTLArgument`](mtlargument.md) object describes a single argument to a Metal function. Your app uses the [`MTLArgument`](mtlargument.md) properties to read details about a function argument as it was defined in the Metal Shading Language. You can determine the argument’s data type, access restrictions, and its associated resource type. For buffer, texture, and threadgroup memory arguments, additional properties can be read to determine more details about the argument.

Your app does not create a [`MTLArgument`](mtlargument.md) object directly. Creating a [`MTLRenderPipelineState`](mtlrenderpipelinestate.md) or [`MTLComputePipelineState`](mtlcomputepipelinestate.md) object can generate a reflection object ([`MTLRenderPipelineReflection`](mtlrenderpipelinereflection.md) or [`MTLComputePipelineReflection`](mtlcomputepipelinereflection.md)) that contains [`MTLArgument`](mtlargument.md) objects.

## Topics

### Describing the Argument
- [var name: String](mtlargument/name.md)
  The name of the argument.
- [var isActive: Bool](mtlargument/isactive.md)
  A Boolean that indicates whether the compiled function uses the argument.
- [var index: Int](mtlargument/index.md)
  The index in the argument table that corresponds to the function argument.
- [var type: MTLArgumentType](mtlargument/type.md)
  The argument’s resource type.
- [var access: MTLBindingAccess](mtlargument/access.md)
  The argument’s read and/or write access.
### Describing a Buffer Argument
- [var bufferAlignment: Int](mtlargument/bufferalignment.md)
  The required byte alignment in memory for the buffer data.
- [var bufferDataSize: Int](mtlargument/bufferdatasize.md)
  The size, in bytes, of the buffer data.
- [var bufferDataType: MTLDataType](mtlargument/bufferdatatype.md)
  The data type of the buffer data.
- [var bufferStructType: MTLStructType?](mtlargument/bufferstructtype.md)
  A description of the structure data of a buffer argument.
- [var bufferPointerType: MTLPointerType?](mtlargument/bufferpointertype.md)
  A description of the pointer to a buffer argument.
### Describing a Texture Argument
- [var textureDataType: MTLDataType](mtlargument/texturedatatype.md)
  The data type of a texture argument.
- [var textureType: MTLTextureType](mtlargument/texturetype.md)
  The texture type of a texture argument.
- [var isDepthTexture: Bool](mtlargument/isdepthtexture.md)
  A Boolean value that indicates whether the texture is a depth texture.
### Describing an Array Argument
- [var arrayLength: Int](mtlargument/arraylength.md)
  The number of elements, if the argument is an array.
### Describing a Threadgroup Memory Argument
- [var threadgroupMemoryAlignment: Int](mtlargument/threadgroupmemoryalignment.md)
  The required byte alignment in memory for the threadgroup data.
- [var threadgroupMemoryDataSize: Int](mtlargument/threadgroupmemorydatasize.md)
  The size, in bytes, of the threadgroup data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MTLAttribute](mtlattribute.md)
  An object that describes an attribute defined in the stage-in argument for a shader.
- [class MTLVertexAttribute](mtlvertexattribute.md)
  An object that represents an attribute of a vertex function.
- [typealias MTLAutoreleasedArgument](mtlautoreleasedargument.md)
  A convenience type alias for an autoreleased argument instance.
- [enum MTLArgumentType](mtlargumenttype.md)
  The resource type for an argument of a function.
- [typealias MTLArgumentAccess](mtlargumentaccess.md)
  Function access restrictions to argument data in the shading language code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument)*