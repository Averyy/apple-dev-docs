# omitted

**Framework**: Foundation  
**Kind**: property

A date style with no date-related components represented.

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
static let omitted: Date.FormatStyle.DateStyle
```

#### Discussion

If both the date style and time style are set to `omitted`, the date is represented using the default style of `abbreviated`.

## See Also

- [static let abbreviated: Date.FormatStyle.DateStyle](date/formatstyle/datestyle/abbreviated.md)
  A date style with some components abbreviated for space-constrained applications.
- [static let complete: Date.FormatStyle.DateStyle](date/formatstyle/datestyle/complete.md)
  A date style with all components represented.
- [static let long: Date.FormatStyle.DateStyle](date/formatstyle/datestyle/long.md)
  A lengthened date style with the full month, day of month, and year components represented.
- [static let numeric: Date.FormatStyle.DateStyle](date/formatstyle/datestyle/numeric.md)
  A date style with the month, day of month, and year components represented as numeric values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/datestyle/omitted)*