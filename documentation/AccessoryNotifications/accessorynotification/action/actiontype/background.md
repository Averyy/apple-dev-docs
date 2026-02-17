# AccessoryNotification.Action.ActionType.background

**Framework**: Accessory Notifications  
**Kind**: case

An action type that handles background interactions with a notification.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
case background
```

#### Discussion

The app that sends the notification might not be running on the accessory, but your companion app can perform a task in the background when a person interacts with the notification.

## See Also

- [AccessoryNotification.Action.ActionType.dismiss](accessorynotification/action/actiontype/dismiss.md)
  An action type that dismisses a notification.
- [AccessoryNotification.Action.ActionType.textInput(placeholder:)](accessorynotification/action/actiontype/textinput(placeholder:).md)
  An action type that captures text provided by a person in response to a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/action/actiontype/background)*