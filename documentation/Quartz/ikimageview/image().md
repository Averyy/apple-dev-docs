# image()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the image associated with the view, after any image corrections.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func image() -> Unmanaged<CGImage>!
```

```objc
- (CGImageRef) image;
```

## Return Value

The image.

## See Also

### Getting and Setting Images
- [func setImage(CGImage!, imageProperties: [AnyHashable : Any]!)](./setimage%28_,imageproperties%29.md)
  Sets the image to display in an image view.
- [func setImageWith(URL!)](./setimagewith%28_%29.md)
  Initializes an image view with the image specified by a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/image())*