# CPMessageListItemTrailingConfiguration

**Framework**: CarPlay  
**Kind**: class

An object that describes the appearance of a message list item’s trailing region.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPMessageListItemTrailingConfiguration
```

#### Overview

Use a trailing configuration to describe the visual elements that a message list item’s trailing region contains. The region can show a [`CPMessageTrailingItem`](cpmessagetrailingitem.md) and an image.

Configurations are immutable. To modify the list item’s trailing configuration, update its [`trailingConfiguration`](cpmessagelistitem/trailingconfiguration.md) property with a new configuration. CarPlay detects the change and redraws the message list item.

## Topics

### Creating a Configuration
- [init(trailingItem: CPMessageTrailingItem, trailingImage: UIImage?)](cpmessagelistitemtrailingconfiguration/init(trailingitem:trailingimage:).md)
  Creates a trailing configuration that contains an item and an image.
- [let CPMaximumMessageItemImageSize: CGSize](cpmaximummessageitemimagesize.md)
  The maximum size of a message list item’s image.
### Getting the Trailing Item
- [var trailingItem: CPMessageTrailingItem](cpmessagelistitemtrailingconfiguration/trailingitem.md)
  The configuration’s item.
- [enum CPMessageTrailingItem](cpmessagetrailingitem.md)
  The accessories that a message list item can display in its trailing region.
### Getting the Trailing Image
- [var trailingImage: UIImage?](cpmessagelistitemtrailingconfiguration/trailingimage.md)
  The configuration’s image.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var leadingConfiguration: CPMessageListItemLeadingConfiguration](cpmessagelistitem/leadingconfiguration.md)
  The configuration of the list item’s leading region.
- [class CPMessageListItemLeadingConfiguration](cpmessagelistitemleadingconfiguration.md)
  An object that describes the appearance of a message list item’s leading region.
- [var trailingConfiguration: CPMessageListItemTrailingConfiguration?](cpmessagelistitem/trailingconfiguration.md)
  The configuration of the list item’s trailing region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitemtrailingconfiguration)*