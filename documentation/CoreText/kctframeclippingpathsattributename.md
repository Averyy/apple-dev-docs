# kCTFrameClippingPathsAttributeName

**Framework**: Core Text  
**Kind**: var

Specifies array of paths to clip frame.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCTFrameClippingPathsAttributeName: CFString
```

#### Discussion

The value must be a `CFArrayRef` containing `CFDictionaryRef`s. Each dictionary should have a `kCTFramePathClippingPathAttributeName` key-value pair, and can have a `kCTFramePathFillRuleAttributeName` key-value pair and `kCTFramePathFillRuleAttributeName` key-value pair as optional parameters.

## See Also

- [enum CTFrameProgression](ctframeprogression.md)
  Constants that specify frame progression types.
- [let kCTFrameProgressionAttributeName: CFString](kctframeprogressionattributename.md)
  Specifies progression for a frame.
- [let kCTFramePathFillRuleAttributeName: CFString](kctframepathfillruleattributename.md)
  The key used to specify the fill rule for a frame.
- [let kCTFramePathWidthAttributeName: CFString](kctframepathwidthattributename.md)
  The key used to specify the frame width.
- [let kCTFramePathClippingPathAttributeName: CFString](kctframepathclippingpathattributename.md)
  Specifies clipping path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctframeclippingpathsattributename)*