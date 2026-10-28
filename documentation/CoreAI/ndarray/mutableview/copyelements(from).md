# copyElements(from:)

**Framework**: Core AI  
**Kind**: method  
**Role**: Instance Method

Copies the elements from `sequence` into this view in row-major order.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@export(implementation)
mutating func copyElements(from sequence: some Sequence<Element>)
```

Available when `Element` conforms to `BitwiseCopyable`.

## Discussion

The number of elements in `sequence` must be less than or equal to `layout.scalarCount`.

## Parameters

- `sequence`: The sequence to be copied from.

## See Also

### Writing data
- [func copyElements(fromContentsOf: some Collection<Element>)](./copyelements%28fromcontentsof%29.md)
  Copies the elements from `collection` into this view in row-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutableview/copyelements(from:))*