# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

Returns a discontiguous substring of this discontiguous attributed string using a range to indicate the discontiguous substring bounds.

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
subscript(bounds: some RangeExpression<AttributedString.Index>) -> DiscontiguousAttributedSubstring { get }
```

## Parameters

- `bounds`: A range that indicates the bounds of the discontiguous substring to return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/discontiguousattributedsubstring/subscript(_:)-6j670)*