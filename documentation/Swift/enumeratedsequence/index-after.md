# index(after:)

**Framework**: Swift  
**Kind**: method

Returns the position immediately after the given index.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func index(after index: EnumeratedSequence<Base>.Index) -> EnumeratedSequence<Base>.Index
```

#### Return Value

The index value immediately after `i`.

#### Discussion

The successor of an index must be well defined. For an index `i` into a collection `c`, calling `c.index(after: i)` returns the same index every time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratedsequence/index(after:))*