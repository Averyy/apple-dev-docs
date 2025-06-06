# CTFrameProgression

**Framework**: Core Text  
**Kind**: enum

Constants that specify frame progression types.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CTFrameProgression
```

#### Overview

The lines of text within a frame may stack for either horizontal or vertical text. Values are enumerated for each stacking type supported by [`CTFrameProgression`](ctframeprogression.md). Frames with a progression type that specifies vertical text rotate lines 90 degrees counterclockwise during drawing.

## Topics

### Constants
- [CTFrameProgression.topToBottom](ctframeprogression/toptobottom.md)
  Lines stack top to bottom for horizontal text.
- [CTFrameProgression.rightToLeft](ctframeprogression/righttoleft.md)
  Lines stack right to left for vertical text.
- [CTFrameProgression.leftToRight](ctframeprogression/lefttoright.md)
  Lines stack left to right for vertical text.
### Initializers
- [init?(rawValue: UInt32)](ctframeprogression/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let kCTFrameProgressionAttributeName: CFString](kctframeprogressionattributename.md)
  Specifies progression for a frame.
- [let kCTFramePathFillRuleAttributeName: CFString](kctframepathfillruleattributename.md)
  The key used to specify the fill rule for a frame.
- [let kCTFramePathWidthAttributeName: CFString](kctframepathwidthattributename.md)
  The key used to specify the frame width.
- [let kCTFrameClippingPathsAttributeName: CFString](kctframeclippingpathsattributename.md)
  Specifies array of paths to clip frame.
- [let kCTFramePathClippingPathAttributeName: CFString](kctframepathclippingpathattributename.md)
  Specifies clipping path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctframeprogression)*