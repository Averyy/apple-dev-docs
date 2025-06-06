# titleVariants

**Framework**: CarPlay  
**Kind**: property

The array of title variants for the button.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
var titleVariants: [String] { get }
```

#### Discussion

An array of title variants for this button in an arrangement from most- to least-preferred. The system selects a title from this array that best fits the available space. You provide the title variants to [`init(titleVariants:subtitleVariants:image:handler:)`](cpdashboardbutton/init(titlevariants:subtitlevariants:image:handler:).md) as localized, displayable content.

## See Also

- [var subtitleVariants: [String]](cpdashboardbutton/subtitlevariants.md)
  The array of subtitle variants for the button.
- [var image: UIImage](cpdashboardbutton/image.md)
  The image the button displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpdashboardbutton/titlevariants)*