# image()

**Framework**: Quartz  
**Kind**: method

Returns the image associated with the view, after any image corrections.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func image() -> Unmanaged<CGImage>!
```

#### Return Value

The image.

## See Also

- [func setImage(CGImage!, imageProperties: [AnyHashable : Any]!)](ikimageview/setimage(_:imageproperties:).md)
  Sets the image to display in an image view.
- [func setImageWith(URL!)](ikimageview/setimagewith(_:).md)
  Initializes an image view with the image specified by a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/image())*