# BNNSGraphArgumentIntent

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that describe argument intents.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSGraphArgumentIntent
```

```c
typedef enum { ... } BNNSGraphArgumentIntent;
```

## Topics

### Argument intents
- [init(UInt32)](./bnnsgraphargumentintent/init%28_%29.md)
  Creates a new instance.
- [init(rawValue: UInt32)](./bnnsgraphargumentintent/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
- [var rawValue: UInt32](./bnnsgraphargumentintent/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSGraphArgumentIntentIn: BNNSGraphArgumentIntent](./bnnsgraphargumentintentin.md)
  A constant that specifies the argument provides an input tensor.
- [var BNNSGraphArgumentIntentOut: BNNSGraphArgumentIntent](./bnnsgraphargumentintentout.md)
  A constant that specifies the argument provides an output tensor.
- [var BNNSGraphArgumentIntentInOut: BNNSGraphArgumentIntent](./bnnsgraphargumentintentinout.md)
  A constant that specifies the argument is an in-place input and output tensor.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Querying a graph’s properties
- [func BNNSGraphGetArgumentIntents(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<BNNSGraphArgumentIntent>) -> Int32](./bnnsgraphgetargumentintents%28_,_,_,_%29.md)
  Extracts the intents of arguments for the given function argument.
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
- [func BNNSGraphGetArgumentInterleaveFactors(bnns_graph_t, UnsafePointer<CChar>?, Int, UnsafeMutablePointer<UnsafePointer<UInt16>?>, UnsafeMutablePointer<Int>) -> Int32](./bnnsgraphgetargumentinterleavefactors%28_,_,_,_,_%29.md)
  Returns the interleave factors for arguments, if present


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphargumentintent)*