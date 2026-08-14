# NSBundleResourceRequest.LowDiskSpaceMessage

**Framework**: Foundation  
**Kind**: struct

A message the system sends when it detects the amount of available disk space getting low.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct LowDiskSpaceMessage
```

#### Overview

After receiving this notification, your app should release any on-demand resources that aren’t required. Call [`endAccessingResources()`](nsbundleresourcerequest/endaccessingresources().md) to release the managed resources. If the app is in the background and the app doesn’t free up enough space, the system may terminate the app.

Observe this message with the identifier [`lowDiskSpace`](notificationcenter/messageidentifier/lowdiskspace.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`NSBundleResourceRequest`](nsbundleresourcerequest.md).

This message interoperates with the notification [`NSBundleResourceRequestLowDiskSpace`](nsnotification/name-swift.struct/nsbundleresourcerequestlowdiskspace.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message
- [init()](nsbundleresourcerequest/lowdiskspacemessage/init.md)
  Creates a message about the available disk space getting low.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/lowdiskspacemessage)*