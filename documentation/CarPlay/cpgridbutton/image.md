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

#### Discussion

When creating a grid button, don’t provide an animated image. If you do, the button uses the first image in the animation sequence.

## See Also

### Obtaining Grid Button Information
- [var titleVariants: [String]](./titlevariants.md)
  An array of title variants for the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridbutton/image)*