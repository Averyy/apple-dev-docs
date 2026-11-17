# setAccessoryImage(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

The custom accessory image to display on the trailing edge of the list item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func setAccessoryImage(_ accessoryImage: UIImage?)
```

```objc
- (void) setAccessoryImage:(UIImage *) accessoryImage;
```

## Discussion

If the [`accessoryType`](./accessorytype.md) property is set to [`CPListItemAccessoryType.none`](../cplistitemaccessorytype/none.md), the list item displays the image in this property. If the value of this property is `nil`, the system omits the accessory image. To change the accessory image in this property, call the [`setAccessoryImage(_:)`](./setaccessoryimage%28_%29.md) method.

## See Also

### Managing accessories
- [var accessoryType: CPListItemAccessoryType](./accessorytype.md)
  The standard accessory type to display on the trailing edge of the list item.
- [var accessoryImage: UIImage?](./accessoryimage.md)
  The custom accessory image to display on the trailing edge of the list item.
- [enum CPListItemAccessoryType](../cplistitemaccessorytype.md)
  The standard image types a list item can display in its accessory region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/setaccessoryimage(_:))*