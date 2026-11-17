# init(image:alignment:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates an overlay that displays an image.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(image: UIImage, alignment: CPImageOverlay.Alignment)
```

```objc
- (instancetype) initWithImage:(UIImage *) image alignment:(CPImageOverlayAlignment) alignment;
```

## Return Value

An overlay object with the image.

## Discussion

After creating the overlay object, initialize a [`CPThumbnailImage`](../cpthumbnailimage.md) object with it or assign it to the thumbnail image’s [`imageOverlay`](../cpthumbnailimage/imageoverlay.md) property.

## Parameters

- `image`: The image to display on top of the thumbnail image.
- `alignment`: The placement of the image on the thumbnail. Overlays appear inside the top edge of the thumbnail image and with the placement you specify in this parameter.

## See Also

### Creating an image overlay
- [init(text: String, textColor: UIColor, backgroundColor: UIColor, alignment: CPImageOverlay.Alignment)](./init%28text,textcolor,backgroundcolor,alignment%29.md)
  Creates an overlay that displays text in a colored badge.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpimageoverlay/init(image:alignment:))*