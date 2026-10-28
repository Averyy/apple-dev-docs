# BNNSTensorGetAllocationSize(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns the minimum allocation size, in bytes, of the specified tensor.

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
func BNNSTensorGetAllocationSize(_ tensor: UnsafePointer<BNNSTensor>) -> Int
```

```c
size_t BNNSTensorGetAllocationSize(const BNNSTensor *tensor);
```

## Return Value

The minimum allocation size, in bytes, of the specified tensor.

## Parameters

- `tensor`: The tensor.

## See Also

### Specifying and querying a tensor’s properties
- [struct BNNSTensor](./bnnstensor.md)
  A structure that describes the shape, stride, data type, and, optionally, the memory location of an n-dimensional array.
- [func BNNSGraphContextGetTensor(bnns_graph_context_t, UnsafePointer<CChar>?, UnsafePointer<CChar>, Bool, UnsafeMutablePointer<BNNSTensor>) -> Int32](./bnnsgraphcontextgettensor%28_,_,_,_,_%29.md)
  Sets the properties of a tensor for the specified function argument.
- [func BNNSGraphTensorFillStrides(bnns_graph_t, UnsafePointer<CChar>?, UnsafePointer<CChar>, UnsafeMutablePointer<BNNSTensor>) -> Int32](./bnnsgraphtensorfillstrides%28_,_,_,_%29.md)
  Sets the stride of the specifed tensor for compatibility with the given model’s input or output argument based on its current shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnstensorgetallocationsize(_:))*