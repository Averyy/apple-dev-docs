# changeFont(_:)

**Framework**: AppKit  
**Kind**: method

This action method changes the font of the selection for a rich text object, or of all text for a plain text object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func changeFont(_ sender: Any?)
```

#### Discussion

If the receiver doesn’t use the Font panel, this method does nothing.

This method changes the font by sending a [`convert(_:)`](nsfontmanager/convert(_:).md) message to the shared NSFontManager and applying each NSFont returned to the appropriate text. See the [`NSFontManager`](nsfontmanager.md) class specification for more information on font conversion.

## See Also

- [var usesFontPanel: Bool](nstext/usesfontpanel.md)
  A Boolean that controls whether the receiver uses the Font panel and Font menu.
- [var font: NSFont?](nstext/font.md)
  The font of all the receiver’s text.
- [func setFont(NSFont, range: NSRange)](nstext/setfont(_:range:).md)
  Sets the font of characters within `aRange` to `aFont`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/changefont(_:))*