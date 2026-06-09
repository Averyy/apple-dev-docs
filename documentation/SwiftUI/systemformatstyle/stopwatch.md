# SystemFormatStyle.Stopwatch

**Framework**: SwiftUI  
**Kind**: struct

A format style that displays elapsed time as a precision stopwatch counting up from zero.

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
struct Stopwatch
```

#### Overview

`Stopwatch` produces output in a time-pattern format that includes hundredths of a second by default, making it suitable for use cases such as athletic timing where sub-second precision matters.

```swift
let startDate = Date.now
Text(.currentDate, format: .stopwatch(startingAt: startDate))
// Output: "00:05.23" (after 5.23 seconds)
```

##### Output Format Progression

The stopwatch automatically adds an hours field when the elapsed time reaches one hour:

| Elapsed | Output |
| --- | --- |
| Under 1 min | `00:05.23` |
| Under 1 hour | `45:30.12` |
| 1 hour or more | `01:00:00.00` |
| Over 25 hours | `25:01:01.00` |

##### Adjusting Precision

Control the displayed precision with the `maxPrecision` parameter:

```swift
// Whole-second precision (no fractional digits)
.stopwatch(startingAt: start, maxPrecision: .seconds(1))
// Output: "01:23"

// Tenth-of-a-second precision (one fractional digit)
.stopwatch(startingAt: start, maxPrecision: .milliseconds(100))
// Output: "01:23.4"

// Minute-only precision
.stopwatch(startingAt: start, maxPrecision: .seconds(60))
// Output: "1 hour" or "23 minutes"
```

##### Controlling Field Count

The `maxFieldCount` parameter limits how many fields appear:

```swift
// At 1 hour, 23 minutes, 45.67 seconds elapsed:
// maxFieldCount: 4 (default): "01:23:45.67"
// maxFieldCount: 3: "01:23:45"
// maxFieldCount: 2: "1:23" (hours and minutes only)
```

## Topics

### Initializers
- [init(startingAt: Date, showsHours: Bool, maxFieldCount: Int, maxPrecision: Duration)](systemformatstyle/stopwatch/init(startingat:showshours:maxfieldcount:maxprecision:).md)
  Creates a stopwatch format style that starts counting up from zero from the date you provide.

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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/systemformatstyle/stopwatch)*