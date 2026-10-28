# accessoryType

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The accessory that the list item displays in its trailing region.

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

If you update the list item to display an accessory image using the [`setAccessoryImage(_:)`](./setaccessoryimage%28_%29.md) method, CarPlay sets this property’s value to [`CPListItemAccessoryType.none`](../cplistitemaccessorytype/none.md).

## See Also

### Managing Accessories
- [enum CPListItemAccessoryType](../cplistitemaccessorytype.md)
  The accessory types that a list item can display.
- [var accessoryImage: UIImage?](./accessoryimage.md)
  The image that the list item displays in its trailing region.
- [func setAccessoryImage(UIImage?)](./setaccessoryimage%28_%29.md)
  Updates the list item’s accessory image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/accessorytype)*