# shape

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

An array of unsigned-integer elements that specify the size of the shape.

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
var shape: UnsafeMutablePointer<UInt64>?
```

```c
uint64_t * shape;
```

## See Also

### Specifying a shape’s properties
- [var rank: Int](./rank.md)
  The rank of the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns_graph_shape_t/shape)*