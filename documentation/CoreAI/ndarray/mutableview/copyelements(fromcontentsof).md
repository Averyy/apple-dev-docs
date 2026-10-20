# copyElements(fromContentsOf:)

**Framework**: Core AI  
**Kind**: method  
**Role**: Instance Method

Copies the elements from `collection` into this view in row-major order.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@export(implementation)
mutating func copyElements(fromContentsOf collection: some Collection<Element>)
```

Available when `Element` conforms to `BitwiseCopyable`.

#### Discussion

The number of elements in `collection` must be less than or equal to `layout.scalarCount`.

## Parameters

- `collection`: The collection to be copied from.

## See Also

### Writing data
- [func copyElements(from: some Sequence<Element>)](./copyelements%28from%29.md)
  Copies the elements from `sequence` into this view in row-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutableview/copyelements(fromcontentsof:))*