# hoverStyle

**Framework**: UIKit  
**Kind**: property

The hover style to apply to the sublayers of this layer when this layer is hovered (e.g., when the user looks at this layer). Defaults to the automatic style.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var hoverStyle: UIHoverStyle { get set }
```

#### Discussion

> **Note**: Not all [`UIHoverStyle`](uihoverstyle.md)s may be supported by [`UIHoverEffectLayer`](uihovereffectlayer.md). If the provided style is not supported, a fallback style will be selected instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihovereffectlayer/hoverstyle)*