# selectedFont

**Framework**: AppKit  
**Kind**: property

The currently selected font object.

**Availability**:
- macOS ?+

## Declaration

```swift
var selectedFont: NSFont? { get }
```

#### Discussion

The value of this property is the last font recorded with a [`setSelectedFont(_:isMultiple:)`](nsfontmanager/setselectedfont(_:ismultiple:).md) message.

While fonts are being converted in response to a [`convert(_:)`](nsfontmanager/convert(_:).md) message, you can determine the font selected in the Font panel like this:

```objc
NSFontManager *fontManager = [NSFontManager sharedFontManager];
panelFont = [fontManager convertFont:[fontManager.selectedFont]];
```

## See Also

- [func setSelectedFont(NSFont, isMultiple: Bool)](nsfontmanager/setselectedfont(_:ismultiple:).md)
  Records the specified font as the currently selected font and updates the Font panel.
- [var isMultiple: Bool](nsfontmanager/ismultiple.md)
  A Boolean value that indicates whether the currently selected font has multiple fonts.
- [func sendAction() -> Bool](nsfontmanager/sendaction.md)
  A Boolean value that indicates whether a responder handled the font manager’s action message.
- [func localizedName(forFamily: String, face: String?) -> String](nsfontmanager/localizedname(forfamily:face:).md)
  Returns a localized string with the name of the specified font family and face, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/selectedfont)*