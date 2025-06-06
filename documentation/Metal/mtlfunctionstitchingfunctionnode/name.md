# name

**Framework**: Metal  
**Kind**: property

The name of the function to call.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var name: String { get set }
```

#### Discussion

The name must match one of the functions in the stitched library descriptor’s [`functions`](mtlstitchedlibrarydescriptor/functions.md) property.

## See Also

- [var arguments: [any MTLFunctionStitchingNode]](mtlfunctionstitchingfunctionnode/arguments.md)
  An ordered list of the nodes that provide the function’s arguments.
- [var controlDependencies: [MTLFunctionStitchingFunctionNode]](mtlfunctionstitchingfunctionnode/controldependencies.md)
  The list of nodes that must execute before executing the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionstitchingfunctionnode/name)*