# toggleVisuals(forSystemImageNamed:of:of:)

**Framework**: Touch Controller  
**Kind**: method

The toggle visuals for the specified system image name, size, and shape.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func toggleVisuals(forSystemImageNamed imageName: String, of size: CGSize, of shape: TCButtonVisualShape) -> TCControlVisuals
```

#### Return Value

The `TCControlVisuals` for the toggle button.

## Parameters

- `imageName`: The name of the system image to use for the toggle button.
- `size`: The size of the toggle button in points.
- `shape`: The shape of the toggle button.

## See Also

- [func toggleVisuals(for: TCControlLabel, of: CGSize, of: TCButtonVisualShape) -> TCControlVisuals](tccontrolsystemvisualsprovider/togglevisuals(for:of:of:).md)
  The toggle visuals for the specified label, size, and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolsystemvisualsprovider/togglevisuals(forsystemimagenamed:of:of:))*