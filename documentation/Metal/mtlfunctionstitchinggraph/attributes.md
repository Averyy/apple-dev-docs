# attributes

**Framework**: Metal  
**Kind**: property

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

## See Also

- [var functionName: String](mtlfunctionstitchinggraph/functionname.md)
  The name of the new stitched function.
- [var nodes: [MTLFunctionStitchingFunctionNode]](mtlfunctionstitchinggraph/nodes.md)
  The nodes in the function’s call graph.
- [var outputNode: MTLFunctionStitchingFunctionNode?](mtlfunctionstitchinggraph/outputnode.md)
  The node with the output that’s the output of the new stitched function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionstitchinggraph/attributes)*