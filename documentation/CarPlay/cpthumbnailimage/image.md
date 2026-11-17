# image

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The main image to display.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var image: UIImage { get set }
```

```objc
@property (nonatomic, strong) UIImage * image;
```

## Discussion

This method resizes the image to fit the expected size of row elements. If you assign a new image to this property, make sure the image’s width/height aspect ratio is in the range `0.5` to `1.8`. If the aspect ratio is outside those bounds, the method changes the aspect ratio to the nearest boundary before resizing.

## See Also

### Getting the thumbnail content
- [var imageOverlay: CPImageOverlay?](./imageoverlay.md)
  An overlay with a custom image or text badge.
- [var sportsOverlay: CPSportsOverlay?](./sportsoverlay.md)
  An overlay with sporting event details, including the teams and current score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpthumbnailimage/image)*