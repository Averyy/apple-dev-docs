# eventEditViewControllerDefaultCalendar(forNewEvents:)

**Framework**: EventKit UI  
**Kind**: method  
**Role**: Instance Method

The default calendar to use when creating new events.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func eventEditViewControllerDefaultCalendar(forNewEvents controller: EKEventEditViewController) -> EKCalendar
```

```objc
- (EKCalendar *) eventEditViewControllerDefaultCalendarForNewEvents:(EKEventEditViewController *) controller;
```

## Discussion

If the delegate does not implement this method, uses the event store’s [`defaultCalendarForNewEvents`](../../EventKit/ekeventstore/defaultcalendarfornewevents.md) property instead.

## Parameters

- `controller`: The event edit view controller requesting the default calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventeditviewdelegate/eventeditviewcontrollerdefaultcalendar(fornewevents:))*