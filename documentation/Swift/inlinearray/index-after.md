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
borrowing func index(after i: InlineArray<count, Element>.Index) -> InlineArray<count, Element>.Index
```

#### Return Value

The index immediately after `i`.

#### Discussion

> **Note**: O(1)

## Parameters

- `i`: A valid index of the array.   must be less than   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/inlinearray/index(after:))*