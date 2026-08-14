# SystemFormatStyle.Timer

**Framework**: SwiftUI  
**Kind**: struct

A format style that displays a countdown or count-up timer within a bounded time interval.

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
struct Timer
```

#### Overview

`Timer` produces a time-pattern output (like `4:32` or `1:23:45`) that progresses between zero and the interval’s total duration. Unlike [`SystemFormatStyle.Stopwatch`](systemformatstyle/stopwatch.md), a timer operates within a defined start and end date and can count in either direction.

```swift
let start = Date.now
let end = start.addingTimeInterval(600)

// Countdown from 10:00 to 0:00
Text(.currentDate, format: .timer(countingDownIn: start..<end))

// Count up from 0:00 to 10:00
Text(.currentDate, format: .timer(countingUpIn: start..<end))
```

##### Countdown Behavior

A countdown timer starts at the total interval duration and decreases to zero:

```swift
// 5-minute countdown
let start = Date.now
let end = start.addingTimeInterval(300)
Text(.currentDate, format: .timer(countingDownIn: start..<end))
```

| Elapsed since start | Output |
| --- | --- |
| 0 seconds | `5:00` |
| 1 minute | `4:00` |
| 4 min, 30 sec | `0:30` |
| 5 minutes | `0:00` |

##### Count Up Behavior

A count-up timer starts at zero and increases toward the total interval duration:

```swift
// 1-hour count-up
let start = Date.now
let end = start.addingTimeInterval(3600)
Text(.currentDate, format: .timer(countingUpIn: start..<end))
```

| Elapsed since start | Output |
| --- | --- |
| 0 seconds | `0:00` |
| 30 seconds | `0:30` |
| 59 min, 59 sec | `59:59` |
| 1 hour | `1:00:00` |

##### Hours Display

When `showsHours` is `true` (the default), the hours field appears once the displayed value reaches one hour. The transition between formats happens cleanly:

```swift
// Countdown transition at the 1-hour boundary:
// "1:00:00" -> "59:59" -> "59:58" -> ...
```

When `showsHours` is `false`, minutes accumulate beyond 60:

```swift
.timer(countingDownIn: start..<end, showsHours: false)
// Output for 90 minutes remaining: "90:00"
```

##### Precision Control

The `maxPrecision` parameter determines the smallest displayed unit:

```swift
// Default (1 second): "4:32"
.timer(countingDownIn: start..<end)

// Minute precision: shows "5 minutes", "4 minutes", etc.
.timer(countingDownIn: start..<end, maxPrecision: .seconds(60))
```

## Topics

### Initializers
- [init(countingDownIn: Range<Date>, showsHours: Bool, maxFieldCount: Int, maxPrecision: Duration)](systemformatstyle/timer/init(countingdownin:showshours:maxfieldcount:maxprecision:).md)
  Creates a timer format style that counts down within the interval you provide.
- [init(countingUpIn: Range<Date>, showsHours: Bool, maxFieldCount: Int, maxPrecision: Duration)](systemformatstyle/timer/init(countingupin:showshours:maxfieldcount:maxprecision:).md)
  Creates a timer format style that counts up within the interval you provide.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [DiscreteFormatStyle](../foundation/discreteformatstyle.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [FormatStyle](../foundation/formatstyle.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/systemformatstyle/timer)*