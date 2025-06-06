# CPMessageListItem

**Framework**: CarPlay  
**Kind**: class

A list template row that represents a conversation or contact.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPMessageListItem
```

#### Overview

Use `CPMessageListItem` to display information about a conversation or a contact in a list template. Unlike [`CPListItem`](cplistitem.md), you don’t provide a selection handler. Instead, when the user selects the row, CarPlay invokes Siri using the parameters you provide and begins a message compose, read, or reply flow.

The behavior of the list item when the user selects it depends on how you initialize or configure it. If the item has a phone number or email address, Siri launches the message compose flow. If the list item has an unread indicator, Siri launches the message read flow. Otherwise, Siri launches the message reply flow.

`CPMessageListItem` can display various auxiliary items in its leading and trailing regions. You describe these using a configuration object for each region. See [`leadingConfiguration`](cpmessagelistitem/leadingconfiguration.md) and [`trailingConfiguration`](cpmessagelistitem/trailingconfiguration.md) for more information.

CarPlay doesn’t support custom list item types. Instead, use the [`userInfo`](cpmessagelistitem/userinfo.md) property to attach a value to the list item that provides additional context, such as specifying  a model object that corresponds to the item.

> **Note**:  `CPMessageListItem` is available only in apps that have the communication entitlement.

 `CPMessageListItem` is available only in apps that have the communication entitlement.

## Topics

### Creating a Message List Item
- [init(conversationIdentifier: String, text: String, leadingConfiguration: CPMessageListItemLeadingConfiguration, trailingConfiguration: CPMessageListItemTrailingConfiguration?, detailText: String?, trailingText: String?)](cpmessagelistitem/init(conversationidentifier:text:leadingconfiguration:trailingconfiguration:detailtext:trailingtext:).md)
  Creates a list item that represents an existing conversation.
- [init(fullName: String, phoneOrEmailAddress: String, leadingConfiguration: CPMessageListItemLeadingConfiguration, trailingConfiguration: CPMessageListItemTrailingConfiguration?, detailText: String?, trailingText: String?)](cpmessagelistitem/init(fullname:phoneoremailaddress:leadingconfiguration:trailingconfiguration:detailtext:trailingtext:).md)
  Creates a list item that represents a contact.
### Managing the Message Context
- [var conversationIdentifier: String?](cpmessagelistitem/conversationidentifier.md)
  The conversation’s unique identifier.
- [var phoneOrEmailAddress: String?](cpmessagelistitem/phoneoremailaddress.md)
  The contact’s phone number or email address.
### Managing Content
- [var text: String?](cpmessagelistitem/text.md)
  The list item’s primary text.
- [var detailText: String?](cpmessagelistitem/detailtext.md)
  The list item’s secondary text.
- [var trailingText: String?](cpmessagelistitem/trailingtext.md)
  The list item’s supplementary text.
### Managing Leading and Trailing Configurations
- [var leadingConfiguration: CPMessageListItemLeadingConfiguration](cpmessagelistitem/leadingconfiguration.md)
  The configuration of the list item’s leading region.
- [class CPMessageListItemLeadingConfiguration](cpmessagelistitemleadingconfiguration.md)
  An object that describes the appearance of a message list item’s leading region.
- [var trailingConfiguration: CPMessageListItemTrailingConfiguration?](cpmessagelistitem/trailingconfiguration.md)
  The configuration of the list item’s trailing region.
- [class CPMessageListItemTrailingConfiguration](cpmessagelistitemtrailingconfiguration.md)
  An object that describes the appearance of a message list item’s trailing region.
### Managing Supplementary Information
- [var userInfo: Any?](cpmessagelistitem/userinfo.md)
  An opaque value for the list item.
### Enabling Items
- [var isEnabled: Bool](cpmessagelistitem/isenabled.md)
  A Boolean value that indicates if the item is enabled.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CPListTemplateItem](cplisttemplateitem.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init(items: [any CPListTemplateItem], header: String, headerSubtitle: String?, headerImage: UIImage?, headerButton: CPButton?, sectionIndexTitle: String?)](cplistsection/init(items:header:headersubtitle:headerimage:headerbutton:sectionindextitle:).md)
  Creates a section with list items, a header, a section index title, and section header details.
- [protocol CPListTemplateItem](cplisttemplateitem.md)
  A description of the common properties of all list item types.
- [protocol CPSelectableListItem](cpselectablelistitem.md)
  A description of a selectable list item.
- [class CPListItem](cplistitem.md)
  A selectable row in a list template.
- [class CPListImageRowItem](cplistimagerowitem.md)
  A list template row that displays a series of images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem)*