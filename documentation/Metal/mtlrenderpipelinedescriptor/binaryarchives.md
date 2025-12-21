# binaryArchives

**Framework**: Metal  
**Kind**: property

An array of binary archives to search for precompiled versions of the shader.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var binaryArchives: [any MTLBinaryArchive]? { get set }
```

## Mentions

- [Creating binary archives from device-built pipeline state objects](creating-binary-archives-from-device-built-pipeline-state-objects.md)

## See Also

- [var supportAddingVertexBinaryFunctions: Bool](mtlrenderpipelinedescriptor/supportaddingvertexbinaryfunctions.md)
  A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to the vertex shader’s callable functions list.
- [var supportAddingFragmentBinaryFunctions: Bool](mtlrenderpipelinedescriptor/supportaddingfragmentbinaryfunctions.md)
  A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to the fragment shader’s callable functions list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/binaryarchives)*