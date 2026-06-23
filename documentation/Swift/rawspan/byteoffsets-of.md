# byteOffsets(of:)

**Framework**: Swift  
**Kind**: method

Returns the byte offsets within this span where the memory represented by other is located, or nil if other is not located within this span.

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
func byteOffsets(of other: borrowing RawSpan) -> Range<Int>?
```

#### Return Value

A range of byte offsets within `self`, or `nil`.

## Parameters

- `other`: A span that may be a subrange of `self`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawspan/byteoffsets(of:))*