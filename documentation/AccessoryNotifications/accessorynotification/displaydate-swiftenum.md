# AccessoryNotification.DisplayDate

**Framework**: Accessory Notifications  
**Kind**: enum

Options for displaying a date in a notification.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
enum DisplayDate
```

## Topics

### Identifying date display options
- [AccessoryNotification.DisplayDate.allDayDate(_:)](accessorynotification/displaydate-swift.enum/alldaydate(_:).md)
  An option to display a date for all-day events.
- [AccessoryNotification.DisplayDate.contentDate(_:)](accessorynotification/displaydate-swift.enum/contentdate(_:).md)
  An option to display a date that includes a specific moment to which the notification refers.
- [AccessoryNotification.DisplayDate.deliveryDate](accessorynotification/displaydate-swift.enum/deliverydate.md)
  An option to display a date that uses the notification’s delivery timestamp.
- [AccessoryNotification.DisplayDate.hideDate](accessorynotification/displaydate-swift.enum/hidedate.md)
  An option that indicates the accessory doesn’t display a date.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [let deliveryDate: Date](accessorynotification/deliverydate.md)
  A timestamp that indicates when the system received the notification.
- [let displayDate: AccessoryNotification.DisplayDate](accessorynotification/displaydate-swift.property.md)
  A preferred date and format to display with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/displaydate-swift.enum)*