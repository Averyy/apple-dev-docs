# fragmentFunction

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The fragment function the pipeline calls to process fragments.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var fragmentFunction: (any MTLFunction)? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) id<MTLFunction> fragmentFunction;
```

#### Discussion

The default value is `nil`. If this value is `nil`, then there is no fragment function and therefore no writes to the color render target occur. Depth and stencil writes and visibility result counting can still proceed.

## See Also

### Specifying graphics functions and associated data
- [var vertexFunction: (any MTLFunction)?](./vertexfunction.md)
  The vertex function the pipeline calls to process vertices.
- [var maxVertexCallStackDepth: Int](./maxvertexcallstackdepth.md)
  The maximum function call depth from the top-most vertex shader function.
- [var maxFragmentCallStackDepth: Int](./maxfragmentcallstackdepth.md)
  The maximum function call depth from the top-most fragment shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/fragmentfunction)*