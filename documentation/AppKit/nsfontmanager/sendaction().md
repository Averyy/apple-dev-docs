# sendAction()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

A Boolean value that indicates whether a responder handled the font manager’s action message.

**Availability**:
- macOS

## Declaration

```swift
func sendAction() -> Bool
```

```objc
- (BOOL) sendAction;
```

## Discussion

By default, the font manager’s action message is [`changeFont:`](../../ObjectiveC/nsobject-swift.class/changefont_.md). The value of this property is [`true`](../../Swift/true.md) if some responder object handled the [`changeFont:`](../../ObjectiveC/nsobject-swift.class/changefont_.md) message or [`false`](../../Swift/false.md) if the message went unheard.

## See Also

### Related Documentation
- [var action: Selector](./action.md)
  The action sent to the first responder when the user selects a new font from the Font panel or chooses a command from the Font menu.
### Setting and Examining the Selected Font
- [func setSelectedFont(NSFont, isMultiple: Bool)](./setselectedfont%28_,ismultiple%29.md)
  Records the specified font as the currently selected font and updates the Font panel.
- [var selectedFont: NSFont?](./selectedfont.md)
  The currently selected font object.
- [var isMultiple: Bool](./ismultiple.md)
  A Boolean value that indicates whether the currently selected font has multiple fonts.
- [func localizedName(forFamily: String, face: String?) -> String](./localizedname%28forfamily,face%29.md)
  Returns a localized string with the name of the specified font family and face, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/sendaction())*