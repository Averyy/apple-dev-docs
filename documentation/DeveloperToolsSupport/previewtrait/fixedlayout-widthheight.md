# fixedLayout(width:height:)

**Framework**: DeveloperToolsSupport  
**Kind**: method

Center the preview in a fixed size container with the given dimensions.

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
static func fixedLayout(width: CGFloat, height: CGFloat) -> PreviewTrait<T>
```

#### Discussion

This is the same as [`PreviewLayout.fixed(width:height:)`](previewlayout/fixed(width:height:).md).

## See Also

- [static var defaultLayout: PreviewTrait<Preview.ViewTraits>](previewtrait/defaultlayout.md)
  Center the preview in a container the size of the device on which the preview is running.
- [static func fixedLayout(width: CGFloat, height: CGFloat, depth: CGFloat) -> PreviewTrait<T>](previewtrait/fixedlayout(width:height:depth:).md)
  Centers the preview in a fixed-size, 3D container.
- [static var sizeThatFitsLayout: PreviewTrait<Preview.ViewTraits>](previewtrait/sizethatfitslayout.md)
  Fit the container to the size of the preview when offered the size of the device that the preview is running on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewtrait/fixedlayout(width:height:))*