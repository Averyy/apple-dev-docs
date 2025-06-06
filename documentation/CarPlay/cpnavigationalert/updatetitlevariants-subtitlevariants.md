# updateTitleVariants(_:subtitleVariants:)

**Framework**: CarPlay  
**Kind**: method

Updates title and subtitle variants.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func updateTitleVariants(_ newTitleVariants: [String], subtitleVariants newSubtitleVariants: [String])
```

#### Discussion

You can update the navigation alert with new title and subtitle variants before presenting the alert or after displaying it. Updating a dismissed alert has no effect.

## Parameters

- `newTitleVariants`: An array of localized, displayable titles. The system selects the title that fits in the available display space.
- `newSubtitleVariants`: An array of localized, displayable subtitles. The system selects the title that fits in the available display space.

## See Also

- [var titleVariants: [String]](cpnavigationalert/titlevariants.md)
  An array of title strings.
- [var subtitleVariants: [String]](cpnavigationalert/subtitlevariants.md)
  An array of subtitle strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalert/updatetitlevariants(_:subtitlevariants:))*