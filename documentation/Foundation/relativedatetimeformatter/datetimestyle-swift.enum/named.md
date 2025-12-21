# RelativeDateTimeFormatter.DateTimeStyle.named

**Framework**: Foundation  
**Kind**: case

A style that uses named styles to describe relative dates, such as “yesterday”, “last week”, or “next week”.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case named
```

#### Discussion

The formatter falls back to using [`RelativeDateTimeFormatter.DateTimeStyle.numeric`](relativedatetimeformatter/datetimestyle-swift.enum/numeric.md) if a name isn’t available.

## See Also

- [RelativeDateTimeFormatter.DateTimeStyle.numeric](relativedatetimeformatter/datetimestyle-swift.enum/numeric.md)
  A style that uses a numeric style to describe relative dates, such as “1 day ago” or “in 3 weeks”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/relativedatetimeformatter/datetimestyle-swift.enum/named)*