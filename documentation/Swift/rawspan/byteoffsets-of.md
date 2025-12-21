# byteOffsets(of:)

**Framework**: Swift  
**Kind**: method

Returns the offsets where the memory of `span` is located within the memory represented by `self`

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

#### Discussion

Note: `span` must be a subrange of `self`

Parameters:

- span: a subrange of `self` Returns: A range of offsets within `self`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawspan/byteoffsets(of:))*