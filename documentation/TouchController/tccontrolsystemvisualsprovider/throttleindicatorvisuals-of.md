# throttleIndicatorVisuals(of:)

**Framework**: Touch Controller  
**Kind**: method

The throttle indicator visuals for the specified size.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func throttleIndicatorVisuals(of size: CGSize) -> TCControlVisuals
```

#### Return Value

The `TCControlVisuals` for the throttle indicator.

## Parameters

- `size`: The size of the throttle indicator in points.

## See Also

- [func directionPadVisuals(for: TCControlLabel, of: CGSize, of: TCDirectionPadVisualStyle, with: TCDirectionPadVisualDirection) -> TCControlVisuals](tccontrolsystemvisualsprovider/directionpadvisuals(for:of:of:with:).md)
  The direction pad visuals for the specified label, size, style, and direction.
- [func throttleBackgroundVisuals(of: CGSize) -> TCControlVisuals](tccontrolsystemvisualsprovider/throttlebackgroundvisuals(of:).md)
  The throttle background visuals for the specified size.
- [func thumbstickBackgroundVisuals(for: TCControlLabel, of: CGSize) -> TCControlVisuals](tccontrolsystemvisualsprovider/thumbstickbackgroundvisuals(for:of:).md)
  The thumbstick background visuals for the specified label and size.
- [func thumbstickStickVisuals(for: TCControlLabel, of: CGSize) -> TCControlVisuals](tccontrolsystemvisualsprovider/thumbstickstickvisuals(for:of:).md)
  The thumbstick stick visuals for the specified label and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolsystemvisualsprovider/throttleindicatorvisuals(of:))*