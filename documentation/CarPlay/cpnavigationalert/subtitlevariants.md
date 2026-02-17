# subtitleVariants

**Framework**: CarPlay  
**Kind**: property

An array of subtitle strings.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var subtitleVariants: [String] { get }
```

#### Discussion

Each subtitle should be localized and ready for display to the user. The system selects the subtitle to display based on the available screen space.

## See Also

- [var titleVariants: [String]](cpnavigationalert/titlevariants.md)
  An array of title strings.
- [func updateTitleVariants([String], subtitleVariants: [String])](cpnavigationalert/updatetitlevariants(_:subtitlevariants:).md)
  Updates title and subtitle variants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/subtitlevariants)*