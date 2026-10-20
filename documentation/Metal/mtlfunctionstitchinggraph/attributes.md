# attributes

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A list of attributes to configure how the Metal device object generates the new stitched function.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var attributes: [any MTLFunctionStitchingAttribute] { get set }
```

```objc
@property (nonatomic, copy, readwrite, nonnull) NSArray<id<MTLFunctionStitchingAttribute>> * attributes;
```

## See Also

### Configuring a function graph
- [var functionName: String](./functionname.md)
  The name of the new stitched function.
- [var nodes: [MTLFunctionStitchingFunctionNode]](./nodes.md)
  The nodes in the function’s call graph.
- [var outputNode: MTLFunctionStitchingFunctionNode?](./outputnode.md)
  The node with the output that’s the output of the new stitched function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionstitchinggraph/attributes)*