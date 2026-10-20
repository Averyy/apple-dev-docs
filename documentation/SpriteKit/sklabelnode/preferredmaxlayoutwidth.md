# preferredMaxLayoutWidth

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The width, in screen points, after which line-break mode should be applied.

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
var preferredMaxLayoutWidth: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat preferredMaxLayoutWidth;
```

#### Discussion

The default value is 0, which means that line break mode will not be applied.

## See Also

### Defining a Label’s Line-Breaking Behavior
- [var lineBreakMode: NSLineBreakMode](./linebreakmode.md)
  Determines the line-break mode for multiple lines.
- [var numberOfLines: Int](./numberoflines.md)
  Determines the number of lines to draw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sklabelnode/preferredmaxlayoutwidth)*