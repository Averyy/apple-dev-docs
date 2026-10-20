# setKeyEquivalentFont(_:size:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets by name and size of the font used to draw the key equivalent.

**Availability**:
- macOS 10.0+ - Deprecated in 10.15

> **Deprecated**: The keyEquivalentFont property is no longer used. Setting it has no effect.

## Declaration

```swift
func setKeyEquivalentFont(_ fontName: String, size fontSize: CGFloat)
```

```objc
- (void) setKeyEquivalentFont:(NSString *) fontName size:(CGFloat) fontSize;
```

#### Discussion

This method redisplays the button if necessary. It does nothing if the button doesn’t have a key equivalent associated with it. The default font is the same as that used to draw the title.

## Parameters

- `fontName`: The name of the font to use to draw the key equivalent.
- `fontSize`: The font size to use to draw the key equivalent.

## See Also

### Related Documentation
- [var font: NSFont?](../nscell/font.md)
  The font that the cell uses to display text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/setkeyequivalentfont(_:size:))*