# InterfaceOrientation

**Framework**: SwiftUI  
**Kind**: struct

The orientation of the interface from the user’s perspective.

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
struct InterfaceOrientation
```

#### Overview

By default, device previews appear right side up, using orientation [`portrait`](interfaceorientation/portrait.md). You can change the orientation with a call to the [`previewInterfaceOrientation(_:)`](view/previewinterfaceorientation(_:).md) modifier:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewInterfaceOrientation(.landscapeRight)
    }
}
```

## Topics

### Getting an orientation
- [static let portrait: InterfaceOrientation](interfaceorientation/portrait.md)
  The device is in portrait mode, with the top of the device on top.
- [static let portraitUpsideDown: InterfaceOrientation](interfaceorientation/portraitupsidedown.md)
  The device is in portrait mode, but is upside down.
- [static let landscapeLeft: InterfaceOrientation](interfaceorientation/landscapeleft.md)
  The device is in landscape mode, with the top of the device on the left.
- [static let landscapeRight: InterfaceOrientation](interfaceorientation/landscaperight.md)
  The device is in landscape mode, with the top of the device on the right.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func previewDevice(PreviewDevice?) -> some View](view/previewdevice(_:).md)
  Overrides the device for a preview.
- [struct PreviewDevice](previewdevice.md)
  A simulator device that runs a preview.
- [func previewLayout(PreviewLayout) -> some View](view/previewlayout(_:).md)
  Overrides the size of the container for the preview.
- [func previewInterfaceOrientation(InterfaceOrientation) -> some View](view/previewinterfaceorientation(_:).md)
  Overrides the orientation of the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/interfaceorientation)*