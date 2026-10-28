# BNNSGraphGetArgumentInterleaveFactors(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns the interleave factors for arguments, if present

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
func BNNSGraphGetArgumentInterleaveFactors(_ graph: bnns_graph_t, _ function: UnsafePointer<CChar>?, _ argument_count: Int, _ argument_interleave: UnsafeMutablePointer<UnsafePointer<UInt16>?>, _ argument_interleave_counts: UnsafeMutablePointer<Int>) -> Int32
```

```c
int BNNSGraphGetArgumentInterleaveFactors(bnns_graph_t graph, const char *function, size_t argument_count, const uint16_t **argument_interleave, size_t *argument_interleave_counts);
```

## Discussion

If any arguments to the function are specified with an interleave factor (e.g. using the `interleave` option to `tensor_buffer` in MIL), this function can be used to retrieve the interleave factor array.

Arguments:

- `graph`: object to query.
- `function`: function to query. It may be `NULL` if there is only one function.
- `argument_count`: number of elements in `argument_interleave` and in `argument_interleave_counts`.
- `argument_interleave`: array of pointers to interleave factors to populate. On exit `argument_interleave[i]` will be set to either:

  - `NULL` if argument `i` has no interleave factor; or
  - a pointer into the graph object containing the interleave factors that contains `argument_interleave_counts[i]` elements. Only the first [0, min(argument_count, argument_interleave)) entries are set.
- `argument_interleave_counts`: gives the size of the array pointed to by `argument_interleave[i]`, or is set to 0 if `argument_interleave[i]` is set to `NULL`.

Returns: 0 on success, nonzero on failure. Failure may be caused by either invalid values of `graph` or `function`.

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
- [func BNNSGraphGetFunctionCount(bnns_graph_t) -> Int](./bnnsgraphgetfunctioncount%28_%29.md)
  Returns the number of callable functions in the specified graph.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphgetargumentinterleavefactors(_:_:_:_:_:))*