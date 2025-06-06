# region

**Framework**: UIKit  
**Kind**: property

The geographic region that triggers the notification.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
@MainActor var region: CLRegion? { get set }
```

#### Discussion

Assigning a value to this property causes the local notification to be delivered when the user crosses the region’s boundary. The region object itself defines whether the notification is triggered when the user enters or exits the region. The default value of this property is `nil`.

You may specify a value for this property or the [`fireDate`](uilocalnotification/firedate.md) property but not both. Attempting to schedule a local notification that contains both a region and fire date raises an exception.

Apps are limited in the total number of regions they may monitor at any given time, and local notifications configured with a region value count against that total. In addition, the user must grant permission for your app to use location-related information for the delivery of region-based local notifications to work. If the user denies your app’s request to use location services, local notifications configured with a region will not be delivered.

## See Also

- [var fireDate: Date?](uilocalnotification/firedate.md)
  The date and time when the system should deliver the notification.
- [var timeZone: TimeZone?](uilocalnotification/timezone.md)
  The time zone of the notification’s fire date.
- [var repeatInterval: NSCalendar.Unit](uilocalnotification/repeatinterval.md)
  The calendar interval at which to reschedule the notification.
- [var repeatCalendar: Calendar?](uilocalnotification/repeatcalendar.md)
  The calendar the system should refer to when it reschedules a repeating notification.
- [var regionTriggersOnce: Bool](uilocalnotification/regiontriggersonce.md)
  A Boolean value indicating whether crossing a geographic region boundary delivers only one notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/region)*