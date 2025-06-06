# tensor(forFunction:argument:fillKnownDynamicShapes:)

**Framework**: Accelerate  
**Kind**: method

Returns an unallocated tensor for a given function argument.

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
func tensor(forFunction function: String? = nil, argument: String, fillKnownDynamicShapes: Bool) -> BNNSTensor?
```

## Parameters

- `function`: The function. Specify as   if the graph only contains one function.
- `argument`: The name of the input or output argument.
- `fillKnownDynamicShapes`: A Boolean value that specifies whether the function should replace any dynamic shapes for the next execution of the context. BNNS derives these shapes either from the default shapes in the source model, or from preceding calls to   or  . If BNNS is unable to derive the shapes, the function sets the dimensions to  .

## See Also

- [func BNNSGraphContextGetTensor(bnns_graph_context_t, UnsafePointer<CChar>?, UnsafePointer<CChar>, Bool, UnsafeMutablePointer<BNNSTensor>) -> Int32](bnnsgraphcontextgettensor(_:_:_:_:_:).md)
  Sets the properties of a tensor for the specified function argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/tensor(forfunction:argument:fillknowndynamicshapes:))*