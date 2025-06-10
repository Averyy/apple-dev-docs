# wide

**Framework**: Foundation  
**Kind**: property

A type that represents the wide day period if the locale prefers using day period with hour.

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
static let wide: Date.FormatStyle.Symbol.Hour.AMPMStyle
```

#### Discussion

This type represents the hour period in a wide format where appropriate. For example, when used with `defaultDigits`, this style may represent 8 a.m. as  `8` or `8 A.M.,` and 1 p.m. as  `13` or `1 P.M.` With `twoDigits`, this style produce `08` or `08 A.M.` and `13 or 01 P.M.`

## See Also

- [static let abbreviated: Date.FormatStyle.Symbol.Hour.AMPMStyle](date/formatstyle/symbol/hour/ampmstyle/abbreviated.md)
  A type that specifies the abbreviated day period for when the locale prefers using day period with hour.
- [static let narrow: Date.FormatStyle.Symbol.Hour.AMPMStyle](date/formatstyle/symbol/hour/ampmstyle/narrow.md)
  A type that specifies the narrow day period if the locale prefers using day period with hour.
- [static let omitted: Date.FormatStyle.Symbol.Hour.AMPMStyle](date/formatstyle/symbol/hour/ampmstyle/omitted.md)
  A type that hides the day period marker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/ampmstyle/wide)*