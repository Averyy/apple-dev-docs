# argumentInfo

**Framework**: Metal  
**Kind**: property

An option instance that provides argument information for textures and threadgroup memory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static var argumentInfo: MTLPipelineOption { get }
```

#### Discussion

This option provides all properties of a [`MTLArgument`](mtlargument.md) object, except for [`bufferStructType`](mtlargument/bufferstructtype.md) and [`bufferPointerType`](mtlargument/bufferpointertype.md), which are `nil`. To obtain these detailed buffer type properties, retrieve the [`bufferTypeInfo`](mtlpipelineoption/buffertypeinfo.md) instance.

## See Also

- [static var bufferTypeInfo: MTLPipelineOption](mtlpipelineoption/buffertypeinfo.md)
  An option instance that provides detailed buffer type information for buffer arguments.
- [static var failOnBinaryArchiveMiss: MTLPipelineOption](mtlpipelineoption/failonbinaryarchivemiss.md)
  An option that specifies that Metal only creates the pipeline state object if the compiled shader is present inside a linked binary archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpipelineoption/argumentinfo)*