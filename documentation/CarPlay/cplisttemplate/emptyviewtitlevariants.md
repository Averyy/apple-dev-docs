# emptyViewTitleVariants

**Framework**: CarPlay  
**Kind**: property

An array of title variants for the template’s empty view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var emptyViewTitleVariants: [String] { get set }
```

#### Discussion

When the list contains zero items, the template displays an empty view with a title and a subtitle. The template removes the empty view if you update the list and provide items.

Provide at least one nonzero length title variant. The view displays the first title variant that fits into the available screen space, so arrange your variants array from most- to least-preferred. Provide the strings as localized displayable content.

## See Also

- [var emptyViewSubtitleVariants: [String]](cplisttemplate/emptyviewsubtitlevariants.md)
  An array of subtitle variants for the template’s empty view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/emptyviewtitlevariants)*