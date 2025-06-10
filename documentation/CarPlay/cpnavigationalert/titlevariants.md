# titleVariants

**Framework**: CarPlay  
**Kind**: property

An array of title strings.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var titleVariants: [String] { get }
```

#### Discussion

Each title should be localized and ready for display to the user. The system selects the title to display based on the available screen space.

## See Also

- [var subtitleVariants: [String]](cpnavigationalert/subtitlevariants.md)
  An array of subtitle strings.
- [func updateTitleVariants([String], subtitleVariants: [String])](cpnavigationalert/updatetitlevariants(_:subtitlevariants:).md)
  Updates title and subtitle variants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/titlevariants)*