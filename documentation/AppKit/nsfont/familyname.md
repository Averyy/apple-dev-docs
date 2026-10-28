# familyName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The family name of the font—for example, “Times” or “Helvetica.”

**Availability**:
- macOS

## Declaration

```swift
var familyName: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * familyName;
```

## Discussion

This name is the one that `NSFontManager` uses and may differ slightly from the AFM name.

The value in this property is intended for an application’s internal usage and not for display. To get a name that you can display to the user, use the [`displayName`](./displayname.md) property instead.

## See Also

### Getting Font Names
- [var displayName: String?](./displayname.md)
  The name of the font, including family and face names, to use when displaying the font information to the user.
- [var fontName: String](./fontname.md)
  The full name of the font, as used in PostScript language code—for example, “Times-Roman” or “Helvetica-Oblique.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/familyname)*