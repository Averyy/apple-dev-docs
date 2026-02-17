# AccessoryError.invalidNotificationResponse

**Framework**: Accessory Notifications  
**Kind**: case

An error that indicates the system failed to handle a notification response.

**Availability**:
- iOS ?+
- iPadOS ?+

## Declaration

```swift
case invalidNotificationResponse
```

#### Discussion

The [`AccessoryNotificationManaging`](accessorynotificationmanaging.md) protocol’s [`sendResponse(_:for:)`](accessorynotificationmanaging/sendresponse(_:for:).md) method can throw an error of this type.

## See Also

- [AccessoryError.unableToGetUserResponse](accessoryerror/unabletogetuserresponse.md)
  An error that indicates the system is unable to handle a notification response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessoryerror/invalidnotificationresponse)*