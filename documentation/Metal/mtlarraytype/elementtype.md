# elementType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The data type of the array’s elements.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var elementType: MTLDataType { get }
```

```objc
@property (readonly) MTLDataType elementType;
```

#### Discussion

For information on possible values, see [`MTLDataType`](../mtldatatype.md).

## See Also

### Describing the array elements
- [var arrayLength: Int](./arraylength.md)
  The number of elements in the array.
- [var stride: Int](./stride.md)
  The stride between array elements, in bytes.
- [var argumentIndexStride: Int](./argumentindexstride.md)
  The stride, in bytes, between argument indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlarraytype/elementtype)*