# BNNSGraph.PointerArgument

**Framework**: Accelerate  
**Kind**: protocol  
**Role**: Protocol

A type that BNNS Graph accepts as an input-output argument.

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
protocol PointerArgument
```

## Topics

### Querying a pointer argument’s properties
- [var baseAddress: UnsafeMutablePointer<Self.Element>?](./pointerargument/baseaddress.md)
  A pointer to the first element of the buffer.
- [var count: Int](./pointerargument/count.md)
  The number of elements in the buffer.
### Associated Types
- [associatedtype Element](./pointerargument/element.md)
  The pointer argument’s element type.

## See Also

### Executing a graph
- [func executeFunction(String?, arguments: inout [BNNSTensor]) async throws](./context/executefunction%28_,arguments%29-8bhcn.md)
  Executes the specified function using an array of input and output tensors.
- [func executeFunction<T>(String?, arguments: [T]) throws](./context/executefunction%28_,arguments%29-95snr.md)
  Executes the specified function using an array of input and output pointers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/pointerargument)*