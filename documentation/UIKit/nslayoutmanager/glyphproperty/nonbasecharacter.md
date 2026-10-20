# nonBaseCharacter

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A glyph that combines several properties.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static var nonBaseCharacter: NSLayoutManager.GlyphProperty { get }
```

```c
NSGlyphPropertyNonBaseCharacter
```

#### Discussion

A glyph of this type typically represents characters in the Unicode Mn class.

## See Also

### Glyph properties
- [static var null: NSLayoutManager.GlyphProperty](./null.md)
  The null glyph, which the layout manager ignores.
- [static var controlCharacter: NSLayoutManager.GlyphProperty](./controlcharacter.md)
  A glyph representing a control character.
- [static var elastic: NSLayoutManager.GlyphProperty](./elastic.md)
  A glyph with a changeable width, such as a white space character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/glyphproperty/nonbasecharacter)*