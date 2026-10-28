# AccessoryNotification.Action.ActionType.background

**Framework**: Accessory Notifications  
**Kind**: case  
**Role**: Case

An action type that handles background interactions with a notification.

**Availability**:
- iOS 26.5+

## Declaration

```swift
case background
```

## Discussion

The app that sends the notification might not be running on the accessory, but your companion app can perform a task in the background when a person interacts with the notification.

## See Also

### Determining the type of action
- [AccessoryNotification.Action.ActionType.dismiss](./dismiss.md)
  An action type that dismisses a notification.
- [AccessoryNotification.Action.ActionType.textInput(placeholder:)](./textinput%28placeholder%29.md)
  An action type that captures text provided by a person in response to a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/action/actiontype/background)*