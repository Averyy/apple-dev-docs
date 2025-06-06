# supportAddingVertexBinaryFunctions

**Framework**: Metal  
**Kind**: property

A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to the vertex shader’s callable functions list.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var supportAddingVertexBinaryFunctions: Bool { get set }
```

## See Also

- [var supportAddingFragmentBinaryFunctions: Bool](mtlrenderpipelinedescriptor/supportaddingfragmentbinaryfunctions.md)
  A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to the fragment shader’s callable functions list.
- [var binaryArchives: [any MTLBinaryArchive]?](mtlrenderpipelinedescriptor/binaryarchives.md)
  An array of binary archives to search for precompiled versions of the shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/supportaddingvertexbinaryfunctions)*