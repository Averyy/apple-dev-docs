# render(with:)

**Framework**: Touch Controller  
**Kind**: method

Renders the touch controls using the provided Metal render command encoder.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func render(with encoder: any MTLRenderCommandEncoder)
```

## Parameters

- `encoder`: The   to use for rendering.

## See Also

- [func drawableSizeWillChange(CGSize, scaleFactor: CGFloat)](tctouchcontroller/drawablesizewillchange(_:scalefactor:).md)
  Called when the drawable size changes.
- [func setupDefaultLayout(for: [TCControlLabel])](tctouchcontroller/setupdefaultlayout(for:).md)
  Sets up a default layout for the provided control labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/render(with:))*