# AccessoryNotification.DisplayDate.contentDate(_:)

**Framework**: Accessory Notifications  
**Kind**: case

An option to display a date that includes a specific moment to which the notification refers.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
case contentDate(Date)
```

#### Discussion

Display this date with information that specifies the minute.

## Parameters

- `date`: The specific date and time to display.

## See Also

- [AccessoryNotification.DisplayDate.allDayDate(_:)](accessorynotification/displaydate-swift.enum/alldaydate(_:).md)
  An option to display a date for all-day events.
- [AccessoryNotification.DisplayDate.deliveryDate](accessorynotification/displaydate-swift.enum/deliverydate.md)
  An option to display a date that uses the notification’s delivery timestamp.
- [AccessoryNotification.DisplayDate.hideDate](accessorynotification/displaydate-swift.enum/hidedate.md)
  An option that indicates the accessory doesn’t display a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/displaydate-swift.enum/contentdate(_:))*