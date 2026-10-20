# fixedLayout(width:height:depth:)

**Framework**: DeveloperToolsSupport  
**Kind**: method  
**Role**: Type Method

Centers the preview in a fixed-size, 3D container.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func fixedLayout(width: CGFloat, height: CGFloat, depth: CGFloat) -> PreviewTrait<T>
```

Available when `T` is `Preview.ViewTraits`.

#### Discussion

This is the same as [`PreviewLayout.fixed3D(width:height:depth:)`](../previewlayout/fixed3d%28width,height,depth%29.md).

## See Also

### Getting a layout
- [static var defaultLayout: PreviewTrait<Preview.ViewTraits>](./defaultlayout.md)
  Center the preview in a container the size of the device on which the preview is running.
- [static func fixedLayout(width: CGFloat, height: CGFloat) -> PreviewTrait<T>](./fixedlayout%28width,height%29.md)
  Center the preview in a fixed size container with the given dimensions.
- [static var sizeThatFitsLayout: PreviewTrait<Preview.ViewTraits>](./sizethatfitslayout.md)
  Fit the container to the size of the preview when offered the size of the device that the preview is running on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewtrait/fixedlayout(width:height:depth:))*