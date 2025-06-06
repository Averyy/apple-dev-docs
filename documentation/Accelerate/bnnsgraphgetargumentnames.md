# BNNSGraphGetArgumentNames(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Extracts the names of arguments for the given function argument.

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
func BNNSGraphGetArgumentNames(_ graph: bnns_graph_t, _ function: UnsafePointer<CChar>?, _ argument_names_count: Int, _ argument_names: UnsafeMutablePointer<UnsafePointer<CChar>?>) -> Int32
```

#### Return Value

`0` on success, nonzero on failure.

#### Discussion

This function is the equivalent of the concatenation of [`BNNSGraphGetOutputNames(_:_:_:_:)`](bnnsgraphgetoutputnames(_:_:_:_:).md) and [`BNNSGraphGetInputNames(_:_:_:_:)`](bnnsgraphgetinputnames(_:_:_:_:).md).

## Parameters

- `graph`: The compiled graph object.
- `function`: The function. Specify as   if the graph only contains one function.
- `argument_names_count`: The number of elements in the   array.
- `argument_names`: On output, an array of pointers to strings that contain the argument names.

## See Also

- [func BNNSGraphGetArgumentIntents(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<BNNSGraphArgumentIntent>) -> Int32](bnnsgraphgetargumentintents(_:_:_:_:).md)
  Extracts the intents of arguments for the given function argument.
- [struct BNNSGraphArgumentIntent](bnnsgraphargumentintent.md)
  Constants that describe argument intents.
- [func BNNSGraphGetArgumentCount(bnns_graph_t, UnsafePointer<CChar>?) -> Int](bnnsgraphgetargumentcount(_:_:).md)
  Returns the number of arguments for the given function argument.
- [func BNNSGraphGetFunctionCount(bnns_graph_t) -> Int](bnnsgraphgetfunctioncount(_:).md)
  Returns the number of callable functions in the specified graph.
- [func BNNSGraphGetFunctionNames(bnns_graph_t, Int, UnsafeMutablePointer<UnsafePointer<CChar>?>) -> Int32](bnnsgraphgetfunctionnames(_:_:_:).md)
  Extracts the names of callable functions in the graph.
- [func BNNSGraphGetInputCount(bnns_graph_t, UnsafePointer<CChar>?) -> Int](bnnsgraphgetinputcount(_:_:).md)
  Returns the number of input arguments for the given function argument.
- [func BNNSGraphGetInputNames(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<UnsafePointer<CChar>?>) -> Int32](bnnsgraphgetinputnames(_:_:_:_:).md)
  Extracts the names of input arguments for the given function argument.
- [func BNNSGraphGetOutputCount(bnns_graph_t, UnsafePointer<CChar>?) -> Int](bnnsgraphgetoutputcount(_:_:).md)
  Returns the number of output arguments for the given function argument.
- [func BNNSGraphGetOutputNames(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<UnsafePointer<CChar>?>) -> Int32](bnnsgraphgetoutputnames(_:_:_:_:).md)
  Extracts the names of output arguments for the given function argument.
- [func BNNSGraphGetArgumentPosition(bnns_graph_t, UnsafePointer<CChar>?, UnsafePointer<CChar>) -> Int](bnnsgraphgetargumentposition(_:_:_:).md)
  Returns the index into the arguments array for the given function argument.
- [func BNNSGraphGetArgumentInterleaveFactors(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<UnsafePointer<UInt16>?>, UnsafeMutablePointer<Int>) -> Int32](bnnsgraphgetargumentinterleavefactors(_:_:_:_:_:).md)
  Returns the interleave factors for arguments, if present


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphgetargumentnames(_:_:_:_:))*