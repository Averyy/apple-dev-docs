# setupDefaultLayout(for:)

**Framework**: Touch Controller  
**Kind**: method

Sets up a default layout for the provided control labels.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setupDefaultLayout(for labels: [TCControlLabel])
```

#### Discussion

This is used to automatically position control labels based on a predefined layout.

## Parameters

- `labels`: An array of   objects to be laid out.

## See Also

- [func drawableSizeWillChange(CGSize, scaleFactor: CGFloat)](tctouchcontroller/drawablesizewillchange(_:scalefactor:).md)
  Called when the drawable size changes.
- [func render(with: any MTLRenderCommandEncoder)](tctouchcontroller/render(with:).md)
  Renders the touch controls using the provided Metal render command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/setupdefaultlayout(for:))*