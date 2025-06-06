# setBatchSize(_:forFunction:)

**Framework**: Accelerate  
**Kind**: method

Sets the batch size for a graph.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
func setBatchSize(_ batchSize: Int, forFunction function: String? = nil) async
```

## Parameters

- `batchSize`: The batch size.
- `function`: The function. Specify as   if the graph only contains one function.

## See Also

- [func BNNSGraphContextSetBatchSize(bnns_graph_context_t, UnsafePointer<CChar>?, UInt64) -> Int32](bnnsgraphcontextsetbatchsize(_:_:_:).md)
  Sets the batch size for a graph.
- [func setDynamicShapes([BNNSGraph.Shape], forFunction: String?) async throws -> [BNNSGraph.Shape]](bnnsgraph/context/setdynamicshapes(_:forfunction:).md)
  Specifies the dynamic shapes for a graph and, if possible, infers the output shapes.
- [BNNSGraph.Shape](bnnsgraph/shape.md)
  The specification of the shape of an argument.
- [func argumentCount(forFunction: String?) -> Int](bnnsgraph/context/argumentcount(forfunction:).md)
  Returns the number of arguments for the given function argument.
- [func argumentNames(forFunction: String?) -> [String]](bnnsgraph/context/argumentnames(forfunction:).md)
  Returns the names of arguments for the given function argument.
- [func argumentPosition(forFunction: String?, argument: String) -> Int](bnnsgraph/context/argumentposition(forfunction:argument:).md)
  Returns the index into the arguments array for the given function argument.
- [var functionCount: Int](bnnsgraph/context/functioncount.md)
  The number of input arguments for the given function argument.
- [var functionNames: [String]](bnnsgraph/context/functionnames.md)
  Returns the names of callable functions in the graph.
- [var checkForNaNsAndInfinities: Bool](bnnsgraph/context/checkfornansandinfinities.md)
  A Boolean value that specifies that the context checks intermediate tensors for NaNs and infinities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/setbatchsize(_:forfunction:))*