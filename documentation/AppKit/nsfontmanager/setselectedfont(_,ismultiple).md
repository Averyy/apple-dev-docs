# setSelectedFont(_:isMultiple:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Records the specified font as the currently selected font and updates the Font panel.

**Availability**:
- macOS

## Declaration

```swift
func setSelectedFont(_ fontObj: NSFont, isMultiple flag: Bool)
```

```objc
- (void) setSelectedFont:(NSFont *) fontObj isMultiple:(BOOL) flag;
```

#### Discussion

An object that manipulates fonts should invoke this method whenever it becomes first responder and whenever its selection changes. It shouldn’t invoke this method in the process of handling a [`changeFont:`](../../ObjectiveC/nsobject-swift.class/changefont_.md) message, as this causes the font manager to lose the information necessary to effect the change. After all fonts have been converted, the font manager itself records the new selected font.

## Parameters

- `fontObj`: The font to set as selected.
- `flag`: If [`true`](../../Swift/true.md), the Font panel indicates that more than one font is contained in the selection; if [`false`](../../Swift/false.md), it does not.

## See Also

### Setting and Examining the Selected Font
- [var selectedFont: NSFont?](./selectedfont.md)
  The currently selected font object.
- [var isMultiple: Bool](./ismultiple.md)
  A Boolean value that indicates whether the currently selected font has multiple fonts.
- [func sendAction() -> Bool](./sendaction%28%29.md)
  A Boolean value that indicates whether a responder handled the font manager’s action message.
- [func localizedName(forFamily: String, face: String?) -> String](./localizedname%28forfamily,face%29.md)
  Returns a localized string with the name of the specified font family and face, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/setselectedfont(_:ismultiple:))*