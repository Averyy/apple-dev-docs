# scaledValue(for:)

**Framework**: UIKit  
**Kind**: method

Scales an arbitrary layout value based on the current Dynamic Type settings.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func scaledValue(for value: CGFloat) -> CGFloat
```

#### Return Value

A layout height that is scaled appropriately to accommodate the text that you want to display.

#### Discussion

Use this method to scale the height of visual elements containing text. For example, if you define a button with text that can scale based on Dynamic Type, you would use this method to obtain an appropriately scaled height for your button’s background content.

## Parameters

- `value`: The height value that you want to scale. Specify the height of the object that contains the text (at the standard Dynamic Type size) that you want to display.

## See Also

- [func scaledValue(for: CGFloat, compatibleWith: UITraitCollection?) -> CGFloat](uifontmetrics/scaledvalue(for:compatiblewith:).md)
  Scales an arbitrary layout value based on the current Dynamic Type settings and the specified traits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontmetrics/scaledvalue(for:))*