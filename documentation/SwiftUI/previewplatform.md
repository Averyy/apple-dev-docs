# PreviewPlatform

**Framework**: SwiftUI  
**Kind**: enum

Platforms that can run the preview.

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
enum PreviewPlatform
```

#### Overview

Xcode infers the platform for a preview based on the currently selected target. If you have a multiplatform target and want to suggest a particular target for a preview, implement the [`platform`](previewprovider/platform.md) computed property as a hint, and specify one of the preview platforms:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
    }

    static var platform: PreviewPlatform? {
        PreviewPlatform.tvOS
    }
}
```

## Topics

### Getting an operating system
- [PreviewPlatform.iOS](previewplatform/ios.md)
  Specifies iOS as the preview platform.
- [PreviewPlatform.macOS](previewplatform/macos.md)
  Specifies macOS as the preview platform.
- [PreviewPlatform.tvOS](previewplatform/tvos.md)
  Specifies tvOS as the preview platform.
- [PreviewPlatform.watchOS](previewplatform/watchos.md)
  Specifies watchOS as the preview platform.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [macro Previewable()](previewable().md)
  Tag allowing a dynamic property to appear inline in a preview.
- [protocol PreviewProvider](previewprovider.md)
  A type that produces view previews in Xcode.
- [func previewDisplayName(String?) -> some View](view/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
- [protocol PreviewModifier](previewmodifier.md)
  A type that defines an environment in which previews can appear.
- [struct PreviewModifierContent](previewmodifiercontent.md)
  The type-erased content of a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewplatform)*