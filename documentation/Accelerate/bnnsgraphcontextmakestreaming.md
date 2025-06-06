# BNNSGraphContextMakeStreaming(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns an allocated and initialized graph context with streaming support from the specified graph.

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
func BNNSGraphContextMakeStreaming(_ graph: bnns_graph_t, _ function: UnsafePointer<CChar>?, _ initial_states_count: Int, _ initial_states: UnsafePointer<BNNSTensor>?) -> bnns_graph_context_t
```

#### Return Value

A compiled graph context object. If the operation fails, the graph object’s [`data`](bnns_graph_context_t/data.md) property is `nil`.

#### Discussion

In addition to the work that [`BNNSGraphContextMake(_:)`](bnnsgraphcontextmake(_:).md) performs, this call allocates ring-buffer backed memory for all [`Core ML`](https://developer.apple.com/documentation/CoreML) state arguments of the given function.

If your model runs on a stream of data, such as processing audio data, it may benefit from working on one frame at a time. You can express this functionality through a model that uses Core ML’s concept of states. In this case, BNNS stores information that the model needs from a previous frame in the state that dilations on convolution layers may require.

If your model uses the pattern below, use this function to specify that BNNS uses an optimized mode that allocates and manages ring buffers for states. Doing so eliminates memory copies associated with the approach.

```c
output_state = concat(input_state, tensorX)
```

BNNS advances the ring buffer by the size of `tensorX` in the concatenation dimension after the function executes.

To use a context with streaming support, your function must include an attribute dictionary named `BNNSOptions` that includes the entry `{ ‘StateMode’: ‘Streaming’ }`. This specifies that the [`BNNSGraphCompileFromFile(_:_:_:)`](bnnsgraphcompilefromfile(_:_:_:).md) function encodes additional metadata into the graph that describes the streaming rate.

Calls to [`BNNSGraphContextExecute(_:_:_:_:_:_:)`](bnnsgraphcontextexecute(_:_:_:_:_:_:).md) that use contexts this function creates ignore any user-provided pointers for input and output arguments. Instead, context execution uses the internal ring buffer and updates any nonnull input and output arguments to point to the same ring-buffer backed memory. On return, an analysis of the compiled program for use in the next frame determines the distance by which the operation advances the ring buffer.

To prevent memory leaks, call [`BNNSGraphContextDestroy(_:)`](bnnsgraphcontextdestroy(_:).md) when you’re finished using the graph context.

## Parameters

- `graph`: The compiled graph object.
- `function`: The function that the new context initializes the state for. Specify as   if the graph only contains one function.
- `initial_states_count`: The number of elements in the   array.
- `initial_states`: An array of   structures that describe the data that the context uses to initialize each state. The context uses   to intialize the state with the name  .

## See Also

- [struct bnns_graph_context_t](bnns_graph_context_t.md)
  An object that wraps a compiled graph object.
- [func BNNSGraphContextMake(bnns_graph_t) -> bnns_graph_context_t](bnnsgraphcontextmake(_:).md)
  Returns an allocated and initialized graph context from the specified graph.
- [func BNNSGraphContextDestroy(bnns_graph_context_t)](bnnsgraphcontextdestroy(_:).md)
  Destroys the specified graph context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraphcontextmakestreaming(_:_:_:_:))*