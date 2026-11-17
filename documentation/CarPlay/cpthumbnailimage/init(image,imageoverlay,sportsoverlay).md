# init(image:imageOverlay:sportsOverlay:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a thumbnail with an image object and optional overlays.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(image: UIImage, imageOverlay: CPImageOverlay?, sportsOverlay: CPSportsOverlay?)
```

```objc
- (instancetype) initWithImage:(UIImage *) image imageOverlay:(CPImageOverlay *) imageOverlay sportsOverlay:(CPSportsOverlay *) sportsOverlay;
```

## Return Value

An initialized thumbnail image with optional overlays.

## Discussion

You can combine an image and sports overlay on the same thumbnail image. Sports overlays have a fixed placement for content, but you can customize the placement of an image overlay.

## Parameters

- `image`: The image to display. Get the maximum image size from the [`maximumImageSize(forAspectRatio:)`](./maximumimagesize%28foraspectratio%29.md) method. If you specify a larger or smaller image, this initializer scales the image to the maximum size. When scaling the image, the method retains the image’s width/height aspect ratio if that ratio is greater than `0.5` and less than `1.8`. If the image’s aspect ratio is outside those bounds, the method changes the aspect ratio to the nearest boundary before rescaling.
- `imageOverlay`: An overlay to display on top of the thumbnail image. Specify `nil` to omit this overlay.
- `sportsOverlay`: A sports overlay to display on top of the thumbnail image. Specify `nil` to omit this overlay.

## See Also

### Creating a thumbnail image
- [init(image: UIImage)](./init%28image%29.md)
  Creates a thumbnail with an image object.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpthumbnailimage/init(image:imageoverlay:sportsoverlay:))*