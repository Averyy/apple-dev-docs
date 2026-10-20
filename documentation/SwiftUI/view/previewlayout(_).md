# previewLayout(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Overrides the size of the container for the preview.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.0+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- tvOS 13.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: Use [`Preview(_:traits:_:body:)`](../preview%28_,traits,_,body%29.md) with [`sizeThatFitsLayout`](../../DeveloperToolsSupport/previewtrait/sizethatfitslayout.md) or  [`fixedLayout(width:height:)`](../../DeveloperToolsSupport/previewtrait/fixedlayout%28width,height%29.md) instead.

## Declaration

```swift
nonisolated
func previewLayout(_ value: PreviewLayout) -> some View
```

#### Return Value

A preview that uses the given layout.

#### Discussion

By default, previews use the `PreviewLayout/device` layout, which places the view inside a visual representation of the chosen device. You can instead tell a preview to use a different layout by choosing one of the `PreviewLayout` values, like `PreviewLayout/sizeThatFits`:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewLayout(.sizeThatFits)
    }
}
```

## Parameters

- `value`: A layout to use for preview.

## See Also

### Customizing a preview
- [func previewDevice(PreviewDevice?) -> some View](./previewdevice%28_%29.md)
  Overrides the device for a preview.
- [struct PreviewDevice](../previewdevice.md)
  A simulator device that runs a preview.
- [func previewInterfaceOrientation(InterfaceOrientation) -> some View](./previewinterfaceorientation%28_%29.md)
  Overrides the orientation of the preview.
- [struct InterfaceOrientation](../interfaceorientation.md)
  The orientation of the interface from the user’s perspective.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/previewlayout(_:))*