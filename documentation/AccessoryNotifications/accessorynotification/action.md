# AccessoryNotification.Action

**Framework**: Accessory Notifications  
**Kind**: struct  
**Role**: Structure

A possible user interaction with a notification.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct Action
```

## Topics

### Creating an action
- [init(identifier: String, title: String?, type: AccessoryNotification.Action.ActionType)](./action/init%28identifier,title,type%29.md)
  Initializes a notification action with the given identifier, title, and type.
### Identifying an action
- [let identifier: String](./action/identifier.md)
  A unique identifier for the action.
- [let title: String?](./action/title.md)
  A title for the action.
### Determining the action type
- [let type: AccessoryNotification.Action.ActionType](./action/type.md)
  A type for the action.
- [AccessoryNotification.Action.ActionType](./action/actiontype.md)
  The types of actions available for a notification.
### Initializers
- [init(identifier: String, title: String?, type: AccessoryNotification.Action.ActionType, isDestructive: Bool)](./action/init%28identifier,title,type,isdestructive%29.md)
### Instance Properties
- [var isDestructive: Bool](./action/isdestructive.md)
  Whether this action performs a destructive task.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)

## See Also

### Handling user interactions
- [let actions: [AccessoryNotification.Action]](./actions.md)
  An array of possible interactions that a person can have with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/action)*