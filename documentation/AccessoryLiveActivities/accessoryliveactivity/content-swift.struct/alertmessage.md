# AccessoryLiveActivity.Content.AlertMessage

**Framework**: Accessory Live Activities  
**Kind**: struct  
**Role**: Structure

The content you use as an alert for a Live Activity update on your accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
struct AlertMessage
```

#### Overview

Use the message’s [`title`](./alertmessage/title.md) and [`body`](./alertmessage/body.md) properties to create a notification-style alert on your accessory.

## Topics

### Accessing alert text
- [let title: String](./alertmessage/title.md)
  The title of the alert.
- [let body: String](./alertmessage/body.md)
  The body text of the alert.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Alerting people
- [let alert: AccessoryLiveActivity.Content.AlertMessage?](./alert.md)
  The Live Activity update’s alert message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/accessoryliveactivity/content-swift.struct/alertmessage)*