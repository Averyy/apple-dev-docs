# CPListItemAccessoryType

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

The standard image types a list item can display in its accessory region.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum CPListItemAccessoryType
```

```c
enum CPListItemAccessoryType : NSInteger;
```

## Overview

Use these constants to set the value of a list item’s [`accessoryType`](./cplistitem/accessorytype.md) property. Assigning one of these values displays the specified image in the accessory region of the list item’s row. Choose an accessory type that provides relevant context about the item’s purpose. For example, display a disclosure indicator to signify that tapping the row takes the person to a new page of content.

## Topics

### Accessory types
- [CPListItemAccessoryType.none](./cplistitemaccessorytype/none.md)
  A value that indicates the list item has no standard accessory type.
- [CPListItemAccessoryType.disclosureIndicator](./cplistitemaccessorytype/disclosureindicator.md)
  A chevron image that signifies the item displays new content.
- [CPListItemAccessoryType.cloud](./cplistitemaccessorytype/cloud.md)
  A cloud image that signifies the item contains cloud-based content.
### Initializers
- [init?(rawValue: Int)](./cplistitemaccessorytype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing accessories
- [var accessoryType: CPListItemAccessoryType](./cplistitem/accessorytype.md)
  The standard accessory type to display on the trailing edge of the list item.
- [var accessoryImage: UIImage?](./cplistitem/accessoryimage.md)
  The custom accessory image to display on the trailing edge of the list item.
- [func setAccessoryImage(UIImage?)](./cplistitem/setaccessoryimage%28_%29.md)
  The custom accessory image to display on the trailing edge of the list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitemaccessorytype)*