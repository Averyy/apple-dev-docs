# image

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The image the button displays.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
var image: UIImage { get }
```

```objc
@property (nonatomic, readonly) UIImage * image;
```

#### Discussion

CarPlays doesn’t support animated images. If you provide an animated image, the button displays only the first image in the animation sequence. The maximum supported image size is 30 x 30 points.

## See Also

### Accessing the Button Configuration
- [var titleVariants: [String]](./titlevariants.md)
  The array of title variants for the button.
- [var subtitleVariants: [String]](./subtitlevariants.md)
  The array of subtitle variants for the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpdashboardbutton/image)*