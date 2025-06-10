# index(after:)

**Framework**: Swift  
**Kind**: method

Returns the position immediately after the given index.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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