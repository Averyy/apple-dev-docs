# abbreviated

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A date style with some components abbreviated for space-constrained applications.

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
static let abbreviated: Date.FormatStyle.DateStyle
```

#### Discussion

A shortened date style that presents an abbreviated month, day of month, and year components of a date. For example, `Oct 17, 2020`, for locale `en_US`.

## See Also

### Modifying a Date Style
- [static let complete: Date.FormatStyle.DateStyle](./complete.md)
  A date style with all components represented.
- [static let long: Date.FormatStyle.DateStyle](./long.md)
  A lengthened date style with the full month, day of month, and year components represented.
- [static let numeric: Date.FormatStyle.DateStyle](./numeric.md)
  A date style with the month, day of month, and year components represented as numeric values.
- [static let omitted: Date.FormatStyle.DateStyle](./omitted.md)
  A date style with no date-related components represented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/datestyle/abbreviated)*