# PreviewTrait

**Framework**: DeveloperToolsSupport  
**Kind**: struct

Customizations that you can apply to a preview.

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
struct PreviewTrait<T>
```

## Topics

### Initializers
- [init(PreviewTrait<T>...)](previewtrait/init(_:).md)
  Convenience to compose multiple traits into a single trait.
### Type Properties
- [static var defaultLayout: PreviewTrait<Preview.ViewTraits>](previewtrait/defaultlayout.md)
  Center the preview in a container the size of the device on which the preview is running.
- [static var landscapeLeft: PreviewTrait<Preview.ViewTraits>](previewtrait/landscapeleft.md)
  The device is in landscape mode, with the top of the device on the left.
- [static var landscapeRight: PreviewTrait<Preview.ViewTraits>](previewtrait/landscaperight.md)
  The device is in landscape mode, with the top of the device on the right.
- [static var portrait: PreviewTrait<Preview.ViewTraits>](previewtrait/portrait.md)
  The device is in portrait mode, with the top of the device on top.
- [static var portraitUpsideDown: PreviewTrait<Preview.ViewTraits>](previewtrait/portraitupsidedown.md)
  The device is in portrait mode, but is upside down.
- [static var sizeThatFitsLayout: PreviewTrait<Preview.ViewTraits>](previewtrait/sizethatfitslayout.md)
  Fit the container to the size of the preview when offered the size of the device that the preview is running on.
### Type Methods
- [static func fixedLayout(width: CGFloat, height: CGFloat) -> PreviewTrait<T>](previewtrait/fixedlayout(width:height:).md)
  Center the preview in a fixed size container with the given dimensions.
- [static func fixedLayout(width: CGFloat, height: CGFloat, depth: CGFloat) -> PreviewTrait<T>](previewtrait/fixedlayout(width:height:depth:).md)
  Centers the preview in a fixed-size, 3D container.
- [static func modifier(some PreviewModifier) -> PreviewTrait<T>](previewtrait/modifier(_:).md)
  Attach a `PreviewModifier` to the preview.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol PreviewRegistry](previewregistry.md)
  A protocol that the system uses to locate previews at runtime.
- [struct Preview](preview.md)
  A base type that preview macros use to create previews.
- [enum PreviewLayout](previewlayout.md)
  A size constraint for a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewtrait)*