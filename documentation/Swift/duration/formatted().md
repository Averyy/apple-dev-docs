# formatted()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Formats the string using a localized hour-minute-second time pattern.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func formatted() -> String
```

#### Return Value

A localized formatted string that describes the duration, such as `1:30:56` for a duration of 1 hour, 30 minutes, and 56 seconds in the U.S. English locale. In the Finnish locale, this returns `1.30.56`.

#### Discussion

The following example shows the effect of applying the default formatting to a duration of two seconds:

```swift
let duration = Duration.seconds(2)
let formattedDuration = duration.formatted() // "0:00:02"
```

This method uses a default [`Duration.TimeFormatStyle`](./timeformatstyle.md). To modify the formatting, customize a [`Duration.TimeFormatStyle`](./timeformatstyle.md) or [`Duration.UnitsFormatStyle`](./unitsformatstyle.md), then call [`formatted(_:)`](./formatted%28_%29.md) on the duration, passing in the style. You can also call `format(_:)` on the style, passing in a duration.

## See Also

### Formatting a duration
- [func formatted<S>(S) -> S.FormatOutput](./formatted%28_%29.md)
  Formats the duration, using the provided format style.
- [Duration.TimeFormatStyle](./timeformatstyle.md)
  A format style that shows durations in a compact, localized format with separators.
- [Duration.UnitsFormatStyle](./unitsformatstyle.md)
  A format style that shows durations with localized labeled components


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/formatted())*