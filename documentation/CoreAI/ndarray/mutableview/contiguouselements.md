# contiguousElements

**Framework**: Core AI  
**Kind**: property

Returns a `MutableSpan` over the backing memory of this view if the memory is in a contiguous layout, otherwise returns `nil`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@export(implementation)
var contiguousElements: MutableSpan<Element>? { mutating get }
```

#### Discussion

> **Note**: `contiguous` here refers to elements in row-major order with zero padding.

## See Also

- [subscript<let rank : Int>(scalarAt _: InlineArray<rank, Int>) -> Element](ndarray/mutableview/subscript(scalarat:).md)
  Access the element at a multi-dimensional `index`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutableview/contiguouselements)*