# CPListItemAccessoryType

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

The accessory types that a list item can display.

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

#### Overview

Use these constants to set the value of a list item’s [`accessoryType`](./cplistitem/accessorytype.md) property. An accessory can provide additional context for a list item’s contents, or help communicate its behavior.

## Topics

### Accessory Types
- [CPListItemAccessoryType.none](./cplistitemaccessorytype/none.md)
  Don’t show an accessory.
- [CPListItemAccessoryType.disclosureIndicator](./cplistitemaccessorytype/disclosureindicator.md)
  Show a chevron icon.
- [CPListItemAccessoryType.cloud](./cplistitemaccessorytype/cloud.md)
  Show a cloud icon.
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

### Managing Accessories
- [var accessoryType: CPListItemAccessoryType](./cplistitem/accessorytype.md)
  The accessory that the list item displays in its trailing region.
- [var accessoryImage: UIImage?](./cplistitem/accessoryimage.md)
  The image that the list item displays in its trailing region.
- [func setAccessoryImage(UIImage?)](./cplistitem/setaccessoryimage%28_%29.md)
  Updates the list item’s accessory image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitemaccessorytype)*