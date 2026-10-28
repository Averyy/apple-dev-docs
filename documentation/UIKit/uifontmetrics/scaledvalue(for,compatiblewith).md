# scaledValue(for:compatibleWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Scales an arbitrary layout value based on the current Dynamic Type settings and the specified traits.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func scaledValue(for value: CGFloat, compatibleWith traitCollection: UITraitCollection?) -> CGFloat
```

```objc
- (CGFloat) scaledValueForValue:(CGFloat) value compatibleWithTraitCollection:(UITraitCollection *) traitCollection;
```

## Return Value

A layout height that is scaled appropriately to accommodate the text that you want to display.

## Discussion

Use this method to scale the height of visual elements containing text. For example, if you define a button with text that can scale based on Dynamic Type, you would use this method to obtain an appropriately scaled height for your button’s background content.

## Parameters

- `value`: The height value that you want to scale. Specify the height of the object that contains the text (at the standard Dynamic Type size) that you want to display.
- `traitCollection`: The trait collection to use when determining compatibility. The returned value is appropriate for use in an interface that adopts the specified traits.

## See Also

### Scaling Layout Values
- [func scaledValue(for: CGFloat) -> CGFloat](./scaledvalue%28for%29.md)
  Scales an arbitrary layout value based on the current Dynamic Type settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontmetrics/scaledvalue(for:compatiblewith:))*