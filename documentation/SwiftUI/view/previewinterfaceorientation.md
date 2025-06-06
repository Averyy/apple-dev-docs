# previewInterfaceOrientation(_:)

**Framework**: SwiftUI  
**Kind**: method

Overrides the orientation of the preview.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func previewInterfaceOrientation(_ value: InterfaceOrientation) -> some View
```

#### Return Value

A preview that uses the given orientation.

#### Discussion

By default, device previews appear right side up, using orientation [`portrait`](interfaceorientation/portrait.md). You can change the orientation of a preview using one of the values in the [`InterfaceOrientation`](interfaceorientation.md) structure:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewInterfaceOrientation(.landscapeRight)
    }
}
```

## Parameters

- `value`: An orientation to use for preview.

## See Also

- [func previewDevice(PreviewDevice?) -> some View](view/previewdevice(_:).md)
  Overrides the device for a preview.
- [struct PreviewDevice](previewdevice.md)
  A simulator device that runs a preview.
- [func previewLayout(PreviewLayout) -> some View](view/previewlayout(_:).md)
  Overrides the size of the container for the preview.
- [struct InterfaceOrientation](interfaceorientation.md)
  The orientation of the interface from the user’s perspective.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/previewinterfaceorientation(_:))*