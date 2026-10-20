# attributed

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

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
var attributed: Duration.UnitsFormatStyle.Attributed { get }
```

#### Discussion

Apply the `attributed` property to a configured [`Duration.UnitsFormatStyle`](../unitsformatstyle.md) to produce an [`Duration.UnitsFormatStyle.Attributed`](./attributed-swift.struct.md) style. You can then format a duration with this style to create a formatted   [`AttributedString`](../../../Foundation/attributedstring.md). The formatted attributed string contains instances of [`AttributeScopes.FoundationAttributes.DateFieldAttribute`](../../../Foundation/attributescopes/foundationattributes/datefieldattribute.md) and [`AttributeScopes.FoundationAttributes.MeasurementAttribute`](../../../Foundation/attributescopes/foundationattributes/measurementattribute.md) for runs with formatted durations.

The following example formats a duration as an attributed string:

```swift
let duration = Duration.seconds(70 * 60 + 32) +
    Duration.milliseconds(400)
let style = Duration.UnitsFormatStyle(allowedUnits: [.hours, .minutes, .seconds],
                                      width: .abbreviated).attributed
let attributedDuration = duration.formatted(style)
```

The resulting `attributedDuration`, representing the string `1 hr, 10 min, 32 sec` contains the following runs:

| Run | Attributes |
| --- | --- |
| `1` | `Foundation.MeasurementAttribute = value`, `Foundation.DurationFormatAttribute = hours` |
| (space) | `Foundation.DurationFormatAttribute = hours` |
| `hr` | `Foundation.DurationFormatAttribute = hours`, `Foundation.MeasurementAttribute = unit` |
| `,  ` | None |
| `10` | `Foundation.MeasurementAttribute = value`, `Foundation.DurationFormatAttribute = minutes` |
| (space) | `Foundation.DurationFormatAttribute = minutes` |
| `min` | `Foundation.DurationFormatAttribute = minutes`, `Foundation.MeasurementAttribute = unit` |
| `,  ` | None |
| `32` | `Foundation.MeasurementAttribute = value`, `Foundation.DurationFormatAttribute = seconds` |
| (space) | `Foundation.DurationFormatAttribute = seconds` |
| `sec` | `Foundation.DurationFormatAttribute = seconds`, `Foundation.MeasurementAttribute = unit` |

## See Also

### Formatting a duration as an attributed string
- [Duration.UnitsFormatStyle.Attributed](./attributed-swift.struct.md)
  A format style that formats durations as attributed strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/unitsformatstyle/attributed-swift.property)*