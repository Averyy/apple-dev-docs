# CPMessageListItemTrailingConfiguration

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that defines the content at the trailing edge of a message list item’s row.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPMessageListItemTrailingConfiguration
```

```objc
@interface CPMessageListItemTrailingConfiguration : NSObject
```

## Overview

A `CPMessageListItemLeadingConfiguration` object contains the content to display at the trailing edge of the row for a [`CPMessageListItem`](./cpmessagelistitem.md). Use this type to specify standard visual elements such as a mute button. You can also specify a custom image to display after the rest of the message information. CarPlay places this content after the portion of the row that shows the conversation name, contact name, and other primary text.

Create an instance of this type and configure it with the information you want to display for the current message list item. Initialize your [`CPMessageListItem`](./cpmessagelistitem.md) object with the instance you create. You can also change the trailing information later by assigning a new instance of this class to the [`trailingConfiguration`](./cpmessagelistitem/trailingconfiguration.md) property of the item.

## Topics

### Creating a configuration
- [init(trailingItem: CPMessageTrailingItem, trailingImage: UIImage?)](./cpmessagelistitemtrailingconfiguration/init%28trailingitem,trailingimage%29.md)
  Creates the configuration object with the items to display at the leading edge of the row.
### Getting the trailing item
- [var trailingItem: CPMessageTrailingItem](./cpmessagelistitemtrailingconfiguration/trailingitem.md)
  The standard system symbol to display in the row’s trailing region.
- [enum CPMessageTrailingItem](./cpmessagetrailingitem.md)
  Constants that indicate the type of symbol to display at the trailing edge of a message list row.
### Getting the trailing image
- [var trailingImage: UIImage?](./cpmessagelistitemtrailingconfiguration/trailingimage.md)
  The custom image to display in the row’s trailing region.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### List items
- [class CPMessageListItem](./cpmessagelistitem.md)
  A list template row that manages a text message thread or contact.
- [class CPMessageListItemLeadingConfiguration](./cpmessagelistitemleadingconfiguration.md)
  A type that defines the content at the leading edge of a message list item’s row.
- [let CPMaximumMessageItemImageSize: CGSize](./cpmaximummessageitemimagesize.md)
  The maximum size for images in the leading and trailing regions of a message list item.
- [let CPMaximumMessageItemLeadingDetailTextImageSize: CGSize](./cpmaximummessageitemleadingdetailtextimagesize.md)
  The maximum size for images in the detail text image of a message list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitemtrailingconfiguration)*