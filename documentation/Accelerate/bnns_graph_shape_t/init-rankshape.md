# init(rank:shape:)

**Framework**: Accelerate  
**Kind**: init

Creates a shape structure with the specified rank and dimensions.

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
init(rank: Int, shape: UnsafeMutablePointer<UInt64>?)
```

## Parameters

- `rank`: The rank of the tensor and number of elements in array shape.
- `shape`: Array with a count of   that contains the sizes of each dimension.

## See Also

- [init()](bnns_graph_shape_t/init.md)
  Creates an empty shape structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns_graph_shape_t/init(rank:shape:))*