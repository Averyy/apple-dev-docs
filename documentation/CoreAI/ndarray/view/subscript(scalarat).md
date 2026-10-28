# subscript(scalarAt:)

**Framework**: Core AI  
**Kind**: subscript  
**Role**: Instance Subscript

Access the element at a multi-dimensional `index`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
subscript<let rank : Int>(scalarAt index: InlineArray<rank, Int>) -> Element { get }
```

Available when `Element` conforms to `BitwiseCopyable`.

## Overview

> **Note**: `rank` must be equal to the `rank` of this view.

## Parameters

- `index`: The multi-dimensional index of the element to access. It must have the same count as rank of this view.

## See Also

### Accessing elements
- [var contiguousElements: Span<Element>?](./contiguouselements.md)
  Returns a `Span` over the backing memory of this view if the memory is in a contiguous layout, otherwise returns `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/view/subscript(scalarat:))*