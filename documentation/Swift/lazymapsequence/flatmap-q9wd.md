# flatMap(_:)

**Framework**: Swift  
**Kind**: method

Returns the concatenated results of mapping the given transformation over this sequence.

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
func flatMap<SegmentOfResult>(_ transform: @escaping (Self.Elements.Element) -> SegmentOfResult) -> LazySequence<FlattenSequence<LazyMapSequence<Self.Elements, SegmentOfResult>>> where SegmentOfResult : Sequence
```

#### Discussion

Use this method to receive a single-level sequence when your transformation produces a sequence or collection for each element. Calling `flatMap(_:)` on a sequence `s` is equivalent to calling `s.map(transform).joined()`.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazymapsequence/flatmap(_:)-q9wd)*