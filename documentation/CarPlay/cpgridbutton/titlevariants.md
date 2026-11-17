# titleVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of title variants for the button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var titleVariants: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * titleVariants;
```

## Discussion

When the system displays the button, it selects the title that best fits the available screen space, so arrange the titles from most to least preferred when creating a grid button. Also, localize each title for display to the user, and be sure to include at least one title in the array.

## See Also

### Managing the button content
- [var image: UIImage](./image.md)
  The image displayed on the button.
- [func updateImage(UIImage)](./updateimage%28_%29.md)
- [func updateTitleVariants([String])](./updatetitlevariants%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridbutton/titlevariants)*