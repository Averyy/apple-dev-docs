# copyElements(from:)

**Framework**: Core AI  
**Kind**: method

Copies the elements from `sequence` into this view in row-major order.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@export(implementation)
mutating func copyElements(from sequence: some Sequence<Element>)
```

#### Discussion

The number of elements in `sequence` must be less than or equal to `layout.scalarCount`.

## Parameters

- `sequence`: The sequence to be copied from.

## See Also

- [func copyElements(fromContentsOf: some Collection<Element>)](ndarray/mutableview/copyelements(fromcontentsof:).md)
  Copies the elements from `collection` into this view in row-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutableview/copyelements(from:))*