# omitted

**Framework**: Foundation  
**Kind**: property

A type that hides the day period marker.

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
static let omitted: Date.FormatStyle.Symbol.Hour.AMPMStyle
```

#### Discussion

This type represents the hour period numerically only. For example, `8` (for 8 a.m.) or `1` (for 1 p.m.) if used with `defaultDigits`, and `08` or `01` if used with `twoDigits`.

## See Also

- [static let abbreviated: Date.FormatStyle.Symbol.Hour.AMPMStyle](date/formatstyle/symbol/hour/ampmstyle/abbreviated.md)
  A type that specifies the abbreviated day period for when the locale prefers using day period with hour.
- [static let narrow: Date.FormatStyle.Symbol.Hour.AMPMStyle](date/formatstyle/symbol/hour/ampmstyle/narrow.md)
  A type that specifies the narrow day period if the locale prefers using day period with hour.
- [static let wide: Date.FormatStyle.Symbol.Hour.AMPMStyle](date/formatstyle/symbol/hour/ampmstyle/wide.md)
  A type that represents the wide day period if the locale prefers using day period with hour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/ampmstyle/omitted)*