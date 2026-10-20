# PreviewLayout

**Framework**: DeveloperToolsSupport  
**Kind**: enum  
**Role**: Enumeration

A size constraint for a preview.

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
enum PreviewLayout
```

#### Overview

Customize the layout of a preview that you define using the [`PreviewProvider`](../SwiftUI/previewprovider.md) protocol by providing one of the preview layout values to the [`previewLayout(_:)`](../SwiftUI/view/previewlayout%28_%29.md) view modifier. For example, you can tell the preview to take up only the amount of space that the view requires with [`PreviewLayout.sizeThatFits`](./previewlayout/sizethatfits.md):

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewLayout(.sizeThatFits)
    }
}
```

> **Note**: When you migrate away from preview providers and to preview macros, you specify layout using one of the [`PreviewTrait`](./previewtrait.md) layout values with a macro that takes traits, like [`Preview(_:traits:_:body:)`](../SwiftUI/preview%28_,traits,_,body%29.md).

## Topics

### Getting a layout
- [PreviewLayout.device](./previewlayout/device.md)
  Center the preview in a container the size of the device on which the preview is running.
- [case fixed(width: CGFloat, height: CGFloat)](./previewlayout/fixed%28width,height%29.md)
  Center the preview in a fixed size container with the given dimensions.
- [case fixed3D(width: CGFloat, height: CGFloat, depth: CGFloat)](./previewlayout/fixed3d%28width,height,depth%29.md)
  Centers the preview in a fixed-size, 3D container.
- [PreviewLayout.sizeThatFits](./previewlayout/sizethatfits.md)
  Fit the container to the size of the preview when offered the size of the device that the preview is running on.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Preview definition
- [struct Preview](./preview.md)
  A base type that preview macros use to create previews.
- [struct PreviewTrait](./previewtrait.md)
  Customizations that you can apply to a preview.
- [protocol PreviewRegistry](./previewregistry.md)
  A protocol that the system uses to locate previews at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewlayout)*