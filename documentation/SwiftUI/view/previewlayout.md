# previewLayout(_:)

**Framework**: SwiftUI  
**Kind**: method

Overrides the size of the container for the preview.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

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

- [func previewDevice(PreviewDevice?) -> some View](view/previewdevice(_:).md)
  Overrides the device for a preview.
- [struct PreviewDevice](previewdevice.md)
  A simulator device that runs a preview.
- [func previewInterfaceOrientation(InterfaceOrientation) -> some View](view/previewinterfaceorientation(_:).md)
  Overrides the orientation of the preview.
- [struct InterfaceOrientation](interfaceorientation.md)
  The orientation of the interface from the user’s perspective.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/previewlayout(_:))*