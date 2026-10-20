# argumentPosition(forFunction:argument:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Returns the index into the arguments array for the given function argument.

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
func argumentPosition(forFunction function: String? = nil, argument: String) -> Int
```

## Parameters

- `function`: The function. Specify as `nil` if the graph only contains one function.
- `argument`: The name of the input or output argument.

## See Also

### Related Documentation
- [func BNNSGraphGetArgumentPosition(bnns_graph_t, UnsafePointer<CChar>?, UnsafePointer<CChar>) -> Int](../../bnnsgraphgetargumentposition%28_,_,_%29.md)
  Returns the index into the arguments array for the given function argument.
### Specifying and querying a graph context’s properties
- [func setDynamicShapes([BNNSGraph.Shape], forFunction: String?) async throws -> [BNNSGraph.Shape]](./setdynamicshapes%28_,forfunction%29.md)
  Specifies the dynamic shapes for a graph and, if possible, infers the output shapes.
- [BNNSGraph.Shape](../shape.md)
  The specification of the shape of an argument.
- [func argumentCount(forFunction: String?) -> Int](./argumentcount%28forfunction%29.md)
  Returns the number of arguments for the given function argument.
- [func argumentNames(forFunction: String?) -> [String]](./argumentnames%28forfunction%29.md)
  Returns the names of arguments for the given function argument.
- [var functionCount: Int](./functioncount.md)
  The number of input arguments for the given function argument.
- [var functionNames: [String]](./functionnames.md)
  Returns the names of callable functions in the graph.
- [var checkForNaNsAndInfinities: Bool](./checkfornansandinfinities.md)
  A Boolean value that specifies that the context checks intermediate tensors for NaNs and infinities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/argumentposition(forfunction:argument:))*