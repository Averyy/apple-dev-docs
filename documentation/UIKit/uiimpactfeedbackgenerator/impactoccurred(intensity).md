# impactOccurred(intensity:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Triggers impact feedback with a specific intensity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func impactOccurred(intensity: CGFloat)
```

```objc
- (void) impactOccurredWithIntensity:(CGFloat) intensity;
```

## Parameters

- `intensity`: A [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) value between `0.0` and `1.0`.

## See Also

### Reporting impacts
- [func impactOccurred()](./impactoccurred%28%29.md)
  Triggers impact feedback.
- [func impactOccurred(at: CGPoint)](./impactoccurred%28at%29.md)
  Triggers impact feedback at the specified location.
- [func impactOccurred(intensity: CGFloat, at: CGPoint)](./impactoccurred%28intensity,at%29.md)
  Triggers impact feedback with a specific intensity at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimpactfeedbackgenerator/impactoccurred(intensity:))*