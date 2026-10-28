# argumentInfo

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

An option instance that provides argument information for textures and threadgroup memory.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0 (renamed: MTLPipelineOption.bindingInfo)
- iPadOS 8.0+ - Deprecated in 16.0 (renamed: MTLPipelineOption.bindingInfo)
- Mac Catalyst 13.1+ - Deprecated in 16.0 (renamed: MTLPipelineOption.bindingInfo)
- macOS 10.11+ - Deprecated in 13.0 (renamed: MTLPipelineOption.bindingInfo)
- tvOS - Deprecated in 16.0 (renamed: MTLPipelineOption.bindingInfo)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: MTLPipelineOption.bindingInfo)

## Declaration

```swift
static var argumentInfo: MTLPipelineOption { get }
```

```c
MTLPipelineOptionArgumentInfo
```

## Discussion

This option provides all properties of an [`MTLArgument`](../mtlargument.md) instance, except for [`bufferStructType`](../mtlargument/bufferstructtype.md) and [`bufferPointerType`](../mtlargument/bufferpointertype.md), which are `nil`. To obtain these detailed buffer type properties, retrieve the [`bufferTypeInfo`](./buffertypeinfo.md) instance.

## See Also

### Retrieving argument information
- [static var bufferTypeInfo: MTLPipelineOption](./buffertypeinfo.md)
  An option instance that provides detailed buffer type information for buffer arguments.
- [static var failOnBinaryArchiveMiss: MTLPipelineOption](./failonbinaryarchivemiss.md)
  An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [MTLPipelineOptionNone](./mtlpipelineoptionnone.md)
  Don’t provide any reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpipelineoption/argumentinfo)*