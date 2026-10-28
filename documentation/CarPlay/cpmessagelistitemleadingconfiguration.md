# CPMessageListItemLeadingConfiguration

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

An object that describes the appearance of a message list item’s leading region.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPMessageListItemLeadingConfiguration
```

```objc
@interface CPMessageListItemLeadingConfiguration : NSObject
```

## Overview

Use a leading configuration to describe the visual elements that a message list item’s leading region contains. The region can show a [`CPMessageLeadingItem`](./cpmessageleadingitem.md), an image, and an unread indicator.

Configurations are immutable. To modify the list item’s leading configuration, update its [`leadingConfiguration`](./cpmessagelistitem/leadingconfiguration.md) property with a new configuration. CarPlay detects the change and redraws the message list item.

## Topics

### Creating a Configuration
- [init(leadingItem: CPMessageLeadingItem, leadingImage: UIImage?, unread: Bool)](./cpmessagelistitemleadingconfiguration/init%28leadingitem,leadingimage,unread%29.md)
  Creates a leading configuration that contains an item and an image.
- [let CPMaximumMessageItemImageSize: CGSize](./cpmaximummessageitemimagesize.md)
  The maximum size of a message list item’s image.
### Getting the Leading Item
- [var leadingItem: CPMessageLeadingItem](./cpmessagelistitemleadingconfiguration/leadingitem.md)
  The configuration’s item.
- [enum CPMessageLeadingItem](./cpmessageleadingitem.md)
  The accessories that a message list item can display in its leading region.
### Getting the Configuration’s State
- [var leadingImage: UIImage?](./cpmessagelistitemleadingconfiguration/leadingimage.md)
  The configuration’s image.
- [var isUnread: Bool](./cpmessagelistitemleadingconfiguration/isunread.md)
  A Boolean value that determines whether the message list item displays an unread indicator.

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

### Managing Leading and Trailing Configurations
- [var leadingConfiguration: CPMessageListItemLeadingConfiguration](./cpmessagelistitem/leadingconfiguration.md)
  The configuration of the list item’s leading region.
- [var trailingConfiguration: CPMessageListItemTrailingConfiguration?](./cpmessagelistitem/trailingconfiguration.md)
  The configuration of the list item’s trailing region.
- [class CPMessageListItemTrailingConfiguration](./cpmessagelistitemtrailingconfiguration.md)
  An object that describes the appearance of a message list item’s trailing region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitemleadingconfiguration)*