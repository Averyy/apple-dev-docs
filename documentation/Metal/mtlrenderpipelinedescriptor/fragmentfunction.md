# fragmentFunction

**Framework**: Metal  
**Kind**: property

The fragment function the pipeline calls to process fragments.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var fragmentFunction: (any MTLFunction)? { get set }
```

#### Discussion

The default value is `nil`. If this value is `nil`, then there is no fragment function and therefore no writes to the color render target occur. Depth and stencil writes and visibility result counting can still proceed.

## See Also

- [var vertexFunction: (any MTLFunction)?](mtlrenderpipelinedescriptor/vertexfunction.md)
  The vertex function the pipeline calls to process vertices.
- [var maxVertexCallStackDepth: Int](mtlrenderpipelinedescriptor/maxvertexcallstackdepth.md)
  The maximum function call depth from the top-most vertex shader function.
- [var maxFragmentCallStackDepth: Int](mtlrenderpipelinedescriptor/maxfragmentcallstackdepth.md)
  The maximum function call depth from the top-most fragment shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/fragmentfunction)*