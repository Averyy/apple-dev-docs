# AccessoryNotification.DisplayDate

**Framework**: Accessory Notifications  
**Kind**: enum  
**Role**: Enumeration

Options for displaying a date in a notification.

**Availability**:
- iOS 26.5+

## Declaration

```swift
enum DisplayDate
```

## Topics

### Identifying date display options
- [AccessoryNotification.DisplayDate.allDayDate(_:)](./displaydate-swift.enum/alldaydate%28_%29.md)
  An option to display a date for all-day events.
- [AccessoryNotification.DisplayDate.contentDate(_:)](./displaydate-swift.enum/contentdate%28_%29.md)
  An option to display a date that includes a specific moment to which the notification refers.
- [AccessoryNotification.DisplayDate.deliveryDate](./displaydate-swift.enum/deliverydate.md)
  An option to display a date that uses the notification’s delivery timestamp.
- [AccessoryNotification.DisplayDate.hideDate](./displaydate-swift.enum/hidedate.md)
  An option that indicates the accessory doesn’t display a date.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)

## See Also

### Working with notification dates
- [let deliveryDate: Date](./deliverydate.md)
  A timestamp that indicates when the system received the notification.
- [let displayDate: AccessoryNotification.DisplayDate](./displaydate-swift.property.md)
  A preferred date and format to display with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/displaydate-swift.enum)*