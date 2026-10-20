# TN3132: Changes to EventKit and EventKitUI in iOS 16

**Framework**: Technotes  
**Role**: Technote

Test your apps against EventKit and EventKitUI API changes in iOS 16.

#### Overview

The iOS 16 SDK introduces some changes to the EventKit and EventKitUI frameworks. This document highlights some of the major changes. To learn about related changes in macOS Ventura 13, see [TN3130: Changes to EventKit in macOS Ventura 13](./tn3130-changes-to-eventkit-in-macos13-ventura.md).

For apps running on systems prior to iOS 16, built with Xcode 13 or earlier and linked against older versions of the iOS SDK, the legacy behavior remains in place when using these frameworks. When you run your app on iOS 16, and have built it with Xcode 14 and linked against the iOS 16 SDK, you may see behavior that you are unfamiliar with when using EventKit or EventKitUI. To identify these changes in behavior, thoroughly test your app on each major OS version it supports on real hardware. Confirm that your implementation of EventKit or EventKitUI behaves as you expect in each OS version and update your code where needed.
If you notice an unexpected behavior in EventKit, report it using [Feedback Assistant](https://developer.apple.com/bug-reporting/).

#### EKCalendarChooser

Setting the [`selectedCalendars`](../EventKitUI/ekcalendarchooser/selectedcalendars.md) property of a calendar chooser view controller no longer calls the [`calendarChooserSelectionDidChange(_:)`](../EventKitUI/ekcalendarchooserdelegate/calendarchooserselectiondidchange%28_%29.md) delegate method. `calendarChooserSelectionDidChange(_:)` is only called when the user selects a calendar in the view controller.

#### EKEventStore

##### Committing changes

When you call [`saveCalendar(_:commit:)`](../EventKit/ekeventstore/savecalendar%28_,commit%29.md), [`removeCalendar(_:commit:)`](../EventKit/ekeventstore/removecalendar%28_,commit%29.md), [`save(_:span:commit:)`](../EventKit/ekeventstore/save%28_,span,commit%29.md), [`remove(_:span:commit:)`](../EventKit/ekeventstore/remove%28_,span,commit%29.md), [`save(_:commit:)`](../EventKit/ekeventstore/save%28_,commit%29.md), or [`remove(_:commit:)`](../EventKit/ekeventstore/remove%28_,commit%29.md) methods with the `commit` parameter set to `true`, [`EKEventStore`](../EventKit/ekeventstore.md) attempts to immediately save and commit your changes to the event store. If the commit fails, `EKEventStore` automatically rolls back all changes that have been saved but aren’t yet committed to the event store.

In the legacy behavior, objects remain saved but uncommitted in the event store when the commit failed.

##### Fetching events

[`events(matching:)`](../EventKit/ekeventstore/events%28matching%29.md) and [`enumerateEvents(matching:using:)`](../EventKit/ekeventstore/enumerateevents%28matching,using%29.md) now return events that have been saved but weren’t yet committed to the event store.

In the legacy behavior, `events(matching:)` and `enumerateEvents(matching:using:)` only return events that have been saved and committed to the event store.

##### Recurring events

If you are saving a detached occurrence of a recurring event, and you specify [`EKSpan.futureEvents`](../EventKit/ekspan/futureevents.md) for the `span` parameter of the [`save(_:span:commit:)`](../EventKit/ekeventstore/save%28_,span,commit%29.md) method, your changes apply to all future occurrences of the event.

In the legacy behavior, your changes only apply to this instance of the recurring event.

#### Revision History

- **2022-08-16** First published.

## See Also

### Related Documentation
- [TN3130: Changes to EventKit in macOS Ventura 13](./tn3130-changes-to-eventkit-in-macos13-ventura.md)
  Test your apps against EventKit API changes in macOS Ventura 13.
- [TN3153: Adopting API changes for EventKit in iOS 17, macOS 14, and watchOS 10](./tn3153-adopting-api-changes-for-eventkit-in-ios-macos-and-watchos.md)
  Test your existing apps against EventKit API latest changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3132-changes-eventkit-and-eventkitui-in-ios16)*