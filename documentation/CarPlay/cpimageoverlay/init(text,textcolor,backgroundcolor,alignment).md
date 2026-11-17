# init(text:textColor:backgroundColor:alignment:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates an overlay that displays text in a colored badge.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(text: String, textColor: UIColor, backgroundColor: UIColor, alignment: CPImageOverlay.Alignment)
```

```objc
- (instancetype) initWithText:(NSString *) text textColor:(UIColor *) textColor backgroundColor:(UIColor *) backgroundColor alignment:(CPImageOverlayAlignment) alignment;
```

## Return Value

An overlay object with the specified text information.

## Discussion

After creating the overlay object, initialize a [`CPThumbnailImage`](../cpthumbnailimage.md) object with it or assign it to the thumbnail image’s [`imageOverlay`](../cpthumbnailimage/imageoverlay.md) property.

## Parameters

- `text`: The text to display in the badge. Restrict the amount of text you provide to only a few characters. If the amount of text is too large to fit in the boundaries of the thumbnail image, CarPlay truncates the text to make it fit.
- `textColor`: The color to apply to the text. Choose a color that contrasts with `backgroundColor`.
- `backgroundColor`: The color to apply to the badge platter. Choose a color that contrasts with `textColor`.
- `alignment`: The placement of the badge on the thumbnail. Overlays appear inside the top edge of the thumbnail image and with the placement you specify in this parameter.

## See Also

### Creating an image overlay
- [init(image: UIImage, alignment: CPImageOverlay.Alignment)](./init%28image,alignment%29.md)
  Creates an overlay that displays an image.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpimageoverlay/init(text:textcolor:backgroundcolor:alignment:))*