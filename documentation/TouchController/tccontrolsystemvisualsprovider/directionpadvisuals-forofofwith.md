# directionPadVisuals(for:of:of:with:)

**Framework**: Touch Controller  
**Kind**: method

The direction pad visuals for the specified label, size, style, and direction.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func directionPadVisuals(for label: TCControlLabel, of size: CGSize, of style: TCDirectionPadVisualStyle, with direction: TCDirectionPadVisualDirection) -> TCControlVisuals
```

#### Return Value

The `TCControlVisuals` for the direction pad.

## Parameters

- `label`: The label for the direction pad.
- `size`: The size of the direction pad in points.
- `style`: The style of the direction pad.
- `direction`: The direction of the direction pad visual.

## See Also

- [func throttleBackgroundVisuals(of: CGSize) -> TCControlVisuals](tccontrolsystemvisualsprovider/throttlebackgroundvisuals(of:).md)
  The throttle background visuals for the specified size.
- [func throttleIndicatorVisuals(of: CGSize) -> TCControlVisuals](tccontrolsystemvisualsprovider/throttleindicatorvisuals(of:).md)
  The throttle indicator visuals for the specified size.
- [func thumbstickBackgroundVisuals(for: TCControlLabel, of: CGSize) -> TCControlVisuals](tccontrolsystemvisualsprovider/thumbstickbackgroundvisuals(for:of:).md)
  The thumbstick background visuals for the specified label and size.
- [func thumbstickStickVisuals(for: TCControlLabel, of: CGSize) -> TCControlVisuals](tccontrolsystemvisualsprovider/thumbstickstickvisuals(for:of:).md)
  The thumbstick stick visuals for the specified label and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolsystemvisualsprovider/directionpadvisuals(for:of:of:with:))*