# imageOverlay

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An overlay with a custom image or text badge.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var imageOverlay: CPImageOverlay? { get set }
```

```objc
@property (nonatomic, strong, nullable) CPImageOverlay * imageOverlay;
```

## Discussion

Use this property to add or update the overlay for the thumbnail image. This overlay displays the specified image or text with the alignment your overlay specifies. If you didn’t provide an overlay at initialization time, the default value of this property is `nil`.

## See Also

### Getting the thumbnail content
- [var image: UIImage](./image.md)
  The main image to display.
- [var sportsOverlay: CPSportsOverlay?](./sportsoverlay.md)
  An overlay with sporting event details, including the teams and current score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpthumbnailimage/imageoverlay)*