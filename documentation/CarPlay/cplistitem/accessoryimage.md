# accessoryImage

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The custom accessory image to display on the trailing edge of the list item.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var accessoryImage: UIImage? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIImage * accessoryImage;
```

## Discussion

If the [`accessoryType`](./accessorytype.md) property is set to [`CPListItemAccessoryType.none`](../cplistitemaccessorytype/none.md), the list item displays the image in this property. To change the accessory image in this property, call the [`setAccessoryImage(_:)`](./setaccessoryimage%28_%29.md) method.

## See Also

### Managing accessories
- [var accessoryType: CPListItemAccessoryType](./accessorytype.md)
  The standard accessory type to display on the trailing edge of the list item.
- [func setAccessoryImage(UIImage?)](./setaccessoryimage%28_%29.md)
  The custom accessory image to display on the trailing edge of the list item.
- [enum CPListItemAccessoryType](../cplistitemaccessorytype.md)
  The standard image types a list item can display in its accessory region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/accessoryimage)*