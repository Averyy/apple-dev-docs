# AccessoryNotification.Action

**Framework**: Accessory Notifications  
**Kind**: struct

A possible user interaction with a notification.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct Action
```

## Topics

### Creating an action
- [init(identifier: String, title: String?, type: AccessoryNotification.Action.ActionType)](accessorynotification/action/init(identifier:title:type:).md)
  Initializes a notification action with the given identifier, title, and type.
### Identifying an action
- [let identifier: String](accessorynotification/action/identifier.md)
  A unique identifier for the action.
- [let title: String?](accessorynotification/action/title.md)
  A title for the action.
### Determining the action type
- [let type: AccessoryNotification.Action.ActionType](accessorynotification/action/type.md)
  A type for the action.
- [AccessoryNotification.Action.ActionType](accessorynotification/action/actiontype.md)
  The types of actions available for a notification.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)

## See Also

- [let actions: [AccessoryNotification.Action]](accessorynotification/actions.md)
  An array of possible interactions that a person can have with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/action)*