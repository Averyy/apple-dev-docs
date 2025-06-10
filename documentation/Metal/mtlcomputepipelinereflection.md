# MTLComputePipelineReflection

**Framework**: Metal  
**Kind**: class

Information about the arguments of a compute function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLComputePipelineReflection
```

#### Overview

An [`MTLComputePipelineReflection`](mtlcomputepipelinereflection.md) object provides access to the arguments of the compute function used in an [`MTLComputePipelineState`](mtlcomputepipelinestate.md) object. An [`MTLComputePipelineReflection`](mtlcomputepipelinereflection.md) object can be created along with an [`MTLComputePipelineState`](mtlcomputepipelinestate.md) object. Don’t create an [`MTLComputePipelineReflection`](mtlcomputepipelinereflection.md) object directly. Instead, call either the [`makeComputePipelineState(function:options:reflection:)`](mtldevice/makecomputepipelinestate(function:options:reflection:).md) or [`makeComputePipelineState(function:options:completionHandler:)`](mtldevice/makecomputepipelinestate(function:options:completionhandler:).md) method of [`MTLDevice`](mtldevice.md) to create both an [`MTLComputePipelineState`](mtlcomputepipelinestate.md) object and an [`MTLComputePipelineReflection`](mtlcomputepipelinereflection.md) object.

[`MTLComputePipelineReflection`](mtlcomputepipelinereflection.md) objects can use a significant amount of memory; release any strong references to them after you finish creating pipeline objects.

## Topics

### Obtaining the Arguments of the Compute Function
- [var arguments: [MTLArgument]](mtlcomputepipelinereflection/arguments.md)
  An array of objects that describe the arguments of a compute function.
### Instance Properties
- [var bindings: [any MTLBinding]](mtlcomputepipelinereflection/bindings.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection)*