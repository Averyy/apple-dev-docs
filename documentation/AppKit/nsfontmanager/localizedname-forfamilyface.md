# localizedName(forFamily:face:)

**Framework**: AppKit  
**Kind**: method

Returns a localized string with the name of the specified font family and face, if one exists.

**Availability**:
- macOS ?+

## Declaration

```swift
func localizedName(forFamily family: String, face faceKey: String?) -> String
```

#### Return Value

A localized string with the name of the specified font family and face, or, if `face` is `nil`, the font family only.

#### Discussion

The user’s locale is determined from the user’s `NSLanguages` default setting. The method also loads the localized strings for the font, if they aren’t already loaded.

## Parameters

- `family`: The font family, for example,  .
- `faceKey`: The font face, for example,  .

## See Also

- [func setSelectedFont(NSFont, isMultiple: Bool)](nsfontmanager/setselectedfont(_:ismultiple:).md)
  Records the specified font as the currently selected font and updates the Font panel.
- [var selectedFont: NSFont?](nsfontmanager/selectedfont.md)
  The currently selected font object.
- [var isMultiple: Bool](nsfontmanager/ismultiple.md)
  A Boolean value that indicates whether the currently selected font has multiple fonts.
- [func sendAction() -> Bool](nsfontmanager/sendaction.md)
  A Boolean value that indicates whether a responder handled the font manager’s action message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/localizedname(forfamily:face:))*