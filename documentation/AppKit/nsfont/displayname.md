# displayName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name of the font, including family and face names, to use when displaying the font information to the user.

**Availability**:
- macOS

## Declaration

```swift
var displayName: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * displayName;
```

## Discussion

The font’s display name is typically localized for the user’s language.

## See Also

### Getting Font Names
- [var familyName: String?](./familyname.md)
  The family name of the font—for example, “Times” or “Helvetica.”
- [var fontName: String](./fontname.md)
  The full name of the font, as used in PostScript language code—for example, “Times-Roman” or “Helvetica-Oblique.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/displayname)*