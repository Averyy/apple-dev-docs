---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleelement"
framework: "CareKit/CareKitStore"
---

# OCKScheduleElement

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

The simplest possible `OCKSchedulable`, representing a single event that repeats at fixed intervals. It may have fixed duration or repeat indefinitely.

## Declaration

```swift
struct OCKScheduleElement
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./ockscheduleelement/init%28from%29.md)
- [init(start: Date, end: Date?, interval: DateComponents, text: String?, targetValues: [OCKOutcomeValue], duration: Duration, calendar: Calendar)](./ockscheduleelement/init%28start,end,interval,text,targetvalues,duration,calendar%29.md)
  Create a `ScheduleElement` by specifying the start date, end date, and interval.
### Instance Properties
- [var calendar: Calendar](./ockscheduleelement/calendar.md)
  The calendar used when computing dates for the schedule.
- [var duration: Duration](./ockscheduleelement/duration-swift.property.md)
  The amount of time that the event should take, in seconds.
- [var elements: [OCKScheduleElement]](./ockscheduleelement/elements.md)
- [var end: Date?](./ockscheduleelement/end.md)
  The latest possible time for an event to occur.
- [var interval: DateComponents](./ockscheduleelement/interval.md)
  The amount of time between events specified using `DateCoponents`.
- [let start: Date](./ockscheduleelement/start.md)
  The date and time the first event occurs.
- [var targetValues: [OCKOutcomeValue]](./ockscheduleelement/targetvalues.md)
  An array of values that specify what values the user is expected to record. For example, for a medication, it may be the dose that the patient is expected to take.
- [var text: String?](./ockscheduleelement/text.md)
  An text about the time this element represents. e.g. before breakfast on Tuesdays, 5PM every day, etc.
### Instance Methods
- [func date(ofOccurrence: Int) -> Date?](./ockscheduleelement/date%28ofoccurrence%29.md)
  Computes the date of the Nth event. The result will be nil if the Nth event starts after the end of the schedule.
- [func events(betweenOccurrenceIndex: Int, and: Int) -> [OCKScheduleEvent]](./ockscheduleelement/events%28betweenoccurrenceindex,and%29.md)
  Compute all events that occur between `startIndex` (inclusive) and `stopIndex` (exclusive). The result might not contain the desired events if the schedule ends before a particular event starts.
- [func events(from: Date, to: Date) -> [OCKScheduleEvent]](./ockscheduleelement/events%28from,to%29.md)
  Compute all events that occur between `start` (inclusive) and `end` (exclusive).
- [func offset(by: DateComponents) -> OCKScheduleElement](./ockscheduleelement/offset%28by%29.md)
### Subscripts
- [subscript(Int) -> OCKScheduleEvent](./ockscheduleelement/subscript%28_%29.md)
  Compute the Nth event of this schedule.
### Enumerations
- [OCKScheduleElement.Duration](./ockscheduleelement/duration-swift.enum.md)
  A duration describing the length of an event. Options include all day, or a deterministic number of hours, minutes, or seconds.
### Default Implementations
- [Equatable Implementations](./ockscheduleelement/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Care task scheduling
- [struct OCKSchedule](./ockschedule.md)
  An implementation of `OCKSchedulable` that can be created by composing together any number of other `OCKSchedulable` objects, including other instance of `OCKSchedule`. This allows for the creation of arbitrarily complex schedules.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleelement)*