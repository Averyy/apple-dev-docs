# maxVertexCallStackDepth

**Framework**: Metal  
**Kind**: property

The maximum function call depth from the top-most vertex shader function.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var maxVertexCallStackDepth: Int { get set }
```

#### Discussion

The default value is 1.

## See Also

- [var vertexFunction: (any MTLFunction)?](mtlrenderpipelinedescriptor/vertexfunction.md)
  The vertex function the pipeline calls to process vertices.
- [var fragmentFunction: (any MTLFunction)?](mtlrenderpipelinedescriptor/fragmentfunction.md)
  The fragment function the pipeline calls to process fragments.
- [var maxFragmentCallStackDepth: Int](mtlrenderpipelinedescriptor/maxfragmentcallstackdepth.md)
  The maximum function call depth from the top-most fragment shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/maxvertexcallstackdepth)*