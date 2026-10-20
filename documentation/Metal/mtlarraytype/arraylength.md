# arrayLength

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The number of elements in the array.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var arrayLength: Int { get }
```

```objc
@property (readonly) NSUInteger arrayLength;
```

## See Also

### Related Documentation
- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
### Describing the array elements
- [var elementType: MTLDataType](./elementtype.md)
  The data type of the array’s elements.
- [var stride: Int](./stride.md)
  The stride between array elements, in bytes.
- [var argumentIndexStride: Int](./argumentindexstride.md)
  The stride, in bytes, between argument indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlarraytype/arraylength)*