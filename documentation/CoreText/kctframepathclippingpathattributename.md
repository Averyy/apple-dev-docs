# kCTFramePathClippingPathAttributeName

**Framework**: Core Text  
**Kind**: var

Specifies clipping path.

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
let kCTFramePathClippingPathAttributeName: CFString
```

#### Discussion

Specifies clipping path.  This attribute is valid only in a dictionary contained in an array specified by `kCTFrameClippingPathsAttributeName`.

The value must be a `CGPathRef` specifying a clipping path. See [`kCTFrameClippingPathsAttributeName`](kctframeclippingpathsattributename.md).

## See Also

- [enum CTFrameProgression](ctframeprogression.md)
  Constants that specify frame progression types.
- [let kCTFrameProgressionAttributeName: CFString](kctframeprogressionattributename.md)
  Specifies progression for a frame.
- [let kCTFramePathFillRuleAttributeName: CFString](kctframepathfillruleattributename.md)
  The key used to specify the fill rule for a frame.
- [let kCTFramePathWidthAttributeName: CFString](kctframepathwidthattributename.md)
  The key used to specify the frame width.
- [let kCTFrameClippingPathsAttributeName: CFString](kctframeclippingpathsattributename.md)
  Specifies array of paths to clip frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctframepathclippingpathattributename)*