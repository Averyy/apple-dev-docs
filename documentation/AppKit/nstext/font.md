# font

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The font of all the receiver’s text.

**Availability**:
- macOS

## Declaration

```swift
var font: NSFont? { get set }
```

```objc
@property (strong, nullable) NSFont * font;
```

#### Discussion

When the specified font doesn’t include a character, the text system uses an alternate font that contains the character. The substituted font may not have compatible metrics.

## See Also

### Changing the font
- [func changeFont(Any?)](./changefont%28_%29.md)
  This action method changes the font of the selection for a rich text object, or of all text for a plain text object.
- [func setFont(NSFont, range: NSRange)](./setfont%28_,range%29.md)
  Sets the font of characters within `aRange` to `aFont`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/font)*