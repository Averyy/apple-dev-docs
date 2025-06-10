# accessoryType

**Framework**: CarPlay  
**Kind**: property

The accessory that the list item displays in its trailing region.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
var accessoryType: CPListItemAccessoryType { get set }
```

#### Discussion

If you update the list item to display an accessory image using the [`setAccessoryImage(_:)`](cplistitem/setaccessoryimage(_:).md) method, CarPlay sets this property’s value to [`CPListItemAccessoryType.none`](cplistitemaccessorytype/none.md).

## See Also

- [enum CPListItemAccessoryType](cplistitemaccessorytype.md)
  The accessory types that a list item can display.
- [var accessoryImage: UIImage?](cplistitem/accessoryimage.md)
  The image that the list item displays in its trailing region.
- [func setAccessoryImage(UIImage?)](cplistitem/setaccessoryimage(_:).md)
  Updates the list item’s accessory image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/accessorytype)*