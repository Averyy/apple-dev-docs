# titleAlignment

**Framework**: AppKit  
**Kind**: property

The alignment of the title.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var titleAlignment: NSTextAlignment { get set }
```

#### Discussion

The alignment can be one of the following values: `NSLeftTextAlignment`, `NSCenterTextAlignment`, or `NSRightTextAlignment`. The default alignment is `NSRightTextAlignment`.

## See Also

- [var attributedTitle: NSAttributedString](nsformcell/attributedtitle.md)
  The title of the cell as an attributed string.
- [var title: String](nsformcell/title.md)
  The cell’s title text.
- [var titleBaseWritingDirection: NSWritingDirection](nsformcell/titlebasewritingdirection.md)
  The default writing direction used to render the form cell’s title.
- [var titleFont: NSFont](nsformcell/titlefont.md)
  The font used to draw cell’s title.
- [var titleWidth: CGFloat](nsformcell/titlewidth.md)
  The width of the title field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/titlealignment)*