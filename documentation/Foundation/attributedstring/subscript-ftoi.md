# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

Returns a discontiguous substring of this discontiguous attributed string using a set of ranges to indicate the discontiguous substring bounds.

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
subscript(indices: RangeSet<AttributedString.Index>) -> DiscontiguousAttributedSubstring { get set }
```

## Parameters

- `indices`: A set of ranges that indicate the bounds of the discontiguous substring to return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/subscript(_:)-ftoi)*