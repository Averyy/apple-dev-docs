# isMultiple

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the currently selected font has multiple fonts.

**Availability**:
- macOS ?+

## Declaration

```swift
var isMultiple: Bool { get }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the last font selection recorded has multiple fonts; if the last font selection recorded is a single font, the value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func setSelectedFont(NSFont, isMultiple: Bool)](nsfontmanager/setselectedfont(_:ismultiple:).md)
  Records the specified font as the currently selected font and updates the Font panel.
- [var selectedFont: NSFont?](nsfontmanager/selectedfont.md)
  The currently selected font object.
- [func sendAction() -> Bool](nsfontmanager/sendaction.md)
  A Boolean value that indicates whether a responder handled the font manager’s action message.
- [func localizedName(forFamily: String, face: String?) -> String](nsfontmanager/localizedname(forfamily:face:).md)
  Returns a localized string with the name of the specified font family and face, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/ismultiple)*