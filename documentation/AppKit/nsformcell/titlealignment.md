# titleAlignment

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The alignment of the title.

**Availability**:
- macOS

## Declaration

```swift
var titleAlignment: NSTextAlignment { get set }
```

```objc
@property NSTextAlignment titleAlignment;
```

#### Discussion

The alignment can be one of the following values: `NSLeftTextAlignment`, `NSCenterTextAlignment`, or `NSRightTextAlignment`. The default alignment is `NSRightTextAlignment`.

## See Also

### Accessing a Cell’s Title
- [var attributedTitle: NSAttributedString](./attributedtitle.md)
  The title of the cell as an attributed string.
- [var title: String](./title.md)
  The cell’s title text.
- [var titleBaseWritingDirection: NSWritingDirection](./titlebasewritingdirection.md)
  The default writing direction used to render the form cell’s title.
- [var titleFont: NSFont](./titlefont.md)
  The font used to draw cell’s title.
- [var titleWidth: CGFloat](./titlewidth.md)
  The width of the title field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/titlealignment)*