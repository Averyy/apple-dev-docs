# indices(of:)

**Framework**: Swift  
**Kind**: method

Returns the indices within `self` where the memory represented by `other` is located, or `nil` if `other` is not located within `self`.

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
func indices(of other: borrowing Span<Element>) -> Range<Span<Element>.Index>?
```

#### Return Value

A range of indices within `self`, or `nil`

#### Discussion

- other: a span that may be a subrange of `self`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/span/indices(of:))*