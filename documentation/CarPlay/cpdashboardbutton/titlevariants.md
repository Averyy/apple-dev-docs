# titleVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The array of title variants for the button.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
var titleVariants: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * titleVariants;
```

## Discussion

An array of title variants for this button in an arrangement from most- to least-preferred. The system selects a title from this array that best fits the available space. You provide the title variants to [`init(titleVariants:subtitleVariants:image:handler:)`](./init%28titlevariants,subtitlevariants,image,handler%29.md) as localized, displayable content.

## See Also

### Accessing the Button Configuration
- [var subtitleVariants: [String]](./subtitlevariants.md)
  The array of subtitle variants for the button.
- [var image: UIImage](./image.md)
  The image the button displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpdashboardbutton/titlevariants)*