# vertexFunction

**Framework**: Metal  
**Kind**: property

The vertex function the pipeline calls to process vertices.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var vertexFunction: (any MTLFunction)? { get set }
```

#### Discussion

The default value is `nil`. The vertex function needs to be specified. The vertex function can be either a regular vertex function or a post-tessellation vertex function.

## See Also

- [var fragmentFunction: (any MTLFunction)?](mtlrenderpipelinedescriptor/fragmentfunction.md)
  The fragment function the pipeline calls to process fragments.
- [var maxVertexCallStackDepth: Int](mtlrenderpipelinedescriptor/maxvertexcallstackdepth.md)
  The maximum function call depth from the top-most vertex shader function.
- [var maxFragmentCallStackDepth: Int](mtlrenderpipelinedescriptor/maxfragmentcallstackdepth.md)
  The maximum function call depth from the top-most fragment shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/vertexfunction)*