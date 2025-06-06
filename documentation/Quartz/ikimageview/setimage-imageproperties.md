# setImage(_:imageProperties:)

**Framework**: Quartz  
**Kind**: method

Sets the image to display in an image view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setImage(_ image: CGImage!, imageProperties metaData: [AnyHashable : Any]!)
```

## Parameters

- `image`: The image to set.
- `metaData`: A dictionary that contains metadata that describes the image.

## See Also

- [func imageProperties() -> [AnyHashable : Any]!](ikimageview/imageproperties.md)
  Returns the metadata for the image in the view.
- [func image() -> Unmanaged<CGImage>!](ikimageview/image.md)
  Returns the image associated with the view, after any image corrections.
- [func setImageWith(URL!)](ikimageview/setimagewith(_:).md)
  Initializes an image view with the image specified by a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/setimage(_:imageproperties:))*