# AccessoryNotification.DisplayDate.allDayDate(_:)

**Framework**: Accessory Notifications  
**Kind**: case

An option to display a date for all-day events.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
case allDayDate(Date)
```

#### Discussion

Display this date with information about the day (for example, “Sunday” or “July 1st”).

## Parameters

- `date`: The date of the all-day event.

## See Also

- [AccessoryNotification.DisplayDate.contentDate(_:)](accessorynotification/displaydate-swift.enum/contentdate(_:).md)
  An option to display a date that includes a specific moment to which the notification refers.
- [AccessoryNotification.DisplayDate.deliveryDate](accessorynotification/displaydate-swift.enum/deliverydate.md)
  An option to display a date that uses the notification’s delivery timestamp.
- [AccessoryNotification.DisplayDate.hideDate](accessorynotification/displaydate-swift.enum/hidedate.md)
  An option that indicates the accessory doesn’t display a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/displaydate-swift.enum/alldaydate(_:))*