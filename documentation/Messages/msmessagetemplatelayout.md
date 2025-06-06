# MSMessageTemplateLayout

**Framework**: Messages  
**Kind**: class

A template-based layout for custom messages.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MSMessageTemplateLayout
```

#### Overview

The [`MSMessageTemplateLayout`](msmessagetemplatelayout.md) describes how an [`MSMessage`](msmessage.md) object is presented in the transcript. The message template includes the Message extension’s icon, an image, video, or audio file, and a number of text elements (title, subtitle, caption, subcaption, trailing caption, and trailing subcaption). These elements are laid out as shown in [`Figure 1`](msmessagetemplatelayout#1965603.md).

![None](https://docs-assets.developer.apple.com/published/1901e82e59b3edc1aa1efc9684c8c7ee/media-1965603%402x.png)

To use the template:

1. Instantiate a new `MSMessageTemplateLayout` object.
2. Assign values to the properties representing the desired visual elements. You can leave unwanted elements set to `nil`. The system sizes the message balloon to fit the provided content.
3. Assign the `MSMessageTemplateLayout` object to the [`MSMessage`](msmessage.md) object’s [`layout`](msmessage/layout.md) property.

Do not subclass the `MSMessageTemplateLayout` class.

## Topics

### Assigning Visual Elements
- [var image: UIImage?](msmessagetemplatelayout/image.md)
  An image used to represent the message in the transcript.
- [var mediaFileURL: URL?](msmessagetemplatelayout/mediafileurl.md)
  A media file used to represent the message in the transcript.
- [var imageTitle: String?](msmessagetemplatelayout/imagetitle.md)
  The title for the image or media file.
- [var imageSubtitle: String?](msmessagetemplatelayout/imagesubtitle.md)
  The subtitle for the image or media file.
- [var caption: String?](msmessagetemplatelayout/caption.md)
  A left-aligned caption for the message bubble.
- [var subcaption: String?](msmessagetemplatelayout/subcaption.md)
  A left-aligned subcaption for the message bubble.
- [var trailingCaption: String?](msmessagetemplatelayout/trailingcaption.md)
  A right-aligned caption for the message bubble.
- [var trailingSubcaption: String?](msmessagetemplatelayout/trailingsubcaption.md)
  A right-aligned subcaption for the message bubble.

## Relationships

### Inherits From
- [MSMessageLayout](msmessagelayout.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MSMessage](msmessage.md)
  A custom message object.
- [class MSSession](mssession.md)
  A session object used to create and update messages.
- [class MSMessageLayout](msmessagelayout.md)
  An abstract base class that defines the appearance of [`MSMessage`](msmessage.md) objects in the conversation transcript.
- [class MSMessageLiveLayout](msmessagelivelayout.md)
  A layout that provides a custom, interactive view inside the transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagetemplatelayout)*