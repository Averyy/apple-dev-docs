# CPListItemAccessoryType

**Framework**: CarPlay  
**Kind**: enum

The accessory types that a list item can display.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum CPListItemAccessoryType
```

#### Overview

Use these constants to set the value of a list item’s [`accessoryType`](cplistitem/accessorytype.md) property. An accessory can provide additional context for a list item’s contents, or help communicate its behavior.

## Topics

### Accessory Types
- [CPListItemAccessoryType.none](cplistitemaccessorytype/none.md)
  Don’t show an accessory.
- [CPListItemAccessoryType.disclosureIndicator](cplistitemaccessorytype/disclosureindicator.md)
  Show a chevron icon.
- [CPListItemAccessoryType.cloud](cplistitemaccessorytype/cloud.md)
  Show a cloud icon.
### Initializers
- [init?(rawValue: Int)](cplistitemaccessorytype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var accessoryType: CPListItemAccessoryType](cplistitem/accessorytype.md)
  The accessory that the list item displays in its trailing region.
- [var accessoryImage: UIImage?](cplistitem/accessoryimage.md)
  The image that the list item displays in its trailing region.
- [func setAccessoryImage(UIImage?)](cplistitem/setaccessoryimage(_:).md)
  Updates the list item’s accessory image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitemaccessorytype)*