# bufferTypeInfo

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

An option instance that provides detailed buffer type information for buffer arguments.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static var bufferTypeInfo: MTLPipelineOption { get }
```

```c
MTLPipelineOptionBufferTypeInfo
```

#### Discussion

This option provides the [`bufferStructType`](../mtlargument/bufferstructtype.md) and [`bufferPointerType`](../mtlargument/bufferpointertype.md) properties for the [`MTLPipelineOption`](../mtlpipelineoption.md) stored in [`argumentInfo`](./argumentinfo.md).

## See Also

### Retrieving argument information
- [static var failOnBinaryArchiveMiss: MTLPipelineOption](./failonbinaryarchivemiss.md)
  An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [static var argumentInfo: MTLPipelineOption](./argumentinfo.md)
  An option instance that provides argument information for textures and threadgroup memory.
- [MTLPipelineOptionNone](./mtlpipelineoptionnone.md)
  Don’t provide any reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpipelineoption/buffertypeinfo)*