# MTLBinding

**Framework**: Metal  
**Kind**: protocol

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLBinding : NSObjectProtocol
```

## Topics

### Instance Properties
- [var access: MTLBindingAccess](mtlbinding/access.md)
- [var index: Int](mtlbinding/index.md)
- [var isArgument: Bool](mtlbinding/isargument.md)
- [var isUsed: Bool](mtlbinding/isused.md)
- [var name: String](mtlbinding/name.md)
- [var type: MTLBindingType](mtlbinding/type.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [MTLBufferBinding](mtlbufferbinding.md)
- [MTLObjectPayloadBinding](mtlobjectpayloadbinding.md)
- [MTLTextureBinding](mtltexturebinding.md)
- [MTLThreadgroupBinding](mtlthreadgroupbinding.md)

## See Also

- [class MTLComputePipelineReflection](mtlcomputepipelinereflection.md)
  Information about the arguments of a compute function.
- [typealias MTLAutoreleasedComputePipelineReflection](mtlautoreleasedcomputepipelinereflection.md)
  A convenience type alias for an autoreleased compute pipeline reflection object.
- [class MTLRenderPipelineReflection](mtlrenderpipelinereflection.md)
  Information about the arguments of a graphics function.
- [typealias MTLAutoreleasedRenderPipelineReflection](mtlautoreleasedrenderpipelinereflection.md)
  A convenience type alias for an autoreleased pipeline reflection instance.
- [enum MTLBindingType](mtlbindingtype.md)
- [enum MTLBindingAccess](mtlbindingaccess.md)
- [protocol MTLBufferBinding](mtlbufferbinding.md)
- [protocol MTLTextureBinding](mtltexturebinding.md)
- [protocol MTLThreadgroupBinding](mtlthreadgroupbinding.md)
- [protocol MTLObjectPayloadBinding](mtlobjectpayloadbinding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinding)*