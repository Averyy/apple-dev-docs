# Loading future timeline events

**Framework**: ClockKit

Preserve battery life and improve performance on the watch by providing a timeline with expected data and updates.

#### Overview

ClockKit renders your complication in advance to ensure that it’s instantly available when the user glances at their watch. To minimize power usage, create a timeline that includes your app’s current data as well as future entries. These timeline entries let ClockKit automatically update your complication without requiring further background tasks.

For example, a meeting complication could display all the meetings that the user currently has scheduled, with a timeline entry for each meeting. If details about the meeting change, your server can use PushKit [`complication`](https://developer.apple.com/documentation/PushKit/PKPushType/complication) notifications to alert the user of these changes, updating the timeline as needed. For more information, see [`Keeping your complications up to date`](keeping-your-complications-up-to-date.md).

##### Batch Load Data

To batch load data for future timeline entries, implement your data source’s [`getTimelineEndDate(for:withHandler:)`](clkcomplicationdatasource/gettimelineenddate(for:withhandler:).md) method and pass the handler the date of the last timeline entry you can create. For example, a meeting app might return the date of the user’s last meeting.

```swift
func getTimelineEndDate(for complication: CLKComplication, withHandler handler: @escaping (Date?) -> Void) {
    handler(myMeetings.last?.date)
}
```

If your app can’t provide future data, pass `nil` to the handler.

> **Note**:  In watchOS 6 and earlier the system sets the end date to [`distantFuture`](https://developer.apple.com/documentation/Foundation/NSDate/distantFuture) if you passed `nil` to [`getTimelineEndDate(for:withHandler:)`](clkcomplicationdatasource/gettimelineenddate(for:withhandler:).md). To indicate that your app can batch load future timeline entries, implement your data source’s [`getSupportedTimeTravelDirections(for:withHandler:)`](clkcomplicationdatasource/getsupportedtimetraveldirections(for:withhandler:).md) method, and pass [`forward`](clkcomplicationtimetraveldirections/forward.md) to the handler.

Next, implement your data source’s [`getTimelineEntries(for:after:limit:withHandler:)`](clkcomplicationdatasource/gettimelineentries(for:after:limit:withhandler:).md) method.

This process is similar to implementing the [`getCurrentTimelineEntry(for:withHandler:)`](clkcomplicationdatasource/getcurrenttimelineentry(for:withhandler:).md) and may reuse much of the same code. However, your implementation must create timeline entries starting at the specified date. The entries must occur in chronological order, and the `limit` parameter determines the maximum number of entries you can pass to the handler. ClockKit calls this method again whenever it needs to extend your timeline.

For details on creating timeline entries, see [`Creating a timeline entry`](creating-a-timeline-entry.md).

##### Schedule Future Events

When constructing your timeline entries, choose dates that make sense based on when the user needs to see the data. ClockKit displays a timeline entry at the time specified by the entry’s [`date`](clkcomplicationtimelineentry/date.md) property. For some types of data, you may want to specify a date before the event actually occurs. For example, if you’re implementing a meeting app, alert users to the meeting before it starts. One option is to set the dates so that the complication displays the next meeting, as soon as the current meeting begins.

![An illustration showing three meetings in the timeline. For the future events, the date is set to the previous meeting’s start time.](https://docs-assets.developer.apple.com/published/e1afb2ae7c1edee98eef4ca32dd1bd8e/media-3161329%402x.png)

## See Also

- [Enabling Complications for Your watchOS App](enabling-complications-for-your-watchos-app.md)
  Set up your watchOS app’s complications.
- [Adding Placeholders for Your Complication](adding-placeholders-for-your-complication.md)
  Provide the placeholders that users see when adding your complication to a watch face.
- [Creating complications for your watchOS app](creating-complications-for-your-watchos-app.md)
  Set up and implement complications for your watchOS app.
- [Declaring complications for your app](declaring-complications-for-your-app.md)
  Define the complications that your app supports.
- [Creating a timeline entry](creating-a-timeline-entry.md)
  Package your app-specific data into a template and create a timeline entry for that template.
- [Keeping your complications up to date](keeping-your-complications-up-to-date.md)
  Replace or extend the data in your complication’s timeline.
- [Building complications with SwiftUI](building-complications-with-swiftui.md)
  Design the appearance of a graphic complication using SwiftUI.
- [Displaying progress views and gauges](displaying-progress-views-and-gauges.md)
  Add rich visual data to your SwiftUI complications with progress views and gauges.
- [Adding text to a complication](adding-text-to-a-complication.md)
  Use text in SwiftUI complications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/loading-future-timeline-events)*