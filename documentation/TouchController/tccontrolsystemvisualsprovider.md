# TCControlSystemVisualsProvider

**Framework**: Touch Controller  
**Kind**: class

Provides system-defined visuals for touch controls.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class TCControlSystemVisualsProvider
```

## Topics

### Creating a visuals provider
- [init(touchController: TCTouchController)](tccontrolsystemvisualsprovider/init(touchcontroller:).md)
  Creates a new visuals provider with the specified touch controller.
### Getting the button visuals
- [func buttonVisuals(for: TCControlLabel, of: CGSize, of: TCButtonVisualShape) -> TCControlVisuals](tccontrolsystemvisualsprovider/buttonvisuals(for:of:of:).md)
  The button visuals for the specified label, size, and shape.
- [func buttonVisuals(forSystemImageNamed: String, of: CGSize, of: TCButtonVisualShape) -> TCControlVisuals](tccontrolsystemvisualsprovider/buttonvisuals(forsystemimagenamed:of:of:).md)
  The button visuals for the specified system image name, size, and shape.
### Accessing direction pad, throttle, and thumbstick visuals
- [func directionPadVisuals(for: TCControlLabel, of: CGSize, of: TCDirectionPadVisualStyle, with: TCDirectionPadVisualDirection) -> TCControlVisuals](tccontrolsystemvisualsprovider/directionpadvisuals(for:of:of:with:).md)
  The direction pad visuals for the specified label, size, style, and direction.
- [func throttleBackgroundVisuals(of: CGSize) -> TCControlVisuals](tccontrolsystemvisualsprovider/throttlebackgroundvisuals(of:).md)
  The throttle background visuals for the specified size.
- [func throttleIndicatorVisuals(of: CGSize) -> TCControlVisuals](tccontrolsystemvisualsprovider/throttleindicatorvisuals(of:).md)
  The throttle indicator visuals for the specified size.
- [func thumbstickBackgroundVisuals(for: TCControlLabel, of: CGSize) -> TCControlVisuals](tccontrolsystemvisualsprovider/thumbstickbackgroundvisuals(for:of:).md)
  The thumbstick background visuals for the specified label and size.
- [func thumbstickStickVisuals(for: TCControlLabel, of: CGSize) -> TCControlVisuals](tccontrolsystemvisualsprovider/thumbstickstickvisuals(for:of:).md)
  The thumbstick stick visuals for the specified label and size.
### Toggling the visuals
- [func toggleVisuals(for: TCControlLabel, of: CGSize, of: TCButtonVisualShape) -> TCControlVisuals](tccontrolsystemvisualsprovider/togglevisuals(for:of:of:).md)
  The toggle visuals for the specified label, size, and shape.
- [func toggleVisuals(forSystemImageNamed: String, of: CGSize, of: TCButtonVisualShape) -> TCControlVisuals](tccontrolsystemvisualsprovider/togglevisuals(forsystemimagenamed:of:of:).md)
  The toggle visuals for the specified system image name, size, and shape.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [enum TCButtonVisualShape](tcbuttonvisualshape.md)
  Defines the visual shape of a button.
- [enum TCDirectionPadVisualStyle](tcdirectionpadvisualstyle.md)
  Defines the visual style of a direction pad.
- [enum TCDirectionPadVisualDirection](tcdirectionpadvisualdirection.md)
  Defines the direction of a direction pad visual.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolsystemvisualsprovider)*