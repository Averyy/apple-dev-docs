# byteOffsets(of:)

**Framework**: Swift  
**Kind**: method

Returns the offsets where the memory of `other` is located within the memory represented by `self`

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

A range of offsets within `self`

#### Discussion

Note: `other` must be a subrange of `self`

## Parameters

- `other`: A subrange of 


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawspan/byteoffsets(of:))*