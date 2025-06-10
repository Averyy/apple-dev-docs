# omitted

**Framework**: Foundation  
**Kind**: property

A time style with no time-related components represented.

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
static let omitted: Date.FormatStyle.TimeStyle
```

#### Discussion

If both the date style and time style are set to `omitted`, the time is represented using the default style of `shortened`.

## See Also

- [static let complete: Date.FormatStyle.TimeStyle](date/formatstyle/timestyle/complete.md)
  A time style with all components represented.
- [static let shortened: Date.FormatStyle.TimeStyle](date/formatstyle/timestyle/shortened.md)
  A shortened time style with only the hour, minute, and day period components represented.
- [static let standard: Date.FormatStyle.TimeStyle](date/formatstyle/timestyle/standard.md)
  A time style with all components except the time zone represented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/timestyle/omitted)*