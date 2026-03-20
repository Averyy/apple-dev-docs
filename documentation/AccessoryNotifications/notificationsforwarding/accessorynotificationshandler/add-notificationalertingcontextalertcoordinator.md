# add(notification:alertingContext:alertCoordinator:)

**Framework**: Accessory Notifications  
**Kind**: method  
**Required**: Yes

Provides a new notification for display on your accessory.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
func add(notification: AccessoryNotification, alertingContext: AlertingContext, alertCoordinator: any AlertCoordinating)
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Discussion

Parse the notification details, select the information to display on your accessory, and convert it to data for transmission.

## Parameters

- `notification`: A structured notification containing display details and metadata.
- `alertingContext`: Context for evaluating whether the notification alerts the person or delivers quietly.
- `alertCoordinator`: An object that informs the system when alert coordination completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler/add(notification:alertingcontext:alertcoordinator:))*