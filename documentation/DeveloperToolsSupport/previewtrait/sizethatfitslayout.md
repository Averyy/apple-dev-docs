# sizeThatFitsLayout

**Framework**: DeveloperToolsSupport  
**Kind**: property  
**Role**: Type Property

Fit the container to the size of the preview when offered the size of the device that the preview is running on.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
static var sizeThatFitsLayout: PreviewTrait<Preview.ViewTraits> { get }
```

Available when `T` is `Preview.ViewTraits`.

## Discussion

This is the same as [`PreviewLayout.sizeThatFits`](../previewlayout/sizethatfits.md).

## See Also

### Getting a layout
- [static var defaultLayout: PreviewTrait<Preview.ViewTraits>](./defaultlayout.md)
  Center the preview in a container the size of the device on which the preview is running.
- [static func fixedLayout(width: CGFloat, height: CGFloat) -> PreviewTrait<T>](./fixedlayout%28width,height%29.md)
  Center the preview in a fixed size container with the given dimensions.
- [static func fixedLayout(width: CGFloat, height: CGFloat, depth: CGFloat) -> PreviewTrait<T>](./fixedlayout%28width,height,depth%29.md)
  Centers the preview in a fixed-size, 3D container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewtrait/sizethatfitslayout)*