# copyElements(fromContentsOf:)

**Framework**: Core AI  
**Kind**: method

Copies the elements from `collection` into this view in row-major order.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@export(implementation)
mutating func copyElements(fromContentsOf collection: some Collection<Element>)
```

#### Discussion

The number of elements in `collection` must be less than or equal to `layout.scalarCount`.

## Parameters

- `collection`: The collection to be copied from.

## See Also

- [func copyElements(from: some Sequence<Element>)](ndarray/mutableview/copyelements(from:).md)
  Copies the elements from `sequence` into this view in row-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutableview/copyelements(fromcontentsof:))*