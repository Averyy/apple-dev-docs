# BNNSGraph.PointerArgument

**Framework**: Accelerate  
**Kind**: protocol

A type that BNNS Graph accepts as an input-output argument.

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
protocol PointerArgument
```

## Topics

### Querying a pointer argument’s properties
- [var baseAddress: UnsafeMutablePointer<Self.Element>?](bnnsgraph/pointerargument/baseaddress.md)
  A pointer to the first element of the buffer.
- [var count: Int](bnnsgraph/pointerargument/count.md)
  The number of elements in the buffer.
### Associated Types
- [associatedtype Element](bnnsgraph/pointerargument/element.md)
  The pointer argument’s element type.

## See Also

- [func executeFunction(String?, arguments: inout [BNNSTensor]) async throws](bnnsgraph/context/executefunction(_:arguments:)-8bhcn.md)
  Executes the specified function using an array of input and output tensors.
- [func executeFunction<T>(String?, arguments: [T]) throws](bnnsgraph/context/executefunction(_:arguments:)-95snr.md)
  Executes the specified function using an array of input and output pointers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/pointerargument)*