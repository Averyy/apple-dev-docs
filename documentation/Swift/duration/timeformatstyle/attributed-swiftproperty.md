# attributed

**Framework**: Swift  
**Kind**: property

A property that formats the duration as an attributed string.

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
var attributed: Duration.TimeFormatStyle.Attributed { get }
```

#### Discussion

Apply the `attributed` property to a configured [`Duration.TimeFormatStyle`](duration/timeformatstyle.md) to produce an [`Duration.TimeFormatStyle.Attributed`](duration/timeformatstyle/attributed-swift.struct.md) style. You can then format a duration with this style to create a formatted [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString). The formatted attributed string contains instances of [`AttributeScopes.FoundationAttributes.DateFieldAttribute`](https://developer.apple.com/documentation/Foundation/AttributeScopes/FoundationAttributes/DateFieldAttribute) for runs with formatted durations.

The following example formats a duration as an attributed string:

```swift
let duration = Duration.seconds(70 * 60 + 32) +
    Duration.milliseconds(400)
let style = Duration.TimeFormatStyle(pattern: .hourMinuteSecond).attributed
let attributedDuration = duration.formatted(style)
```

The resulting `attributedDuration`, representing the string `1:10:32` contains the following runs:

| Run | Attributes |
| --- | --- |
| `1` | `Foundation.DurationFormatAttribute = hours` |
| `:` | None |
| `10` | `Foundation.DurationFormatAttribute = minutes` |
| `:` | None |
| `32` | `Foundation.DurationFormatAttribute = seconds` |

## See Also

- [Duration.TimeFormatStyle.Attributed](duration/timeformatstyle/attributed-swift.struct.md)
  A format style that formats durations as attributed strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/timeformatstyle/attributed-swift.property)*