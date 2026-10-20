# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript  
**Role**: Instance Subscript  
**Required**: Yes

Returns a substring of the attributed string using a range to indicate the substring bounds.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
subscript<R>(bounds: R) -> AttributedSubstring where R : RangeExpression, R.Bound == AttributedString.Index { get }
```

## Default Implementations

### AttributedStringProtocol Implementations
- [subscript(RangeSet<AttributedString.Index>) -> DiscontiguousAttributedSubstring](./subscript%28_%29-67hgv.md)
  Returns a discontiguous substring of this attributed string using a set of ranges to indicate the discontiguous substring bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringprotocol/subscript(_:)-109me)*