# setSelectedFont(_:isMultiple:)

**Framework**: AppKit  
**Kind**: method

Records the specified font as the currently selected font and updates the Font panel.

**Availability**:
- macOS ?+

## Declaration

```swift
func setSelectedFont(_ fontObj: NSFont, isMultiple flag: Bool)
```

#### Discussion

An object that manipulates fonts should invoke this method whenever it becomes first responder and whenever its selection changes. It shouldn’t invoke this method in the process of handling a [`changeFont:`](https://developer.apple.com/documentation/objectivec/nsobject/1462311-changefont) message, as this causes the font manager to lose the information necessary to effect the change. After all fonts have been converted, the font manager itself records the new selected font.

## Parameters

- `fontObj`: The font to set as selected.
- `flag`: If  , the Font panel indicates that more than one font is contained in the selection; if  , it does not.

## See Also

- [var selectedFont: NSFont?](nsfontmanager/selectedfont.md)
  The currently selected font object.
- [var isMultiple: Bool](nsfontmanager/ismultiple.md)
  A Boolean value that indicates whether the currently selected font has multiple fonts.
- [func sendAction() -> Bool](nsfontmanager/sendaction.md)
  A Boolean value that indicates whether a responder handled the font manager’s action message.
- [func localizedName(forFamily: String, face: String?) -> String](nsfontmanager/localizedname(forfamily:face:).md)
  Returns a localized string with the name of the specified font family and face, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/setselectedfont(_:ismultiple:))*