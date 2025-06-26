# drawableSizeWillChange(_:scaleFactor:)

**Framework**: Touch Controller  
**Kind**: method

Called when the drawable size changes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func drawableSizeWillChange(_ size: CGSize, scaleFactor: CGFloat)
```

## Parameters

- `size`: The new size of the drawable in points.
- `scaleFactor`: The new scale factor of the screen.

## See Also

- [func render(with: any MTLRenderCommandEncoder)](tctouchcontroller/render(with:).md)
  Renders the touch controls using the provided Metal render command encoder.
- [func setupDefaultLayout(for: [TCControlLabel])](tctouchcontroller/setupdefaultlayout(for:).md)
  Sets up a default layout for the provided control labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/drawablesizewillchange(_:scalefactor:))*