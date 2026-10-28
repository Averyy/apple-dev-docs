# BNNSGraphGetFunctionCount(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns the number of callable functions in the specified graph.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func BNNSGraphGetFunctionCount(_ graph: bnns_graph_t) -> Int
```

```c
size_t BNNSGraphGetFunctionCount(bnns_graph_t graph);
```

## Return Value

The number of callable functions in the specified graph, or `SIZE_T_MAX` if the query fails.

## Parameters

- `graph`: The compiled graph object.

## See Also

### Querying a graph’s properties
- [func BNNSGraphGetArgumentIntents(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<BNNSGraphArgumentIntent>) -> Int32](./bnnsgraphgetargumentintents%28_,_,_,_%29.md)
  Extracts the intents of arguments for the given function argument.
- [struct BNNSGraphArgumentIntent](./bnnsgraphargumentintent.md)
  Constants that describe argument intents.
- [func BNNSGraphGetArgumentCount(bnns_graph_t, UnsafePointer<CChar>?) -> Int](./bnnsgraphgetargumentcount%28_,_%29.md)
  Returns the number of arguments for the given function argument.
- [func BNNSGraphGetArgumentNames(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<UnsafePointer<CChar>?>) -> Int32](./bnnsgraphgetargumentnames%28_,_,_,_%29.md)
  Extracts the names of arguments for the given function argument.
- [func BNNSGraphGetFunctionNames(bnns_graph_t, Int, UnsafeMutablePointer<UnsafePointer<CChar>?>) -> Int32](./bnnsgraphgetfunctionnames%28_,_,_%29.md)
  Extracts the names of callable functions in the graph.
- [func BNNSGraphGetInputCount(bnns_graph_t, UnsafePointer<CChar>?) -> Int](./bnnsgraphgetinputcount%28_,_%29.md)
  Returns the number of input arguments for the given function argument.
- [func BNNSGraphGetInputNames(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<UnsafePointer<CChar>?>) -> Int32](./bnnsgraphgetinputnames%28_,_,_,_%29.md)
  Extracts the names of input arguments for the given function argument.
- [func BNNSGraphGetOutputCount(bnns_graph_t, UnsafePointer<CChar>?) -> Int](./bnnsgraphgetoutputcount%28_,_%29.md)
  Returns the number of output arguments for the given function argument.
- [func BNNSGraphGetOutputNames(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<UnsafePointer<CChar>?>) -> Int32](./bnnsgraphgetoutputnames%28_,_,_,_%29.md)
  Extracts the names of output arguments for the given function argument.
- [func BNNSGraphGetArgumentPosition(bnns_graph_t, UnsafePointer<CChar>?, UnsafePointer<CChar>) -> Int](./bnnsgraphgetargumentposition%28_,_,_%29.md)
  Returns the index into the arguments array for the given function argument.
- [func BNNSGraphGetArgumentInterleaveFactors(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<UnsafePointer<UInt16>?>, UnsafeMutablePointer<Int>) -> Int32](./bnnsgraphgetargumentinterleavefactors%28_,_,_,_,_%29.md)
  Returns the interleave factors for arguments, if present


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphgetfunctioncount(_:))*