# vertexFunction

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The vertex function the pipeline calls to process vertices.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var vertexFunction: (any MTLFunction)? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) id<MTLFunction> vertexFunction;
```

#### Discussion

The default value is `nil`. The vertex function needs to be specified. The vertex function can be either a regular vertex function or a post-tessellation vertex function.

## See Also

### Specifying graphics functions and associated data
- [var fragmentFunction: (any MTLFunction)?](./fragmentfunction.md)
  The fragment function the pipeline calls to process fragments.
- [var maxVertexCallStackDepth: Int](./maxvertexcallstackdepth.md)
  The maximum function call depth from the top-most vertex shader function.
- [var maxFragmentCallStackDepth: Int](./maxfragmentcallstackdepth.md)
  The maximum function call depth from the top-most fragment shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/vertexfunction)*