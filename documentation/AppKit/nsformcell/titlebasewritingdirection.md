# titleBaseWritingDirection

**Framework**: AppKit  
**Kind**: property

The default writing direction used to render the form cell’s title.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var titleBaseWritingDirection: NSWritingDirection { get set }
```

#### Discussion

Can be one of the following constants: `NSWritingDirectionNatural`, `NSWritingDirectionLeftToRight`, or `NSWritingDirectionRightToLeft`.

## See Also

- [var attributedTitle: NSAttributedString](nsformcell/attributedtitle.md)
  The title of the cell as an attributed string.
- [var title: String](nsformcell/title.md)
  The cell’s title text.
- [var titleAlignment: NSTextAlignment](nsformcell/titlealignment.md)
  The alignment of the title.
- [var titleFont: NSFont](nsformcell/titlefont.md)
  The font used to draw cell’s title.
- [var titleWidth: CGFloat](nsformcell/titlewidth.md)
  The width of the title field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/titlebasewritingdirection)*