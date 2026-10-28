# AccessoryNotification.DisplayDate.contentDate(_:)

**Framework**: Accessory Notifications  
**Kind**: case  
**Role**: Case

An option to display a date that includes a specific moment to which the notification refers.

**Availability**:
- iOS 26.5+

## Declaration

```swift
case contentDate(Date)
```

## Discussion

Display this date with information that specifies the minute.

## Parameters

- `date`: The specific date and time to display.

## See Also

### Identifying date display options
- [AccessoryNotification.DisplayDate.allDayDate(_:)](./alldaydate%28_%29.md)
  An option to display a date for all-day events.
- [AccessoryNotification.DisplayDate.deliveryDate](./deliverydate.md)
  An option to display a date that uses the notification’s delivery timestamp.
- [AccessoryNotification.DisplayDate.hideDate](./hidedate.md)
  An option that indicates the accessory doesn’t display a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/displaydate-swift.enum/contentdate(_:))*