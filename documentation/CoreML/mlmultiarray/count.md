# count

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The total number of elements in the multiarray.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var count: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger count;
```

## See Also

### Inspecting a multiarray
- [var dataType: MLMultiArrayDataType](./datatype.md)
  The underlying type of the multiarray.
- [var shape: [NSNumber]](./shape.md)
  The multiarray’s multidimensional shape as a number array in which each element’s value is the size of the corresponding dimension.
- [var strides: [NSNumber]](./strides.md)
  A number array in which each element is the number of memory locations that span the length of the corresponding dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/count)*