# SystemFormatStyle.DateReference

**Framework**: SwiftUI  
**Kind**: struct

A format style that refers to a date using the most natural phrasing based on how much time separates it from the current time.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct DateReference
```

#### Overview

`DateReference` adapts its output based on how far the referenced date is from the input (which is typically the current time). Close dates use a relative representation, while distant dates switch to an absolute one.

```swift
// Displays "in 5 minutes", "tomorrow", "June 2019", etc.
Text(.currentDate, format: .reference(to: eventDate))
```

##### Relative Vs Absolute Representation

The style uses a relative format (“in 2 hours”, “3 days ago”) when the referenced date is within the threshold distance. Beyond that threshold, it switches to an absolute format (“Monday, June 3”, “June 2019”).

The `thresholdField` parameter controls where this switch happens. With the default value of `.day`, the style uses the relative format as long as the date falls within approximately one month of the reference date:

| Distance | Style | Output |
| --- | --- | --- |
| < 1 min | Relative | `now` |
| 5 min | Relative | `in 5 minutes` |
| 3 hours | Relative | `in 3 hours` |
| 1 day | Relative | `tomorrow` |
| 3 days | Relative | `3 days ago` |
| 27 days | Relative | `27 days ago` |
| > 1 month | Absolute | `Monday, June 3` |
| > 1 year | Absolute | `June 2019` |

##### Controlling the Absolute Representation

The `maxFieldCount` parameter determines how many date components appear in the absolute representation:

```swift
// maxFieldCount: 2 (default)
// Output for a date in a different year: "June 2019"

// maxFieldCount: 3
.reference(to: date, maxFieldCount: 3)
// Output: "June 3, 2019"
```

The style automatically removes higher-order fields that match the reference date. For a date within the same year, the year field is dropped, leaving room for day-level detail:

```swift
// Same year as reference date, maxFieldCount: 2
// Output: "Monday, June 3" (instead of "June 2019")
```

## Topics

### Initializers
- [init(to: Date, allowedFields: Set<Date.RelativeFormatStyle.Field>, maxFieldCount: Int, thresholdField: Date.RelativeFormatStyle.Field)](systemformatstyle/datereference/init(to:allowedfields:maxfieldcount:thresholdfield:).md)
  Creates a format style that refers to a comparison date using natural language.
### Instance Methods
- [func calendar(Calendar) -> SystemFormatStyle.DateReference](systemformatstyle/datereference/calendar(_:).md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [DiscreteFormatStyle](../Foundation/DiscreteFormatStyle.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [FormatStyle](../Foundation/FormatStyle.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/systemformatstyle/datereference)*