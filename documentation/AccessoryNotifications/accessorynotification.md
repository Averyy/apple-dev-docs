# AccessoryNotification

**Framework**: Accessory Notifications  
**Kind**: struct

A structure that contains the details of a notification that iOS provides to your accessory.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct AccessoryNotification
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Overview

The notification includes display elements, metadata, interactive components, and rich content such as icons, attachments, and Apple Intelligence summaries.

## Topics

### Creating a notification
- [init(identifier: AccessoryNotification.Identifier, sourceName: String, deliveryDate: Date, displayDate: AccessoryNotification.DisplayDate, title: String?, subtitle: String?, body: NSAttributedString?, threadIdentifier: String?, attributes: AccessoryNotification.Attributes, summary: NSAttributedString?, actions: [AccessoryNotification.Action], sourceIcon: AccessoryNotification.File?, contextIcon: AccessoryNotification.File?, attachments: [AccessoryNotification.File])](accessorynotification/init(identifier:sourcename:deliverydate:displaydate:title:subtitle:body:threadidentifier:attributes:summary:actions:sourceicon:contexticon:attachments:).md)
  Initializes an accessory notification.
### Displaying notification content
- [let title: String?](accessorynotification/title.md)
  A primary text for the notification.
- [let subtitle: String?](accessorynotification/subtitle.md)
  Secondary text for the notification.
- [let body: NSAttributedString?](accessorynotification/body.md)
  A string that contains the notification’s main content.
- [let summary: NSAttributedString?](accessorynotification/summary.md)
  An Apple Intelligence summary for the notification.
### Working with notification attributes
- [let attributes: AccessoryNotification.Attributes](accessorynotification/attributes-swift.property.md)
  A set of attributes that indicate the notification’s priority level.
- [AccessoryNotification.Attributes](accessorynotification/attributes-swift.struct.md)
  Attributes that display priority for a notification.
### Accessing related media
- [let attachments: [AccessoryNotification.File]](accessorynotification/attachments.md)
  An array of files sent with the notification.
- [let sourceIcon: AccessoryNotification.File?](accessorynotification/sourceicon.md)
  An icon that represents the app that sent the notification.
- [let contextIcon: AccessoryNotification.File?](accessorynotification/contexticon.md)
  A secondary icon that provides additional contextual information about the notification.
- [AccessoryNotification.File](accessorynotification/file.md)
  A file associated with a notification.
### Identifying and grouping notifications
- [let identifier: AccessoryNotification.Identifier](accessorynotification/identifier-swift.property.md)
  A structure that uniquely identifies the notification.
- [AccessoryNotification.Identifier](accessorynotification/identifier-swift.struct.md)
  A structure that uniquely identifies a notification.
- [let threadIdentifier: String?](accessorynotification/threadidentifier.md)
  An identifier that groups notifications that belong to the same thread.
- [let sourceName: String](accessorynotification/sourcename.md)
  A display name for the bundle that sent the notification.
### Working with notification dates
- [let deliveryDate: Date](accessorynotification/deliverydate.md)
  A timestamp that indicates when the system received the notification.
- [let displayDate: AccessoryNotification.DisplayDate](accessorynotification/displaydate-swift.property.md)
  A preferred date and format to display with the notification.
- [AccessoryNotification.DisplayDate](accessorynotification/displaydate-swift.enum.md)
  Options for displaying a date in a notification.
### Handling user interactions
- [let actions: [AccessoryNotification.Action]](accessorynotification/actions.md)
  An array of possible interactions that a person can have with the notification.
- [AccessoryNotification.Action](accessorynotification/action.md)
  A possible user interaction with a notification.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct AlertingContext](alertingcontext.md)
  A structure that provides guidance for how to alert for a notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification)*