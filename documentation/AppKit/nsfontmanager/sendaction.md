# sendAction()

**Framework**: AppKit  
**Kind**: method

A Boolean value that indicates whether a responder handled the font manager’s action message.

**Availability**:
- macOS ?+

## Declaration

```swift
func sendAction() -> Bool
```

#### Discussion

By default, the font manager’s action message is [`changeFont:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/changeFont:). The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if some responder object handled the [`changeFont:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/changeFont:) message or [`false`](https://developer.apple.com/documentation/Swift/false) if the message went unheard.

## See Also

- [var action: Selector](nsfontmanager/action.md)
  The action sent to the first responder when the user selects a new font from the Font panel or chooses a command from the Font menu.
- [func setSelectedFont(NSFont, isMultiple: Bool)](nsfontmanager/setselectedfont(_:ismultiple:).md)
  Records the specified font as the currently selected font and updates the Font panel.
- [var selectedFont: NSFont?](nsfontmanager/selectedfont.md)
  The currently selected font object.
- [var isMultiple: Bool](nsfontmanager/ismultiple.md)
  A Boolean value that indicates whether the currently selected font has multiple fonts.
- [func localizedName(forFamily: String, face: String?) -> String](nsfontmanager/localizedname(forfamily:face:).md)
  Returns a localized string with the name of the specified font family and face, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/sendaction())*