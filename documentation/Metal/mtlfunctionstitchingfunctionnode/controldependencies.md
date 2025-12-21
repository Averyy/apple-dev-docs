# controlDependencies

**Framework**: Metal  
**Kind**: property

The list of nodes that need to execute before executing the node.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var controlDependencies: [MTLFunctionStitchingFunctionNode] { get set }
```

#### Discussion

When a stitched function calls functions that have side effects on their input data, you often need the GPU to execute functions in a specific order. In such cases, use the [`controlDependencies`](mtlfunctionstitchingfunctionnode/controldependencies.md) property to specify which nodes need to run before executing this node.

## See Also

- [var name: String](mtlfunctionstitchingfunctionnode/name.md)
  The name of the function to call.
- [var arguments: [any MTLFunctionStitchingNode]](mtlfunctionstitchingfunctionnode/arguments.md)
  An ordered list of the nodes that provide the function’s arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionstitchingfunctionnode/controldependencies)*