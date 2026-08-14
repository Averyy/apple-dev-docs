# CKNotification.ID

**Framework**: CloudKit  
**Kind**: class

An object that uniquely identifies a push notification that a container sends.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class ID
```

#### Overview

You don’t create notification IDs directly. The server creates them when it creates instances of [`CKNotification`](cknotification.md) that correspond to the push notifications that CloudKit sends to your app. You can compare two IDs using the [`isEqual(_:)`](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/isequal(_:)) method to determine whether two notifications are the same. This class defines no methods or properties.

## Topics

### Initializers
- [init?(coder: NSCoder)](cknotification/id/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var notificationID: CKNotification.ID?](cknotification/notificationid.md)
  The notification’s ID.
- [var notificationType: CKNotification.NotificationType](cknotification/notificationtype-swift.property.md)
  The type of event that generates the notification.
- [CKNotification.NotificationType](cknotification/notificationtype-swift.enum.md)
  Constants that indicate the type of event that generates the push notification.
- [var containerIdentifier: String?](cknotification/containeridentifier.md)
  The ID of the container with the content that triggers the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/id)*