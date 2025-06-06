# executeFunction(_:arguments:)

**Framework**: Accelerate  
**Kind**: method

Executes the specified function using an array of input and output pointers.

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
func executeFunction<T>(_ function: String? = nil, arguments: [T]) throws where T : BNNSGraph.PointerArgument
```

## Parameters

- `function`: The function. Specify as   if the graph only contains one function.
- `arguments`: The output and input arguments. Note that the arguments may not be in the same order as the original   or   file. Use the   function to get the correct position in the   array for a given argument.

## See Also

- [func executeFunction(String?, arguments: inout [BNNSTensor]) async throws](bnnsgraph/context/executefunction(_:arguments:)-8bhcn.md)
  Executes the specified function using an array of input and output tensors.
- [BNNSGraph.PointerArgument](bnnsgraph/pointerargument.md)
  A type that BNNS Graph accepts as an input-output argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/executefunction(_:arguments:)-95snr)*