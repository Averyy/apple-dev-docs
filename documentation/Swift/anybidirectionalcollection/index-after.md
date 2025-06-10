# index(after:)

**Framework**: Swift  
**Kind**: method

Returns the position immediately after the given index.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func index(after i: AnyBidirectionalCollection<Element>.Index) -> AnyBidirectionalCollection<Element>.Index
```

#### Return Value

The index value immediately after `i`.

#### Discussion

The successor of an index must be well defined. For an index `i` into a collection `c`, calling `c.index(after: i)` returns the same index every time.

## Parameters

- `i`: A valid index of the collection.   must be less than   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anybidirectionalcollection/index(after:))*