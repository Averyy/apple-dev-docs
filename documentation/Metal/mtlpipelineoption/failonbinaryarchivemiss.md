# failOnBinaryArchiveMiss

**Framework**: Metal  
**Kind**: property

An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.

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

- [Creating binary archives from device-built pipeline state objects](creating-binary-archives-from-device-built-pipeline-state-objects.md)

#### Discussion

By default, Metal compiles the functions for a pipeline state if they aren’t in a binary archive. When you set this option, Metal returns an error instead of compiling a missing function.

## See Also

- [static var bufferTypeInfo: MTLPipelineOption](mtlpipelineoption/buffertypeinfo.md)
  An option instance that provides detailed buffer type information for buffer arguments.
- [static var argumentInfo: MTLPipelineOption](mtlpipelineoption/argumentinfo.md)
  An option instance that provides argument information for textures and threadgroup memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpipelineoption/failonbinaryarchivemiss)*