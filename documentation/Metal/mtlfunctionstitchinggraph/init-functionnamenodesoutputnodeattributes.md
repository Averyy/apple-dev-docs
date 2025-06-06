# init(functionName:nodes:outputNode:attributes:)

**Framework**: Metal  
**Kind**: init

Creates a description of a new function call graph.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(functionName: String, nodes: [MTLFunctionStitchingFunctionNode], outputNode: MTLFunctionStitchingFunctionNode?, attributes: [any MTLFunctionStitchingAttribute])
```

## Parameters

- `functionName`: The name of the new function.
- `nodes`: The nodes in the function’s call graph.
- `outputNode`: The node whose output is the output of the new stitched function.
- `attributes`: A list of attributes used to generate the new stitched function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionstitchinggraph/init(functionname:nodes:outputnode:attributes:))*