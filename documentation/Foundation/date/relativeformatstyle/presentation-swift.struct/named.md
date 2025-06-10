# named

**Framework**: Foundation  
**Kind**: property

A style that uses named styles to describe relative dates, such as “yesterday”, “last week”, or “next week”.

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
static var named: Date.RelativeFormatStyle.Presentation { get }
```

#### Discussion

The format uses the [`numeric`](date/relativeformatstyle/presentation-swift.struct/numeric.md) style if a name isn’t available.

## See Also

- [static var numeric: Date.RelativeFormatStyle.Presentation](date/relativeformatstyle/presentation-swift.struct/numeric.md)
  A style that uses a numeric style to describe relative dates, such as “1 day ago” or “in 3 weeks”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/relativeformatstyle/presentation-swift.struct/named)*