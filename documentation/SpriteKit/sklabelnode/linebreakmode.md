# lineBreakMode

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

Determines the line-break mode for multiple lines.

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
var lineBreakMode: NSLineBreakMode { get set }
```

```objc
@property (nonatomic) NSLineBreakMode lineBreakMode;
```

#### Discussion

The default value is NSLineBreakByTruncatingTail.

## See Also

### Defining a Label’s Line-Breaking Behavior
- [var preferredMaxLayoutWidth: CGFloat](./preferredmaxlayoutwidth.md)
  The width, in screen points, after which line-break mode should be applied.
- [var numberOfLines: Int](./numberoflines.md)
  Determines the number of lines to draw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sklabelnode/linebreakmode)*