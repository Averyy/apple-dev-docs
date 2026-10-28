# descender

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The bottom y-coordinate, offset from the baseline, of the font’s longest descender.

**Availability**:
- macOS

## Declaration

```swift
var descender: CGFloat { get }
```

```objc
@property (readonly) CGFloat descender;
```

## Discussion

For example, if the longest descender extends 2 points below the baseline, the value in this property is `–2`.

## See Also

### Getting the Font Metrics
- [var ascender: CGFloat](./ascender.md)
  The top y-coordinate, offset from the baseline, of the font’s longest ascender.
- [var capHeight: CGFloat](./capheight.md)
  The cap height of the font.
- [var leading: CGFloat](./leading.md)
  The leading value of the font.
- [var xHeight: CGFloat](./xheight.md)
  The x-height of the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/descender)*