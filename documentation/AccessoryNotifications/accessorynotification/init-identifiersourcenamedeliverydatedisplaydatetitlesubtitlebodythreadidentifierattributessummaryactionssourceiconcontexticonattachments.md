# init(identifier:sourceName:deliveryDate:displayDate:title:subtitle:body:threadIdentifier:attributes:summary:actions:sourceIcon:contextIcon:attachments:)

**Framework**: Accessory Notifications  
**Kind**: init

Initializes an accessory notification.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
init(identifier: AccessoryNotification.Identifier, sourceName: String, deliveryDate: Date, displayDate: AccessoryNotification.DisplayDate = .deliveryDate, title: String? = nil, subtitle: String? = nil, body: NSAttributedString? = nil, threadIdentifier: String? = nil, attributes: AccessoryNotification.Attributes = [], summary: NSAttributedString? = nil, actions: [AccessoryNotification.Action] = [], sourceIcon: AccessoryNotification.File? = nil, contextIcon: AccessoryNotification.File? = nil, attachments: [AccessoryNotification.File] = [])
```

## Parameters

- `identifier`: A unique identifier for the notification.
- `sourceName`: The name of the bundle that sent the notification.
- `deliveryDate`: The timestamp when the system received the notification.
- `displayDate`: The preferred date and format to display.
- `title`: The notification’s primary text.
- `subtitle`: The notification’s secondary text.
- `body`: The notification’s main content.
- `threadIdentifier`: An identifier for grouping related notifications.
- `attributes`: The priority attributes for the notification.
- `summary`: An Apple Intelligence summary.
- `actions`: Possible user interactions.
- `sourceIcon`: The source app’s icon.
- `contextIcon`: A contextual icon for additional information.
- `attachments`: Files sent with the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/init(identifier:sourcename:deliverydate:displaydate:title:subtitle:body:threadidentifier:attributes:summary:actions:sourceicon:contexticon:attachments:))*