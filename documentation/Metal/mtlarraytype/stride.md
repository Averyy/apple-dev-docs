# stride

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The stride between array elements, in bytes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var stride: Int { get }
```

```objc
@property (readonly) NSUInteger stride;
```

## See Also

### Describing the array elements
- [var arrayLength: Int](./arraylength.md)
  The number of elements in the array.
- [var elementType: MTLDataType](./elementtype.md)
  The data type of the array’s elements.
- [var argumentIndexStride: Int](./argumentindexstride.md)
  The stride, in bytes, between argument indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlarraytype/stride)*