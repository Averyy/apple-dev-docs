# titleBaseWritingDirection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The default writing direction used to render the form cell’s title.

**Availability**:
- macOS

## Declaration

```swift
var titleBaseWritingDirection: NSWritingDirection { get set }
```

```objc
@property NSWritingDirection titleBaseWritingDirection;
```

#### Discussion

Can be one of the following constants: `NSWritingDirectionNatural`, `NSWritingDirectionLeftToRight`, or `NSWritingDirectionRightToLeft`.

## See Also

### Accessing a Cell’s Title
- [var attributedTitle: NSAttributedString](./attributedtitle.md)
  The title of the cell as an attributed string.
- [var title: String](./title.md)
  The cell’s title text.
- [var titleAlignment: NSTextAlignment](./titlealignment.md)
  The alignment of the title.
- [var titleFont: NSFont](./titlefont.md)
  The font used to draw cell’s title.
- [var titleWidth: CGFloat](./titlewidth.md)
  The width of the title field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/titlebasewritingdirection)*