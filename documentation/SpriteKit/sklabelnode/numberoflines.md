# numberOfLines

**Framework**: SpriteKit  
**Kind**: property

Determines the number of lines to draw.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@MainActor
var numberOfLines: Int { get set }
```

#### Discussion

The default value is 1 (a single line). A value of 0 in interpreted as an unlimited number of lines. If the height of the text reaches the number of lines, the text will be truncated using the line break mode.

## See Also

- [var preferredMaxLayoutWidth: CGFloat](sklabelnode/preferredmaxlayoutwidth.md)
  The width, in screen points, after which line-break mode should be applied.
- [var lineBreakMode: NSLineBreakMode](sklabelnode/linebreakmode.md)
  Determines the line-break mode for multiple lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sklabelnode/numberoflines)*