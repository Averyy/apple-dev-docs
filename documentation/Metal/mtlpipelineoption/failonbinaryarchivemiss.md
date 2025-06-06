# failOnBinaryArchiveMiss

**Framework**: Metal  
**Kind**: property

An option that specifies that Metal only creates the pipeline state object if the compiled shader is present inside a linked binary archive.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static var failOnBinaryArchiveMiss: MTLPipelineOption { get }
```

## Mentions

- [Creating Binary Archives from Device-Built Pipeline State Objects](creating-binary-archives-from-device-built-pipeline-state-objects.md)

#### Discussion

When this value is `true` and a compiled shader isn’t available, Metal produces an error rather than attempting to recompile on-demand on the GPU.

## See Also

- [static var bufferTypeInfo: MTLPipelineOption](mtlpipelineoption/buffertypeinfo.md)
  An option instance that provides detailed buffer type information for buffer arguments.
- [static var argumentInfo: MTLPipelineOption](mtlpipelineoption/argumentinfo.md)
  An option instance that provides argument information for textures and threadgroup memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpipelineoption/failonbinaryarchivemiss)*