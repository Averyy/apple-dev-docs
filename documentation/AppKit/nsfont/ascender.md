# ascender

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The top y-coordinate, offset from the baseline, of the font’s longest ascender.

**Availability**:
- macOS

## Declaration

```swift
var ascender: CGFloat { get }
```

```objc
@property (readonly) CGFloat ascender;
```

#### Discussion

The value of this property is the distance of the longest ascender’s top y-coordinate from the baseline, measured in points.

## See Also

### Getting the Font Metrics
- [var descender: CGFloat](./descender.md)
  The bottom y-coordinate, offset from the baseline, of the font’s longest descender.
- [var capHeight: CGFloat](./capheight.md)
  The cap height of the font.
- [var leading: CGFloat](./leading.md)
  The leading value of the font.
- [var xHeight: CGFloat](./xheight.md)
  The x-height of the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/ascender)*