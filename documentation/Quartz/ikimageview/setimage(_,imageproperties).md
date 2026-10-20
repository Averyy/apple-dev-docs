# setImage(_:imageProperties:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets the image to display in an image view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setImage(_ image: CGImage!, imageProperties metaData: [AnyHashable : Any]!)
```

```objc
- (void) setImage:(CGImageRef) image imageProperties:(NSDictionary *) metaData;
```

## Parameters

- `image`: The image to set.
- `metaData`: A dictionary that contains metadata that describes the image.

## See Also

### Related Documentation
- [func imageProperties() -> [AnyHashable : Any]!](./imageproperties%28%29.md)
  Returns the metadata for the image in the view.
### Getting and Setting Images
- [func image() -> Unmanaged<CGImage>!](./image%28%29.md)
  Returns the image associated with the view, after any image corrections.
- [func setImageWith(URL!)](./setimagewith%28_%29.md)
  Initializes an image view with the image specified by a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/setimage(_:imageproperties:))*