# titleWidth

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The width of the title field.

**Availability**:
- macOS

## Declaration

```swift
var titleWidth: CGFloat { get set }
```

```objc
@property CGFloat titleWidth;
```

#### Discussion

The width of the title field, measured in points in the user coordinate space. You usually do not need to set this property. AppKit automatically sets the title width whenever the title changes. If the automatic width doesn’t suit your needs, though, you can use this property to set the width explicitly.

After you have set the width this way, AppKit stops setting the width automatically, so you must set this property every time the title changes. If you want AppKit to resume automatic width assignments, set this property to a negative value.

## See Also

### Accessing a Cell’s Title
- [var attributedTitle: NSAttributedString](./attributedtitle.md)
  The title of the cell as an attributed string.
- [var title: String](./title.md)
  The cell’s title text.
- [var titleAlignment: NSTextAlignment](./titlealignment.md)
  The alignment of the title.
- [var titleBaseWritingDirection: NSWritingDirection](./titlebasewritingdirection.md)
  The default writing direction used to render the form cell’s title.
- [var titleFont: NSFont](./titlefont.md)
  The font used to draw cell’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/titlewidth)*