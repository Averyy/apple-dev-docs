# checkForNaNsAndInfinities

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies that the context checks intermediate tensors for NaNs and infinities.

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
var checkForNaNsAndInfinities: Bool { get set }
```

## See Also

### Related Documentation
- [func BNNSGraphContextEnableNanAndInfChecks(bnns_graph_context_t, Bool)](../../bnnsgraphcontextenablenanandinfchecks%28_,_%29.md)
  Specifies that the context checks intermediate tensors for NaNs and infinities.
### Specifying and querying a graph context’s properties
- [func setDynamicShapes([BNNSGraph.Shape], forFunction: String?) async throws -> [BNNSGraph.Shape]](./setdynamicshapes%28_,forfunction%29.md)
  Specifies the dynamic shapes for a graph and, if possible, infers the output shapes.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/checkfornansandinfinities)*