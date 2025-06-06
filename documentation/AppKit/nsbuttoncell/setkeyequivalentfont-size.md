# setKeyEquivalentFont(_:size:)

**Framework**: AppKit  
**Kind**: method

Sets by name and size of the font used to draw the key equivalent.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func setKeyEquivalentFont(_ fontName: String, size fontSize: CGFloat)
```

#### Discussion

This method redisplays the button if necessary. It does nothing if the button doesn’t have a key equivalent associated with it. The default font is the same as that used to draw the title.

## Parameters

- `fontName`: The name of the font to use to draw the key equivalent.
- `fontSize`: The font size to use to draw the key equivalent.

## See Also

- [var font: NSFont?](nscell/font.md)
  The font that the cell uses to display text.
- [var keyEquivalent: String](nsbuttoncell/keyequivalent.md)
  The button’s key-equivalent character.
- [var keyEquivalentFont: NSFont?](nsbuttoncell/keyequivalentfont.md)
  The font used to draw the button’s key equivalent.
- [var keyEquivalentModifierMask: NSEvent.ModifierFlags](nsbuttoncell/keyequivalentmodifiermask.md)
  The mask that identifies the modifier keys for the button’s key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/setkeyequivalentfont(_:size:))*