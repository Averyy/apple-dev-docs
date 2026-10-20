# region

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The geographic region that triggers the notification.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 3.0

## Declaration

```swift
@NSCopying
var region: CLRegion? { get set }
```

```objc
@property (nonatomic, copy, nullable) CLRegion * region;
```

#### Discussion

Assigning a value to this property causes the local notification to be delivered when the user crosses the region’s boundary. The region object itself defines whether the notification is triggered when the user enters or exits the region. The default value of this property is `nil`.

You may specify a value for this property or the [`fireDate`](./firedate.md) property but not both. Attempting to schedule a local notification that contains both a region and fire date raises an exception.

Apps are limited in the total number of regions they may monitor at any given time, and local notifications configured with a region value count against that total. In addition, the user must grant permission for your app to use location-related information for the delivery of region-based local notifications to work. If the user denies your app’s request to use location services, local notifications configured with a region will not be delivered.

## See Also

### Scheduling a local notification
- [var fireDate: Date?](./firedate.md)
  The date and time when the system should deliver the notification.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone of the notification’s fire date.
- [var repeatInterval: NSCalendar.Unit](./repeatinterval.md)
  The calendar interval at which to reschedule the notification.
- [var repeatCalendar: Calendar?](./repeatcalendar.md)
  The calendar the system should refer to when it reschedules a repeating notification.
- [var regionTriggersOnce: Bool](./regiontriggersonce.md)
  A Boolean value indicating whether crossing a geographic region boundary delivers only one notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/region)*