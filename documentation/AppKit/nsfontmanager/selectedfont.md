# selectedFont

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The currently selected font object.

**Availability**:
- macOS

## Declaration

```swift
var selectedFont: NSFont? { get }
```

```objc
@property (strong, readonly, nullable) NSFont * selectedFont;
```

#### Discussion

The value of this property is the last font recorded with a [`setSelectedFont(_:isMultiple:)`](./setselectedfont%28_,ismultiple%29.md) message.

While fonts are being converted in response to a [`convert(_:)`](./convert%28_%29.md) message, you can determine the font selected in the Font panel like this:

```objc
NSFontManager *fontManager = [NSFontManager sharedFontManager];
panelFont = [fontManager convertFont:[fontManager.selectedFont]];
```

## See Also

### Setting and Examining the Selected Font
- [func setSelectedFont(NSFont, isMultiple: Bool)](./setselectedfont%28_,ismultiple%29.md)
  Records the specified font as the currently selected font and updates the Font panel.
- [var isMultiple: Bool](./ismultiple.md)
  A Boolean value that indicates whether the currently selected font has multiple fonts.
- [func sendAction() -> Bool](./sendaction%28%29.md)
  A Boolean value that indicates whether a responder handled the font manager’s action message.
- [func localizedName(forFamily: String, face: String?) -> String](./localizedname%28forfamily,face%29.md)
  Returns a localized string with the name of the specified font family and face, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/selectedfont)*