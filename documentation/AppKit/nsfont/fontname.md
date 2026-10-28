# fontName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The full name of the font, as used in PostScript language code—for example, “Times-Roman” or “Helvetica-Oblique.”

**Availability**:
- macOS

## Declaration

```swift
var fontName: String { get }
```

```objc
@property (copy, readonly) NSString * fontName;
```

## Discussion

The value in this property is intended for an application’s internal usage and not for display. To get a name that you can display to the user, use the [`displayName`](./displayname.md) property instead.

## See Also

### Getting Font Names
- [var displayName: String?](./displayname.md)
  The name of the font, including family and face names, to use when displaying the font information to the user.
- [var familyName: String?](./familyname.md)
  The family name of the font—for example, “Times” or “Helvetica.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/fontname)*