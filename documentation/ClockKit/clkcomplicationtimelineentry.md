# CLKComplicationTimelineEntry

**Framework**: ClockKit  
**Kind**: class

A container for the complication template object to display and the time to display it.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTimelineEntry
```

## Mentions

- [Creating a timeline entry](creating-a-timeline-entry.md)

#### Overview

Each entry object represents a single data point along your complication’s timeline. You create and return timeline entries when asked to do so by ClockKit. When the date associated with a particular timeline entry occurs, ClockKit updates your complication’s interface with the data in the accompanying template object.

You can assign a group identifier to timeline entries to control the behavior of transition animations during Time Travel. When two timeline entries have different values in their [`timelineAnimationGroup`](clkcomplicationtimelineentry/timelineanimationgroup.md) property, or when the values are `nil`, ClockKit animates the transition between those entries during Time Travel. When two entries have the same group value, no animation is created.

## Topics

### Creating a Timeline Entry
- [convenience init(date: Date, complicationTemplate: CLKComplicationTemplate)](clkcomplicationtimelineentry/init(date:complicationtemplate:).md)
  Creates and returns a timeline entry with the specified date and complication data.
- [convenience init(date: Date, complicationTemplate: CLKComplicationTemplate, timelineAnimationGroup: String?)](clkcomplicationtimelineentry/init(date:complicationtemplate:timelineanimationgroup:).md)
  Creates and returns a timeline entry with the specified information.
### Setting the Entry Values
- [var date: Date](clkcomplicationtimelineentry/date.md)
  The time at which to display the entry.
- [var complicationTemplate: CLKComplicationTemplate](clkcomplicationtimelineentry/complicationtemplate.md)
  The template containing the data to display in your complication.
- [var timelineAnimationGroup: String?](clkcomplicationtimelineentry/timelineanimationgroup.md)
  The animation group to which the entry belongs.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKComplicationServer](clkcomplicationserver.md)
  An object that manages the active complications for an app.
- [class CLKComplication](clkcomplication.md)
  Metadata about a custom complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry)*