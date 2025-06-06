# familyName

**Framework**: AppKit  
**Kind**: property

The family name of the font—for example, “Times” or “Helvetica.”

**Availability**:
- macOS ?+

## Declaration

```swift
var familyName: String? { get }
```

#### Discussion

This name is the one that `NSFontManager` uses and may differ slightly from the AFM name.

The value in this property is intended for an application’s internal usage and not for display. To get a name that you can display to the user, use the [`displayName`](nsfont/displayname.md) property instead.

## See Also

- [var displayName: String?](nsfont/displayname.md)
  The name of the font, including family and face names, to use when displaying the font information to the user.
- [var fontName: String](nsfont/fontname.md)
  The full name of the font, as used in PostScript language code—for example, “Times-Roman” or “Helvetica-Oblique.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/familyname)*