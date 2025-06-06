# font

**Framework**: AppKit  
**Kind**: property

The font of all the receiver’s text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var font: NSFont? { get set }
```

#### Discussion

When the specified font doesn’t include a character, the text system uses an alternate font that contains the character. The substituted font may not have compatible metrics.

## See Also

- [func changeFont(Any?)](nstext/changefont(_:).md)
  This action method changes the font of the selection for a rich text object, or of all text for a plain text object.
- [func setFont(NSFont, range: NSRange)](nstext/setfont(_:range:).md)
  Sets the font of characters within `aRange` to `aFont`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/font)*