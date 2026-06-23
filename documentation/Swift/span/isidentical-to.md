# isIdentical(to:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether two instances refer to the same memory region.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
func isIdentical(to other: Span<Element>) -> Bool
```

#### Return Value

Whether `self` and `other` reference the same region in memory.

#### Discussion

Two spans are identical if they reference the same starting address and have the same number of elements.

> **Note**: O(1)

## Parameters

- `other`: A span to compare with this one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/span/isidentical(to:))*