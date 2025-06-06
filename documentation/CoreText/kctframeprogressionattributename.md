# kCTFrameProgressionAttributeName

**Framework**: Core Text  
**Kind**: var

Specifies progression for a frame.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCTFrameProgressionAttributeName: CFString
```

#### Discussion

A [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) object containing a [`CTFrameProgression`](ctframeprogression.md) constant. The default is `kCTFrameProgressionTopToBottom`.

This value determines the line-stacking behavior for a frame and does not affect the appearance of the glyphs within that frame.

## See Also

- [enum CTFrameProgression](ctframeprogression.md)
  Constants that specify frame progression types.
- [let kCTFramePathFillRuleAttributeName: CFString](kctframepathfillruleattributename.md)
  The key used to specify the fill rule for a frame.
- [let kCTFramePathWidthAttributeName: CFString](kctframepathwidthattributename.md)
  The key used to specify the frame width.
- [let kCTFrameClippingPathsAttributeName: CFString](kctframeclippingpathsattributename.md)
  Specifies array of paths to clip frame.
- [let kCTFramePathClippingPathAttributeName: CFString](kctframepathclippingpathattributename.md)
  Specifies clipping path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctframeprogressionattributename)*