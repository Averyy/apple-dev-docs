# pictureInPictureButtonStopImage

**Framework**: AVKit  
**Kind**: property  
**Role**: Type Property

A system-default template image for the button that stops Picture in Picture in your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
class var pictureInPictureButtonStopImage: UIImage { get }
```

*macOS*

```swift
class var pictureInPictureButtonStopImage: NSImage { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (class, nonatomic, readonly) UIImage * pictureInPictureButtonStopImage;
```

*macOS*

```objc
@property (class, nonatomic, readonly) NSImage * pictureInPictureButtonStopImage;
```

## Mentions

- [Adopting Picture in Picture in a custom player](../adopting-picture-in-picture-in-a-custom-player.md)

## See Also

### Retrieving Picture in Picture template images
- [class var pictureInPictureButtonStartImage: UIImage](./pictureinpicturebuttonstartimage.md)
  A system-default template image for the button that starts Picture in Picture in your app.
- [class func pictureInPictureButtonStartImage(compatibleWith: UITraitCollection?) -> UIImage](./pictureinpicturebuttonstartimage%28compatiblewith%29.md)
  Returns a system-default template image that’s compatible with a trait collection for the button that starts Picture in Picture in your app.
- [class func pictureInPictureButtonStopImage(compatibleWith: UITraitCollection?) -> UIImage](./pictureinpicturebuttonstopimage%28compatiblewith%29.md)
  Returns a system-default template image that’s compatible with a trait collection for the button that stops Picture in Picture in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/pictureinpicturebuttonstopimage)*