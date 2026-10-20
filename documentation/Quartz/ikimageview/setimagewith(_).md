# setImageWith(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Initializes an image view with the image specified by a URL.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setImageWith(_ url: URL!)
```

```objc
- (void) setImageWithURL:(NSURL *) url;
```

#### Discussion

This method is the preferred initializer for RAW images. If you use this method for a TIFF file that contains multiple images, only the first image is displayed.

## Parameters

- `url`: The URL that specifies the location of the image.

## See Also

### Getting and Setting Images
- [func image() -> Unmanaged<CGImage>!](./image%28%29.md)
  Returns the image associated with the view, after any image corrections.
- [func setImage(CGImage!, imageProperties: [AnyHashable : Any]!)](./setimage%28_,imageproperties%29.md)
  Sets the image to display in an image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/setimagewith(_:))*