# index(after:)

**Framework**: Swift  
**Kind**: method

Returns the position immediately after the given index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func index(after index: CollectionDifference<ChangeElement>.Index) -> CollectionDifference<ChangeElement>.Index
```

#### Return Value

The index value immediately after `i`.

#### Discussion

The successor of an index must be well defined. For an index `i` into a collection `c`, calling `c.index(after: i)` returns the same index every time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectiondifference/index(after:))*