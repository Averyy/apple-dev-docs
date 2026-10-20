# supportAddingFragmentBinaryFunctions

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to the fragment shader’s callable functions list.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var supportAddingFragmentBinaryFunctions: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL supportAddingFragmentBinaryFunctions;
```

## See Also

### Specifying precompiled shader binaries
- [var supportAddingVertexBinaryFunctions: Bool](./supportaddingvertexbinaryfunctions.md)
  A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to the vertex shader’s callable functions list.
- [var binaryArchives: [any MTLBinaryArchive]?](./binaryarchives.md)
  An array of binary archives to search for precompiled versions of the shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/supportaddingfragmentbinaryfunctions)*