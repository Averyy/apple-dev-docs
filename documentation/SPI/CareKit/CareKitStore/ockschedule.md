---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockschedule"
framework: "CareKit/CareKitStore"
---

# OCKSchedule

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

An implementation of `OCKSchedulable` that can be created by composing together any number of other `OCKSchedulable` objects, including other instance of `OCKSchedule`. This allows for the creation of arbitrarily complex schedules.

## Declaration

```swift
struct OCKSchedule
```

## Overview

> **Note**: A variety of initializers are provided to quickly create commonly used schedules. Used in combination with the offset method, building up complex schedules can be performed quite efficiently.

## Topics

### Initializers
- [init(composing: [OCKScheduleElement])](./ockschedule/init%28composing%29-35hze.md)
  Create a new schedule by combining an array of other `OCKSchedule` objects.
- [init(composing: [OCKSchedule])](./ockschedule/init%28composing%29-6h2mg.md)
  Create a new schedule by combining an array of other `OCKSchedule` objects.
- [init(from: any Decoder) throws](./ockschedule/init%28from%29.md)
### Instance Properties
- [let elements: [OCKScheduleElement]](./ockschedule/elements.md)
  The constituent components this schedule was built from.
### Instance Methods
- [func endDate() -> Date?](./ockschedule/enddate%28%29.md)
  The date of the last event of this schedule, or nil if the schedule is of infinite length.
- [func event(forOccurrenceIndex: Int) -> OCKScheduleEvent?](./ockschedule/event%28foroccurrenceindex%29.md)
  Compute the date of the Nth event. The result will be nil if the Nth event starts after the end of the schedule.
- [func events(from: Date, to: Date) -> [OCKScheduleEvent]](./ockschedule/events%28from,to%29.md)
  Compute a list of events that occur between two dates. The lower bound is inclusive and the upper bound is exclusive.
- [func offset(by: DateComponents) -> OCKSchedule](./ockschedule/offset%28by%29.md)
  Create a new schedule by shifting this schedule.
- [func startDate() -> Date](./ockschedule/startdate%28%29.md)
  The date of the first event of this schedule.
### Subscripts
- [subscript(Int) -> OCKScheduleEvent](./ockschedule/subscript%28_%29.md)
  Returns the Nth event of this schedule.
### Type Methods
- [static func dailyAtTime(hour: Int, minutes: Int, start: Date, end: Date?, text: String?, duration: OCKScheduleElement.Duration, targetValues: [OCKOutcomeValue]) -> OCKSchedule](./ockschedule/dailyattime%28hour,minutes,start,end,text,duration,targetvalues%29.md)
  Create a schedule that happens once per day, every day, at a fixed time.
- [static func weeklyAtTime(weekday: Int, hours: Int, minutes: Int, start: Date, end: Date?, targetValues: [OCKOutcomeValue], text: String?, duration: OCKScheduleElement.Duration) -> OCKSchedule](./ockschedule/weeklyattime%28weekday,hours,minutes,start,end,targetvalues,text,duration%29.md)
  Create a schedule that happens once per week, every week, at a fixed time.
### Default Implementations
- [Equatable Implementations](./ockschedule/equatable-implementations.md)

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
- [struct OCKScheduleElement](./ockscheduleelement.md)
  The simplest possible `OCKSchedulable`, representing a single event that repeats at fixed intervals. It may have fixed duration or repeat indefinitely.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockschedule)*