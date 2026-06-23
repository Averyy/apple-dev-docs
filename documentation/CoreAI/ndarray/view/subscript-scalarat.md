# subscript(scalarAt:)

**Framework**: Core AI  
**Kind**: subscript

Access the element at a multi-dimensional `index`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
subscript<let rank : Int>(scalarAt index: InlineArray<rank, Int>) -> Element { get }
```

#### Overview

> **Note**: `rank` must be equal to the `rank` of this view.

## Parameters

- `index`: The multi-dimensional index of the element to access. It must have the same count as rank of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/view/subscript(scalarat:))*