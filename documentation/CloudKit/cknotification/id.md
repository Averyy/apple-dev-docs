# CKNotification.ID

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that uniquely identifies a push notification that a container sends.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class ID
```

```objc
@interface CKNotificationID : NSObject
```

#### Overview

You don’t create notification IDs directly. The server creates them when it creates instances of [`CKNotification`](../cknotification.md) that correspond to the push notifications that CloudKit sends to your app. You can compare two IDs using the [`isEqual(_:)`](../../ObjectiveC/nsobjectprotocol/isequal%28_%29.md) method to determine whether two notifications are the same. This class defines no methods or properties.

## Topics

### Initializers
- [init?(coder: NSCoder)](./id/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identifying the Notification
- [var notificationID: CKNotification.ID?](./notificationid.md)
  The notification’s ID.
- [var notificationType: CKNotification.NotificationType](./notificationtype-swift.property.md)
  The type of event that generates the notification.
- [CKNotification.NotificationType](./notificationtype-swift.enum.md)
  Constants that indicate the type of event that generates the push notification.
- [var containerIdentifier: String?](./containeridentifier.md)
  The ID of the container with the content that triggers the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/id)*