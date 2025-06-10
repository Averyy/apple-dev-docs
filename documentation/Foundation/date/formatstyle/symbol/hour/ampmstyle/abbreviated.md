# abbreviated

**Framework**: Foundation  
**Kind**: property

A type that specifies the abbreviated day period for when the locale prefers using day period with hour.

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
static let abbreviated: Date.FormatStyle.Symbol.Hour.AMPMStyle
```

#### Discussion

This type represents the hour period in an abbreviated format where appropriate. For example, when used with `defaultDigits`, this style may represent 8 a.m. as  `8`, or `8 AM`, and 1 p.m. as `13`, or `1 PM`. With `twoDigits`, this style produces `08` or `08 AM`, and `13`, `01 PM`, respectively.

## See Also

- [static let narrow: Date.FormatStyle.Symbol.Hour.AMPMStyle](date/formatstyle/symbol/hour/ampmstyle/narrow.md)
  A type that specifies the narrow day period if the locale prefers using day period with hour.
- [static let omitted: Date.FormatStyle.Symbol.Hour.AMPMStyle](date/formatstyle/symbol/hour/ampmstyle/omitted.md)
  A type that hides the day period marker.
- [static let wide: Date.FormatStyle.Symbol.Hour.AMPMStyle](date/formatstyle/symbol/hour/ampmstyle/wide.md)
  A type that represents the wide day period if the locale prefers using day period with hour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/ampmstyle/abbreviated)*