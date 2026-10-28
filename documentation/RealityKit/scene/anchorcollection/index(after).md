# index(after:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns the position immediately after the given index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func index(after i: Int) -> Int
```

## Return Value

The index value immediately after i.

## Parameters

- `i`: A valid index of the collection. Use a value less than [`endIndex`](./endindex.md).

## See Also

### Manipulating indices
- [Scene.AnchorCollection.Index](./index.md)
  A type that represents a position in the collection.
- [var startIndex: Int](./startindex.md)
  The position of the first element in a nonempty collection.
- [var endIndex: Int](./endindex.md)
  The position one greater than the last valid subscript argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/index(after:))*