# MTLRenderPipelineReflection

**Framework**: Metal  
**Kind**: class

Information about the arguments of a graphics function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLRenderPipelineReflection
```

#### Overview

The [`MTLRenderPipelineReflection`](mtlrenderpipelinereflection.md) class is an interface that represents the parameters for the shaders in a render pipeline state (see [`MTLRenderPipelineState`](mtlrenderpipelinestate.md)). Each pipeline state can include object, mesh, vertex, fragment, and tile shaders.

You create a reflection instance at the same time as the pipeline state that it represents by calling the appropriate [`MTLDevice`](mtldevice.md) method. For example, the [`makeRenderPipelineState(descriptor:options:reflection:)`](mtldevice/makerenderpipelinestate(descriptor:options:reflection:).md) and [`makeRenderPipelineState(descriptor:options:completionHandler:)`](mtldevice/makerenderpipelinestate(descriptor:options:completionhandler:)-5gdww.md) methods create the pipeline state and the reflection instances at the same time.

> ❗ **Important**:  Only create reflection instances if you need them because each one can require a significant amount of memory.

For more information, see [`Pipeline State Creation`](pipeline-state-creation.md).

## Topics

### Inspecting a Shader’s Parameter
- [var fragmentBindings: [any MTLBinding]](mtlrenderpipelinereflection/fragmentbindings.md)
  An array of binding instances, each of which represents a parameter of the pipeline state’s fragment shader.
- [var meshBindings: [any MTLBinding]](mtlrenderpipelinereflection/meshbindings.md)
  An array of binding instances, each of which represents a parameter of the pipeline state’s mesh shader.
- [var objectBindings: [any MTLBinding]](mtlrenderpipelinereflection/objectbindings.md)
  An array of binding instances, each of which represents a parameter of the pipeline state’s object shader.
- [var tileBindings: [any MTLBinding]](mtlrenderpipelinereflection/tilebindings.md)
  An array of binding instances, each of which represents a parameter of the pipeline state’s tile shader.
- [var vertexBindings: [any MTLBinding]](mtlrenderpipelinereflection/vertexbindings.md)
  An array of binding instances, each of which represents a parameter of the pipeline state’s vertex shader.
### Deprecated
- [var vertexArguments: [MTLArgument]?](mtlrenderpipelinereflection/vertexarguments.md)
  An array of argument instances, each of which represent a parameter of the pipeline state’s vertex shader.
- [var fragmentArguments: [MTLArgument]?](mtlrenderpipelinereflection/fragmentarguments.md)
  An array of argument instances, each of which represent a parameter of the pipeline state’s fragment shader.
- [var tileArguments: [MTLArgument]?](mtlrenderpipelinereflection/tilearguments.md)
  An array of argument instances, each of which represent a parameter of the pipeline state’s tile shader.

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

- [class MTLComputePipelineReflection](mtlcomputepipelinereflection.md)
  Information about the arguments of a compute function.
- [typealias MTLAutoreleasedComputePipelineReflection](mtlautoreleasedcomputepipelinereflection.md)
  A convenience type alias for an autoreleased compute pipeline reflection object.
- [typealias MTLAutoreleasedRenderPipelineReflection](mtlautoreleasedrenderpipelinereflection.md)
  A convenience type alias for an autoreleased pipeline reflection instance.
- [enum MTLBindingType](mtlbindingtype.md)
- [protocol MTLBinding](mtlbinding.md)
- [enum MTLBindingAccess](mtlbindingaccess.md)
- [protocol MTLBufferBinding](mtlbufferbinding.md)
- [protocol MTLTextureBinding](mtltexturebinding.md)
- [protocol MTLThreadgroupBinding](mtlthreadgroupbinding.md)
- [protocol MTLObjectPayloadBinding](mtlobjectpayloadbinding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection)*