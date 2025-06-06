# index(after:)

**Framework**: RealityKit  
**Kind**: method

Returns the position immediately after the given index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func index(after i: Int) -> Int
```

#### Return Value

The index value immediately after `i`.

#### Discussion

The successor of an index must be well defined. For an index `i` into a collection `c`, calling `c.index(after: i)` returns the same index every time.

## Parameters

- `i`: A valid index of the collection.   must be less than   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsjoints/index(after:))*