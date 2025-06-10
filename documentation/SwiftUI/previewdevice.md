# PreviewDevice

**Framework**: SwiftUI  
**Kind**: struct

A simulator device that runs a preview.

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
struct PreviewDevice
```

#### Overview

Create a preview device by name, like “iPhone X”, or by model number, like “iPad8,1”. Use the device in a call to the [`previewDevice(_:)`](view/previewdevice(_:).md) modifier to set a preview device that doesn’t change when you change the run destination in Xcode:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewDevice(PreviewDevice(rawValue: "iPad Pro (11-inch)"))
    }
}
```

You can get a list of supported preview device names by using the `xcrun` command in the Terminal app:

```swift
% xcrun simctl list devicetypes
```

Additionally, you can use the following values for macOS platform development:

- “Mac”
- “Mac Catalyst”

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func previewDevice(PreviewDevice?) -> some View](view/previewdevice(_:).md)
  Overrides the device for a preview.
- [func previewLayout(PreviewLayout) -> some View](view/previewlayout(_:).md)
  Overrides the size of the container for the preview.
- [func previewInterfaceOrientation(InterfaceOrientation) -> some View](view/previewinterfaceorientation(_:).md)
  Overrides the orientation of the preview.
- [struct InterfaceOrientation](interfaceorientation.md)
  The orientation of the interface from the user’s perspective.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewdevice)*