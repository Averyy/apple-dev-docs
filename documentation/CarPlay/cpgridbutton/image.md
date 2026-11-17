# image

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The image displayed on the button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var image: UIImage { get }
```

```objc
@property (nonatomic, readonly) UIImage * image;
```

## Discussion

When creating a grid button, don’t provide an animated image. If you do, the button uses the first image in the animation sequence.

## See Also

### Managing the button content
- [func updateImage(UIImage)](./updateimage%28_%29.md)
- [var titleVariants: [String]](./titlevariants.md)
  An array of title variants for the button.
- [func updateTitleVariants([String])](./updatetitlevariants%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridbutton/image)*