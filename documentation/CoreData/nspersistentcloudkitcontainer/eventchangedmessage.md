# NSPersistentCloudKitContainer.EventChangedMessage

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

Posted when a CloudKit event occurs on the CloudKit private serial queue.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct EventChangedMessage
```

## Topics

### Instance Properties
- [let event: NSPersistentCloudKitContainer.Event](./eventchangedmessage/event.md)
  The CloudKit event that triggered this notification.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../../Foundation/notificationcenter/asyncmessage.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/eventchangedmessage)*