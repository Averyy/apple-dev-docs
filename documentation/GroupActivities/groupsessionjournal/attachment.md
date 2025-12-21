# GroupSessionJournal.Attachment

**Framework**: Group Activities  
**Kind**: struct

A container for the data you download.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct Attachment
```

## Mentions

- [Synchronizing data during a SharePlay activity](synchronizing-data-during-a-shareplay-activity.md)

#### Overview

When your app receives a new item, the system packages it in an [`GroupSessionJournal.Attachment`](groupsessionjournal/attachment.md) and delivers it to your app. Use this container type to download the contents of the file and decode it to a type that your app recognizes.

## Topics

### Downloading the attachment data
- [func load<AttachmentType>(AttachmentType.Type) async throws -> AttachmentType](groupsessionjournal/attachment/load(_:).md)
  Downloads the attachment data and asynchronously delivers it as the type you specify.
- [func loadMetadata<MetadataType>(of: MetadataType.Type) async throws -> MetadataType](groupsessionjournal/attachment/loadmetadata(of:).md)
  Downloads the metadata for the attachment asynchronously and delivers it as the type you specify.
### Identifying the attachment
- [var id: UUID](groupsessionjournal/attachment/id.md)
  The unique identifier for this attachment.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var attachments: GroupSessionJournal.Attachments](groupsessionjournal/attachments-swift.property.md)
  The currently available attachments for you to download and incorporate into your app.
- [GroupSessionJournal.Attachments](groupsessionjournal/attachments-swift.struct.md)
  An asynchronous sequence that contains one or more incoming attachment containers for you to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionjournal/attachment)*