# isMultiple

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the currently selected font has multiple fonts.

**Availability**:
- macOS

## Declaration

```swift
var isMultiple: Bool { get }
```

```objc
@property (readonly, getter=isMultiple) BOOL multiple;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the last font selection recorded has multiple fonts; if the last font selection recorded is a single font, the value is [`false`](../../Swift/false.md).

## See Also

### Setting and Examining the Selected Font
- [func setSelectedFont(NSFont, isMultiple: Bool)](./setselectedfont%28_,ismultiple%29.md)
  Records the specified font as the currently selected font and updates the Font panel.
- [var selectedFont: NSFont?](./selectedfont.md)
  The currently selected font object.
- [func sendAction() -> Bool](./sendaction%28%29.md)
  A Boolean value that indicates whether a responder handled the font manager’s action message.
- [func localizedName(forFamily: String, face: String?) -> String](./localizedname%28forfamily,face%29.md)
  Returns a localized string with the name of the specified font family and face, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/ismultiple)*