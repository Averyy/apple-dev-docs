# elements(inBoundingRectMin:rectMax:)

**Framework**: GameplayKit  
**Kind**: method

Searches the tree and returns all elements found within the specified bounding region.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func elements(inBoundingRectMin rectMin: vector_float2, rectMax: vector_float2) -> [ElementType]
```

#### Return Value

An array of objects stored in the tree whose bounding regions overlap the specified region. The array is empty if no such objects are found.

## Parameters

- `rectMin`: The corner (with the lowest x- and y-coordinate values) of the bounding region to search.
- `rectMax`: The corner (with the highest x- and y-coordinate values) of the bounding region to search.

## See Also

- [var queryReserve: Int](gkrtree/queryreserve.md)
  The number of elements to reserve space for when searching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrtree/elements(inboundingrectmin:rectmax:))*