# accessoryType

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The standard accessory type to display on the trailing edge of the list item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var accessoryType: CPListItemAccessoryType { get set }
```

```objc
@property (nonatomic, assign) CPListItemAccessoryType accessoryType;
```

## Discussion

The value in this property determines whether to show a standard accessory image such as a disclosure chevron or a custom image you supply. When the value in this property is a value other than [`CPListItemAccessoryType.none`](../cplistitemaccessorytype/none.md), the list item displays the specified standard accessory image. Setting the value to [`CPListItemAccessoryType.none`](../cplistitemaccessorytype/none.md) displays the custom image in the [`accessoryImage`](./accessoryimage.md) property if you provided one; otherwise, the item omits the accessory image.

## See Also

### Managing accessories
- [var accessoryImage: UIImage?](./accessoryimage.md)
  The custom accessory image to display on the trailing edge of the list item.
- [func setAccessoryImage(UIImage?)](./setaccessoryimage%28_%29.md)
  The custom accessory image to display on the trailing edge of the list item.
- [enum CPListItemAccessoryType](../cplistitemaccessorytype.md)
  The standard image types a list item can display in its accessory region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/accessorytype)*