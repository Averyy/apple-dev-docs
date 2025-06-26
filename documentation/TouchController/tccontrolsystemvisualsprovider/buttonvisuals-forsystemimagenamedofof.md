# buttonVisuals(forSystemImageNamed:of:of:)

**Framework**: Touch Controller  
**Kind**: method

The button visuals for the specified system image name, size, and shape.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func buttonVisuals(forSystemImageNamed imageName: String, of size: CGSize, of shape: TCButtonVisualShape) -> TCControlVisuals
```

#### Return Value

The `TCControlVisuals` for the button.

## Parameters

- `imageName`: The name of the system image to use for the button.
- `size`: The size of the button in points.
- `shape`: The shape of the button.

## See Also

- [func buttonVisuals(for: TCControlLabel, of: CGSize, of: TCButtonVisualShape) -> TCControlVisuals](tccontrolsystemvisualsprovider/buttonvisuals(for:of:of:).md)
  The button visuals for the specified label, size, and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolsystemvisualsprovider/buttonvisuals(forsystemimagenamed:of:of:))*