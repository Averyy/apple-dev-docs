# image

**Framework**: CarPlay  
**Kind**: property

The image the button displays.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
var image: UIImage { get }
```

#### Discussion

CarPlays doesn’t support animated images. If you provide an animated image, the button displays only the first image in the animation sequence. The maximum supported image size is 30 x 30 points.

## See Also

- [var titleVariants: [String]](cpdashboardbutton/titlevariants.md)
  The array of title variants for the button.
- [var subtitleVariants: [String]](cpdashboardbutton/subtitlevariants.md)
  The array of subtitle variants for the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpdashboardbutton/image)*