# setDynamicShapes(_:forFunction:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Specifies the dynamic shapes for a graph and, if possible, infers the output shapes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS
- watchOS 11.0+

## Declaration

```swift
func setDynamicShapes(_ shapes: [BNNSGraph.Shape], forFunction function: String? = nil) async throws -> [BNNSGraph.Shape]
```

## Parameters

- `shapes`: An array of input shapes in the same order as you pass to [`BNNSGraphContextExecute(_:_:_:_:_:_:)`](../../bnnsgraphcontextexecute%28_,_,_,_,_,_%29.md).

  This function reads input shapes with a nonzero rank, and uses the constant or default value from the source model for input shapes with a zero rank. The function generates an error for shapes with a nonzero value that doesn’t match the source model.
- `function`: The function. Specify as `nil` if the graph only contains one function.

## See Also

### Related Documentation
- [func BNNSGraphContextSetDynamicShapes(bnns_graph_context_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<bnns_graph_shape_t>) -> Int32](../../bnnsgraphcontextsetdynamicshapes%28_,_,_,_%29.md)
  Specifies the dynamic shapes for a graph and, if possible, infers, the output shapes.
### Specifying and querying a graph context’s properties
- [BNNSGraph.Shape](../shape.md)
  The specification of the shape of an argument.
- [func argumentCount(forFunction: String?) -> Int](./argumentcount%28forfunction%29.md)
  Returns the number of arguments for the given function argument.
- [func argumentNames(forFunction: String?) -> [String]](./argumentnames%28forfunction%29.md)
  Returns the names of arguments for the given function argument.
- [func argumentPosition(forFunction: String?, argument: String) -> Int](./argumentposition%28forfunction,argument%29.md)
  Returns the index into the arguments array for the given function argument.
- [var functionCount: Int](./functioncount.md)
  The number of input arguments for the given function argument.
- [var functionNames: [String]](./functionnames.md)
  Returns the names of callable functions in the graph.
- [var checkForNaNsAndInfinities: Bool](./checkfornansandinfinities.md)
  A Boolean value that specifies that the context checks intermediate tensors for NaNs and infinities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/setdynamicshapes(_:forfunction:))*