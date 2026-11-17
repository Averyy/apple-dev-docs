# CPMessageListItem

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A list template row that manages a text message thread or contact.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPMessageListItem
```

```objc
@interface CPMessageListItem : NSObject
```

## Overview

When your communication app displays a list of someone’s contacts or conversations, create the rows of your list using `CPMessageListItem` objects instead of a custom type. Message list items offer a standard way for communication apps to share conversation and contact information, while still giving you ways to customize the content for your app. Each row shows the name of the thread or contact and offers ways to display additional text and images. Rows also offer ways to show common information. For example, message list items offer standard ways to mark a conversation as unread or mark a contact as a favorite.

Unlike most rows in a list, `CPMessageListItem` objects don’t require you to provide a handler to respond to interactions with the row. Interactions occur via Siri, which uses your app’s existing SiriKit support to compose, read, and reply to messages or phone calls. If you create the item with a phone number or email address, Siri initiates your app’s workflow for composing a message. If an item has an unread indicator, Siri reads the message. In all other cases, Siri initiates the message reply workflow. To support the required workflows, make sure to handle the [`INSendMessageIntent`](../Intents/insendmessageintent.md), [`INSearchForMessagesIntent`](../Intents/insearchformessagesintent.md), and [`INSetMessageAttributeIntent`](../Intents/insetmessageattributeintent.md) types in your app’s SiriKit code.

Each `CPMessageListItem` object you create has three regions: a leading region, a content region, and a trailing region. The leading region displays unread or favorite indicators and an optional image. The trailing region displays optional images and text that are relevant for your content. The content region contains the name of the contact or message thread and additional information you want the person to know. For example, a contact row might have additional text to explain whether it’s the person’s work or personal phone number. Configure this information when you first create the row and update it as needed using the properties of this class.

> **Note**: You can use this class in your app only if it has the CarPlay communication entitlement.

## Topics

### Creating a message list item
- [init(conversationIdentifier: String, text: String, leadingConfiguration: CPMessageListItemLeadingConfiguration, trailingConfiguration: CPMessageListItemTrailingConfiguration?, detailText: String?, trailingText: String?)](./cpmessagelistitem/init%28conversationidentifier,text,leadingconfiguration,trailingconfiguration,detailtext,trailingtext%29.md)
  Creates a message list item with the identifier for one of your app’s conversations.
- [init(fullName: String, phoneOrEmailAddress: String, leadingConfiguration: CPMessageListItemLeadingConfiguration, trailingConfiguration: CPMessageListItemTrailingConfiguration?, detailText: String?, trailingText: String?)](./cpmessagelistitem/init%28fullname,phoneoremailaddress,leadingconfiguration,trailingconfiguration,detailtext,trailingtext%29.md)
  Creates a message list item with the identifier for one of your app’s conversations.
### Getting the message context
- [var conversationIdentifier: String?](./cpmessagelistitem/conversationidentifier.md)
  The app-specific identifier for the message conversation.
- [var phoneOrEmailAddress: String?](./cpmessagelistitem/phoneoremailaddress.md)
  The phone or email address of the contact.
### Getting the row content
- [var text: String?](./cpmessagelistitem/text.md)
  The primary text to display in the message list item’s row.
- [var detailText: String?](./cpmessagelistitem/detailtext.md)
  Additional text to display less prominently below the row’s main text.
- [var trailingText: String?](./cpmessagelistitem/trailingtext.md)
  Additional text to display after the trailing configuration items.
- [var leadingDetailTextImage: UIImage?](./cpmessagelistitem/leadingdetailtextimage.md)
  An image to display before the row’s detail text.
### Configuring additional details
- [var leadingConfiguration: CPMessageListItemLeadingConfiguration](./cpmessagelistitem/leadingconfiguration.md)
  Additional content to display at the leading edge of the row.
- [var trailingConfiguration: CPMessageListItemTrailingConfiguration?](./cpmessagelistitem/trailingconfiguration.md)
  Additional content to display at the trailing edge of the row.
- [var userInfo: Any?](./cpmessagelistitem/userinfo.md)
  Custom information you want to store with the message list item.
### Enabling the item
- [var isEnabled: Bool](./cpmessagelistitem/isenabled.md)
  A Boolean value that indicates whether the row is enabled.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CPListTemplateItem](./cplisttemplateitem.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### List items
- [class CPMessageListItemLeadingConfiguration](./cpmessagelistitemleadingconfiguration.md)
  A type that defines the content at the leading edge of a message list item’s row.
- [class CPMessageListItemTrailingConfiguration](./cpmessagelistitemtrailingconfiguration.md)
  A type that defines the content at the trailing edge of a message list item’s row.
- [let CPMaximumMessageItemImageSize: CGSize](./cpmaximummessageitemimagesize.md)
  The maximum size for images in the leading and trailing regions of a message list item.
- [let CPMaximumMessageItemLeadingDetailTextImageSize: CGSize](./cpmaximummessageitemleadingdetailtextimagesize.md)
  The maximum size for images in the detail text image of a message list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem)*